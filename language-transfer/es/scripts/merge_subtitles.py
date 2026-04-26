#!/usr/bin/env python3
"""
Merge human-transcribed markdown with machine-generated VTT subtitles.

This script aligns correct text from a human transcription (markdown)
with timestamps from a machine-generated VTT file.

Key insight: VTT may have EXTRA words (stutters, fillers) that markdown doesn't.
So we use the VTT as a guide to consume the right AMOUNT of markdown content.

Usage:
    python merge_subtitles.py <markdown_file> <vtt_file> [--output <output_file>]
"""

import argparse
import re
from pathlib import Path
from difflib import SequenceMatcher
from dataclasses import dataclass


@dataclass
class VTTCue:
    """Represents a single VTT subtitle cue."""
    index: int
    start_time: str
    end_time: str
    text: str
    speaker: str | None = None


def parse_vtt(vtt_path: Path) -> list[VTTCue]:
    """Parse a VTT file into a list of cues."""
    content = vtt_path.read_text(encoding="utf-8")
    lines = content.strip().split("\n")
    
    cues = []
    i = 0
    cue_index = 0
    
    while i < len(lines) and not re.match(r"\d{2}:\d{2}:\d{2}", lines[i]):
        i += 1
    
    while i < len(lines):
        line = lines[i].strip()
        
        timestamp_match = re.match(
            r"(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})",
            line
        )
        
        if timestamp_match:
            start_time = timestamp_match.group(1)
            end_time = timestamp_match.group(2)
            
            text_lines = []
            i += 1
            while i < len(lines) and lines[i].strip():
                text_line = lines[i].strip()
                if re.match(r"\d{2}:\d{2}:\d{2}", text_line):
                    break
                text_lines.append(text_line)
                i += 1
            
            full_text = " ".join(text_lines)
            
            speaker = None
            speaker_match = re.match(r"<v\s+(\w+)>(.+)", full_text)
            if speaker_match:
                speaker = speaker_match.group(1)
                full_text = speaker_match.group(2).strip()
            
            cues.append(VTTCue(
                index=cue_index,
                start_time=start_time,
                end_time=end_time,
                text=full_text,
                speaker=speaker
            ))
            cue_index += 1
        else:
            i += 1
    
    return cues


def strip_formatting(text: str) -> str:
    """Remove markdown formatting for comparison."""
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return text


def normalize_for_matching(text: str) -> str:
    """Normalize text for fuzzy matching."""
    text = strip_formatting(text)
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def remove_fillers(text: str) -> str:
    """Remove filler words from VTT text."""
    # Common speech fillers
    text = re.sub(r"\b(uh|um|er|ah|like)\b", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def count_content_words(text: str) -> int:
    """Count meaningful words (excluding fillers)."""
    cleaned = remove_fillers(text)
    normalized = normalize_for_matching(cleaned)
    words = normalized.split()
    return len(words)


def has_unclosed_formatting(text: str) -> bool:
    """Check if text has unclosed markdown formatting markers."""
    # Count asterisks that aren't part of complete formatting
    # Remove complete bold markers **text**
    temp = re.sub(r"\*\*[^*]+\*\*", "", text)
    # Remove complete italic markers *text*
    temp = re.sub(r"\*[^*]+\*", "", temp)
    # If any asterisks remain, formatting is incomplete
    return "*" in temp


def markdown_to_vtt_formatting(text: str) -> str:
    """Convert markdown formatting to VTT formatting.
    
    Only converts if formatting is complete (not split across cues).
    """
    if has_unclosed_formatting(text):
        # Don't convert - just strip the markers
        text = text.replace("**", "").replace("*", "")
        return text
    
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)
    return text


@dataclass 
class Token:
    """A word token with its position in formatted text and speaker."""
    formatted: str
    normalized: str
    start_pos: int
    end_pos: int
    speaker: str | None = None


