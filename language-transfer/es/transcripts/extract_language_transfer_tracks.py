#!/usr/bin/env python3
import html
import re
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
PDF = SCRIPT_DIR / "Complete+Spanish+transcript+-+2019+final.pdf"
OUT_ROOT = SCRIPT_DIR / "extracted"


def run_pdftohtml() -> str:
    return subprocess.check_output(
        ["pdftohtml", "-xml", "-stdout", str(PDF)],
        stderr=subprocess.DEVNULL,
    ).decode("utf-8", errors="replace")


def styled_text(markup: str) -> str:
    markup = re.sub(r"<(?!/?(?:b|i)\b)[^>]+>", "", markup)
    parts = []
    bold = False
    italic = False
    tokens = re.split(r"(</?[bi]>)", markup)
    for token in tokens:
        if not token:
            continue
        if token == "<b>":
            bold = True
            continue
        if token == "</b>":
            bold = False
            continue
        if token == "<i>":
            italic = True
            continue
        if token == "</i>":
            italic = False
            continue

        text = html.escape(html.unescape(token))
        if bold and italic:
            parts.append(f"<strong><em>{text}</em></strong>")
        elif bold:
            parts.append(f"<strong>{text}</strong>")
        elif italic:
            parts.append(f"<em>{text}</em>")
        else:
            parts.append(text)
    return "".join(parts)


def html_to_md(s: str) -> str:
    s = re.sub(r"<strong>(.*?)</strong>", r"**\1**", s)
    s = re.sub(r"<em>(.*?)</em>", r"*\1*", s)
    s = html.unescape(s)
    return s


def normalize_line(s: str) -> str:
    s = s.replace("\u00a0", " ")
    s = re.sub(r" {2,}", " ", s)
    return s.rstrip()


def parse_attrs(attrs: str) -> dict[str, str]:
    return dict(re.findall(r'(\w+)="([^"]*)"', attrs))


def page_lines(page: dict) -> list[dict]:
    spans = []
    for attrs_raw, markup in re.findall(r"<text\s+([^>]*)>(.*?)</text>", page["body"]):
        attrs = parse_attrs(attrs_raw)
        raw_markup = re.sub(r"<[^>]+>", "", markup)
        raw = html.unescape(raw_markup)
        if not raw.strip():
            continue
        spans.append(
            {
                "top": int(attrs["top"]),
                "left": int(attrs["left"]),
                "html": styled_text(markup),
                "plain": raw,
            }
        )

    grouped = {}
    for span in spans:
        grouped.setdefault(span["top"], []).append(span)

    lines = []
    for top in sorted(grouped):
        row = sorted(grouped[top], key=lambda s: s["left"])
        line_html = normalize_line("".join(s["html"] for s in row))
        line_plain = normalize_line("".join(s["plain"] for s in row))
        if line_plain:
            lines.append(
                {
                    "top": top,
                    "left": min(s["left"] for s in row),
                    "html": line_html,
                    "plain": line_plain,
                }
            )
    return lines


def outline_tracks(xml: str) -> list[tuple[int, int]]:
    tracks = []
    for page, label in re.findall(r'<item page="(\d+)">(.*?)</item>', xml):
        label = html.unescape(label).strip()
        match = re.fullmatch(r"Track (\d+)", label)
        if match:
            tracks.append((int(match.group(1)), int(page)))
    return sorted(tracks)


def is_track_heading(line: dict, track: int) -> bool:
    plain = re.sub(r"\s+", " ", line["plain"]).strip()
    return plain == f"Track {track}" and line["top"] < 160


def build_track(track: int, pages: list[dict]) -> list[str]:
    md_lines = []
    previous_top = None
    previous_page = None

    for page in pages:
        page_no = page["number"]
        for line in page_lines(page):
            if is_track_heading(line, track):
                continue
            # Skip accidental page/header whitespace artifacts.
            if not line["plain"].strip():
                continue

            if previous_top is not None:
                same_page = page_no == previous_page
                gap = line["top"] - previous_top if same_page else 999
                starts_dialogue = bool(re.match(r"^(Teacher|Student):", line["plain"]))
                if not same_page or gap > 34 or starts_dialogue:
                    md_lines.append("")

            md_line = html_to_md(line["html"])
            if line["left"] >= 105:
                md_line = "  " + md_line
            md_lines.append(md_line)
            previous_top = line["top"]
            previous_page = page_no

    return md_lines


def main() -> int:
    xml = run_pdftohtml()
    pages = {}
    page_re = re.compile(r"<page\s+([^>]*)>(.*?)</page>", re.DOTALL)
    for attrs_raw, body in page_re.findall(xml):
        attrs = parse_attrs(attrs_raw)
        pages[int(attrs["number"])] = {"number": int(attrs["number"]), "body": body}
    tracks = outline_tracks(xml)
    if not tracks:
        print("No tracks found in PDF outline", file=sys.stderr)
        return 1

    md_dir = OUT_ROOT / "markdown"
    md_dir.mkdir(parents=True, exist_ok=True)

    for idx, (track, start_page) in enumerate(tracks):
        end_page = tracks[idx + 1][1] - 1 if idx + 1 < len(tracks) else max(pages)
        track_pages = [pages[n] for n in range(start_page, end_page + 1) if n in pages]
        md_lines = build_track(track, track_pages)

        stem = f"track-{track:02d}"
        md_text = f"# Track {track}\n\n" + "\n".join(md_lines).strip() + "\n"
        (md_dir / f"{stem}.md").write_text(md_text, encoding="utf-8")

    print(f"Wrote {len(tracks)} Markdown tracks to {md_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