def tokenize_formatted_text(text: str, speaker: str | None = None) -> list[Token]:
    """Tokenize text while tracking positions in formatted original."""
    tokens = []
    
    for match in re.finditer(r'\S+', text):
        word = match.group()
        start = match.start()
        end = match.end()
        
        normalized = strip_formatting(word).lower()
        normalized = re.sub(r'[^\w]', '', normalized)
        
        if normalized:
            tokens.append(Token(
                formatted=word,
                normalized=normalized,
                start_pos=start,
                end_pos=end,
                speaker=speaker
            ))
    
    return tokens


def parse_markdown_to_tokens(md_path: Path) -> tuple[str, list[Token]]:
    """Parse markdown file and return full text with tokens, tracking speakers."""
    content = md_path.read_text(encoding="utf-8")
    
    all_tokens = []
    text_parts = []
    current_offset = 0
    current_speaker = None
    
    for line in content.split("\n"):
        stripped = line.strip()
        
        # Skip title lines
        if stripped.startswith("#"):
            continue
        
        # Check for speaker label at start of line
        speaker_match = re.match(r"^(Teacher|Student):\s*", stripped)
        if speaker_match:
            current_speaker = speaker_match.group(1)
            stripped = stripped[speaker_match.end():]
        elif line.startswith("  ") and stripped:
            # Continuation line (indented) - keep current speaker
            pass
        elif stripped == "":
            # Empty line - keep current speaker for next paragraph
            continue
        
        if not stripped:
            continue
        
        # Add space separator if needed
        if text_parts:
            text_parts.append(" ")
            current_offset += 1
        
        # Tokenize this line segment with speaker info
        for match in re.finditer(r'\S+', stripped):
            word = match.group()
            start = current_offset + match.start()
            end = current_offset + match.end()
            
            normalized = strip_formatting(word).lower()
            normalized = re.sub(r'[^\w]', '', normalized)
            
            if normalized:
                all_tokens.append(Token(
                    formatted=word,
                    normalized=normalized,
                    start_pos=start,
                    end_pos=end,
                    speaker=current_speaker
                ))
        
        text_parts.append(stripped)
        current_offset += len(stripped)
    
    full_text = "".join(text_parts)
    
    return full_text, all_tokens


def get_first_content_word(text: str) -> str:
    """Get the first meaningful word from text (normalized)."""
    cleaned = remove_fillers(text)
    normalized = normalize_for_matching(cleaned)
    words = normalized.split()
    return words[0] if words else ""


def first_word_matches(vtt_text: str, md_tokens: list[Token], start_pos: int) -> bool:
    """Check if the first content word of VTT matches the first markdown token."""
    if start_pos >= len(md_tokens):
        return False
    
    vtt_first = get_first_content_word(vtt_text)
    md_first = md_tokens[start_pos].normalized
    
    if not vtt_first or not md_first:
        return True  # Can't check, assume OK
    
    # Exact match
    if vtt_first == md_first:
        return True
    
    # VTT word is subset of markdown word (common transcription truncation)
    # e.g., VTT "s" for markdown "es", VTT "a" for markdown "a" 
    if vtt_first in md_first or md_first in vtt_first:
        return True
    
    # Allow some fuzzy matching for the first word
    ratio = SequenceMatcher(None, vtt_first, md_first).ratio()
    return ratio >= 0.7


def get_distinctive_words(text: str) -> set[str]:
    """Extract distinctive content words (longer words that help identify the text)."""
    fillers = {'uh', 'um', 'er', 'ah', 'like', 'you', 'know', 'just', 'that', 'this', 'with', 'from', 'have', 'will', 'been'}
    words = re.findall(r'[a-zA-Z]+', text.lower())
    # Keep words with 4+ chars as they're more distinctive
    return {w for w in words if len(w) >= 4 and w not in fillers}


def content_matches(vtt_text: str, md_text: str) -> bool:
    """
    Check if VTT and markdown text have compatible content.
    Catches cases like 'natural' vs 'normal' where the text is different.
    """
    vtt_words = get_distinctive_words(vtt_text)
    md_words = get_distinctive_words(md_text)
    
    if not vtt_words or not md_words:
        return True  # Can't check, assume OK
    
    # Check if VTT has distinctive words that are completely absent from markdown
    # Allow fuzzy matching for each word
    for vtt_word in vtt_words:
        found = False
        for md_word in md_words:
            if vtt_word == md_word:
                found = True
                break
            # Check fuzzy similarity
            if SequenceMatcher(None, vtt_word, md_word).ratio() >= 0.85:
                found = True
                break
        if not found:
            # VTT has a word that doesn't appear in markdown - content mismatch
            return False
    
    return True


def vtt_ends_with_sentence(text: str) -> bool:
    """Check if VTT text ends with sentence-ending punctuation."""
    text = text.strip()
    return text.endswith(('.', '!', '?'))


def is_phonetic_token(token: Token) -> bool:
    """Check if a token is a phonetic notation like /ah/, /eh/, etc."""
    return token.formatted.startswith('/') or token.formatted.endswith('/')


def find_best_end_position(
    vtt_text: str,
    vtt_speaker: str | None,
    md_tokens: list[Token],
    full_md_text: str,
    start_pos: int,
    expected_words: int
) -> tuple[int, float]:
    """
    Find the best end position in md_tokens for matching vtt_text.
    Returns (end_pos, score).
    """
    vtt_norm = normalize_for_matching(vtt_text)
    vtt_ends_sentence = vtt_ends_with_sentence(vtt_text)
    start_speaker = md_tokens[start_pos].speaker if start_pos < len(md_tokens) else None
    
    best_end = min(start_pos + expected_words, len(md_tokens))
    best_score = 0.0
    
    # Try different end positions
    min_end = start_pos + max(1, expected_words - 3)
    max_end = min(len(md_tokens), start_pos + expected_words + 3)
    
    for end in range(min_end, max_end + 1):
        if end <= start_pos:
            continue
        
        # Check for speaker change within the segment
        # If we'd be crossing a speaker boundary, that's usually wrong
        has_speaker_change = False
        for i in range(start_pos, end):
            if md_tokens[i].speaker != start_speaker:
                has_speaker_change = True
                break
        
        md_norm = " ".join(t.normalized for t in md_tokens[start_pos:end])
        score = SequenceMatcher(None, vtt_norm, md_norm).ratio()
        
        # Small preference for expected length
        length_diff = abs((end - start_pos) - expected_words)
        score -= length_diff * 0.02
        
        # Heavy penalty for crossing speaker boundaries
        if has_speaker_change:
            score -= 0.25
        
        # Penalty for sentence boundary mismatch
        # If VTT ends with sentence punctuation, prefer markdown segments
        # that also end with sentence punctuation (or at least not mid-sentence)
        if vtt_ends_sentence and end < len(md_tokens):
            end_char = md_tokens[end - 1].end_pos
            # Check the character right after the last token
            if end_char < len(full_md_text):
                next_chars = full_md_text[end_char:end_char + 10].strip()
                # Remove markdown formatting markers to see actual next word
                next_chars = next_chars.lstrip('*_')
                # If next char is a lowercase letter, we're mid-sentence - penalize
                if next_chars and next_chars[0].islower():
                    score -= 0.15
        
        if score > best_score:
            best_score = score
            best_end = end
    
    # Extend to include phonetic notations that immediately follow
    # (e.g., "/ah/", "/eh/") since these are often represented differently in VTT
    # But only if same speaker
    while (best_end < len(md_tokens) and 
           is_phonetic_token(md_tokens[best_end]) and
           md_tokens[best_end].speaker == start_speaker):
        best_end += 1
    
    return best_end, best_score


@dataclass
class Alignment:
    """An alignment between a VTT cue and markdown tokens."""
    cue_idx: int
    md_start: int
    md_end: int
    score: float
    is_anchor: bool = False


def find_best_match_in_range(
    vtt_text: str,
    md_tokens: list[Token],
    full_md_text: str,
    search_start: int,
    search_end: int,
    expected_words: int
) -> tuple[int, int, float]:
    """
    Find the best matching segment within a bounded range of markdown tokens.
    Returns (start_pos, end_pos, score).
    """
    vtt_norm = normalize_for_matching(vtt_text)
    vtt_first = get_first_content_word(vtt_text)
    
    best_start = search_start
    best_end = min(search_start + expected_words, search_end)
    best_score = 0.0
    
    # Try different starting positions within the range
    for start in range(search_start, min(search_end, search_start + 100)):
        if start >= len(md_tokens):
            break
            
        # Check if first word matches
        md_first = md_tokens[start].normalized
        first_word_ok = (
            vtt_first == md_first or
            (vtt_first in md_first or md_first in vtt_first) or
            SequenceMatcher(None, vtt_first, md_first).ratio() >= 0.5
        )
        
        if not first_word_ok:
            continue
        
        # Try different end positions
        for end in range(start + 1, min(search_end + 1, start + expected_words + 5)):
            if end > len(md_tokens):
                break
                
            md_norm = " ".join(t.normalized for t in md_tokens[start:end])
            score = SequenceMatcher(None, vtt_norm, md_norm).ratio()
            
            # Small preference for expected length
            length_diff = abs((end - start) - expected_words)
            score -= length_diff * 0.02
            
            if score > best_score:
                best_score = score
                best_start = start
                best_end = end
    
    return best_start, best_end, best_score


def validate_match_with_lookahead(
    cues: list[VTTCue],
    cue_idx: int,
    md_tokens: list[Token],
    proposed_end: int,
    num_lookahead: int = 5
) -> bool:
    """
    Check if the next few VTT cues can find matches after the proposed end position.
    This helps avoid consuming markdown for garbled VTT segments.
    
    The key insight: if this is the RIGHT place to consume markdown, then the
    NEXT few VTT cues should also find good matches in the IMMEDIATELY following
    markdown tokens. If we have to search too far or can't find matches, this
    is probably a false positive (garbled VTT matching random markdown).
    """
    matches_found = 0
    cues_checked = 0
    md_pos = proposed_end
    
    for i in range(1, min(num_lookahead + 1, len(cues) - cue_idx)):
        next_cue = cues[cue_idx + i]
        if not next_cue.text.strip():
            continue
        
        next_content_words = count_content_words(next_cue.text)
        if next_content_words == 0:
            continue
        
        cues_checked += 1
        next_vtt_first = get_first_content_word(next_cue.text)
        next_vtt_norm = normalize_for_matching(next_cue.text)
        
        # Check if we can find a match in the NEARBY tokens
        # Use a tight window - if we have to search far, it's suspect
        search_window = max(20, next_content_words * 3)
        best_score = 0.0
        best_start = md_pos
        
        for start in range(md_pos, min(len(md_tokens), md_pos + search_window)):
            md_first = md_tokens[start].normalized
            
            if (next_vtt_first == md_first or 
                SequenceMatcher(None, next_vtt_first, md_first).ratio() >= 0.7):
                
                for end in range(start + 1, min(len(md_tokens) + 1, start + next_content_words + 3)):
                    md_norm = " ".join(t.normalized for t in md_tokens[start:end])
                    score = SequenceMatcher(None, next_vtt_norm, md_norm).ratio()
                    if score > best_score:
                        best_score = score
                        best_start = start
        
        if best_score >= 0.6:
            matches_found += 1
            # Advance md_pos to where we found the match
            md_pos = best_start + next_content_words
        else:
            # No match found - advance by expected words anyway
            md_pos += next_content_words
    
    if cues_checked == 0:
        return True  # No cues to check, assume OK
    
    # Require majority of checked cues to have good matches
    return matches_found >= (cues_checked + 1) // 2


def merge_subtitles(cues: list[VTTCue], md_path: Path, verbose: bool = False) -> list[VTTCue]:
    """
    Merge VTT cues with correct text from markdown using sequential alignment.
    
    Uses a greedy sequential approach: process cues in order, always consuming
    markdown from the current position forward. The key insight is that both
    VTT and markdown follow the same temporal order, so we never need to go
    backwards.
    
    Key principle: Markdown is the source of truth. VTT only provides timestamps.
    """
    full_md_text, md_tokens = parse_markdown_to_tokens(md_path)
    
    if verbose:
        print(f"Total markdown tokens: {len(md_tokens)}")
        print()
    
    result_cues = []
    md_pos = 0  # Current position - always moves forward
    
    for cue_idx, cue in enumerate(cues):
        if not cue.text.strip():
            result_cues.append(cue)
            continue
        
        content_words = count_content_words(cue.text)
        if content_words == 0:
            result_cues.append(cue)
            continue
        
        vtt_norm = normalize_for_matching(cue.text)
        vtt_first = get_first_content_word(cue.text)
        
        # Search forward from current position with a reasonable window
        # Since we process sequentially, the match should be close to md_pos
        search_limit = min(len(md_tokens), md_pos + 80)
        
        best_start = md_pos
        best_end = md_pos
        best_score = 0.0
        
        for start in range(md_pos, search_limit):
            if start >= len(md_tokens):
                break
            
            md_first = md_tokens[start].normalized
            
            # Check if first word is a potential match
            first_word_ok = (
                vtt_first == md_first or
                (vtt_first in md_first or md_first in vtt_first) or
                SequenceMatcher(None, vtt_first, md_first).ratio() >= 0.6
            )
            
            if not first_word_ok:
                continue
            
            # Try different end positions
            for end in range(start + 1, min(len(md_tokens) + 1, start + content_words + 5)):
                md_norm = " ".join(t.normalized for t in md_tokens[start:end])
                score = SequenceMatcher(None, vtt_norm, md_norm).ratio()
                
                # Penalty for skipping too much
                skip_distance = start - md_pos
                if skip_distance > 5:
                    score -= (skip_distance - 5) * 0.01
                
                # Slight preference for starting at current position
                if start == md_pos:
                    score += 0.05
                
                if score > best_score:
                    best_score = score
                    best_start = start
                    best_end = end
        
        # If we're skipping content OR if score is borderline, validate with lookahead
        skip_distance = best_start - md_pos
        use_lookahead = skip_distance > 10 or (best_score < 0.85 and skip_distance > 3)
        if best_score >= 0.5 and best_end > best_start and use_lookahead:
            # Large skip - validate that next cues also match
            if not validate_match_with_lookahead(cues, cue_idx, md_tokens, best_end):
                if verbose:
                    print(f"[{cue.start_time}] score={best_score:.2f} SKIP (lookahead failed, skip={skip_distance})")
                    print(f"  VTT: {cue.text}")
                # Don't advance md_pos - this is likely a false match
                result_cues.append(VTTCue(
                    index=cue.index,
                    start_time=cue.start_time,
                    end_time=cue.end_time,
                    text=cue.text,
                    speaker=cue.speaker
                ))
                continue
        
        # Special case: if we have exactly 1 expected word and there's a single
        # token at md_pos that hasn't been consumed, use it even with low score.
        # This handles completely wrong transcriptions like "Therefore?" -> "Verbo?"
        if (content_words == 1 and 
            md_pos < len(md_tokens) and 
            best_score < 0.5):
            # Check if the next cue can match the token after this one
            next_cue_matches = False
            if cue_idx + 1 < len(cues):
                next_cue = cues[cue_idx + 1]
                if next_cue.text.strip():
                    next_vtt_first = get_first_content_word(next_cue.text)
                    if md_pos + 1 < len(md_tokens):
                        next_md_first = md_tokens[md_pos + 1].normalized
                        if (next_vtt_first == next_md_first or
                            SequenceMatcher(None, next_vtt_first, next_md_first).ratio() >= 0.7):
                            next_cue_matches = True
            
            if next_cue_matches:
                # Use the current token even though the score is low
                best_start = md_pos
                best_end = md_pos + 1
                best_score = 0.5  # Set to threshold to pass
                if verbose:
                    print(f"  [using single token at md_pos due to context]")
        
        # Decide whether to use the match
        # Use a low threshold since markdown is the source of truth
        if best_score >= 0.5 and best_end > best_start:
            start_char = md_tokens[best_start].start_pos
            end_char = md_tokens[best_end - 1].end_pos
            raw_text = full_md_text[start_char:end_char]
            
            # Handle unclosed formatting
            if has_unclosed_formatting(raw_text):
                new_text = raw_text.replace("**", "").replace("*", "")
            else:
                new_text = markdown_to_vtt_formatting(raw_text)
            
            new_speaker = md_tokens[best_start].speaker
            
            # Update position - always move forward
            md_pos = best_end
            
            if verbose:
                skip_note = f" [skip {best_start - (md_pos - (best_end - best_start))}]" if best_start > (md_pos - (best_end - best_start)) else ""
                print(f"[{cue.start_time}] score={best_score:.2f} md={best_start}-{best_end}{skip_note}")
                print(f"  VTT: {cue.text}")
                print(f"  NEW: {new_text}")
            
            result_cues.append(VTTCue(
                index=cue.index,
                start_time=cue.start_time,
                end_time=cue.end_time,
                text=new_text,
                speaker=new_speaker
            ))
        else:
            # Low confidence - but we still want to try to advance md_pos
            # to avoid getting stuck. Use the expected word count.
            if verbose:
                print(f"[{cue.start_time}] score={best_score:.2f} KEEP (low confidence)")
                print(f"  VTT: {cue.text}")
            
            # Advance by expected words to keep sync
            md_pos = min(len(md_tokens), md_pos + content_words)
            
            result_cues.append(VTTCue(
                index=cue.index,
                start_time=cue.start_time,
                end_time=cue.end_time,
                text=cue.text,
                speaker=cue.speaker
            ))
    
    return result_cues


def format_vtt(cues: list[VTTCue], include_speakers: bool = True) -> str:
    """Format cues back to VTT format."""
    lines = ["WEBVTT", ""]
    
    for cue in cues:
        lines.append(f"{cue.start_time} --> {cue.end_time}")
        if include_speakers and cue.speaker:
            lines.append(f"<v {cue.speaker}>{cue.text}")
        else:
            lines.append(cue.text)
        lines.append("")
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Merge human transcription with machine-generated subtitles"
    )
    parser.add_argument("markdown", type=Path, help="Path to markdown transcription")
    parser.add_argument("vtt", type=Path, help="Path to VTT subtitle file")
    parser.add_argument(
        "--output", "-o", type=Path, 
        help="Output VTT file (default: overwrites input VTT)"
    )
    parser.add_argument(
        "--no-speakers", action="store_true",
        help="Don't include speaker tags in output"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show detailed matching info"
    )
    
    args = parser.parse_args()
    
    if not args.markdown.exists():
        print(f"Error: Markdown file not found: {args.markdown}")
        return 1
    
    if not args.vtt.exists():
        print(f"Error: VTT file not found: {args.vtt}")
        return 1
    
    print(f"Parsing VTT: {args.vtt}")
    cues = parse_vtt(args.vtt)
    print(f"  Found {len(cues)} cues")
    
    print(f"Parsing markdown: {args.markdown}")
    
    print("Aligning and merging...")
    merged_cues = merge_subtitles(cues, args.markdown, verbose=args.verbose)
    
    output_path = args.output or args.vtt
    print(f"Writing output: {output_path}")
    
    vtt_content = format_vtt(merged_cues, include_speakers=not args.no_speakers)
    output_path.write_text(vtt_content, encoding="utf-8")
    
    print("Done!")
    return 0


if __name__ == "__main__":
    exit(main())
