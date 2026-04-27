# VTT Transcript Processing

## Standard Process for New Tracks

Follow this 3-step workflow for processing new VTT tracks:

### Step 1: Fix the Markdown Source

1. Read the current markdown file (`transcripts/extracted/markdown/track-XX.md`)
2. Compare with the correct transcript text (provided by user from PDF reader - no formatting but correct content order)
3. Update content to fix parsing/OCR errors while **preserving existing markdown formatting**:
   - Keep `**bold**` for Spanish words
   - Keep `*italic*` for English translations/prompts
   - Keep `T:` and `S:` speaker labels
4. Do NOT remove formatting just because the reference text lacks it - the markdown has good formatting, just bad content from OCR

### Step 2: Run the Merge Script

```bash
cd language-transfer/es
python scripts/merge_subtitles.py transcripts/extracted/markdown/track-XX.md transcripts/XX.vtt --output transcripts/XX.vtt
```

This creates a "rough merge" aligning markdown content with VTT timestamps. The merge is imperfect and needs manual fixes.

### Step 3: In-Context VTT Fixes

Load the full VTT file into context and systematically fix issues using `StrReplace`:

1. **Speaker assignments**: Change `Speaker 1`, `Speaker 2` → `Teacher`, `Student` as appropriate
2. **Formatting**: Add missing `<b>`, `<i>` tags:
   - Spanish words in Student responses: `<b>bold</b>`
   - English prompts from Teacher: `<i>italic</i>`
3. **Content errors**: Fix transcription mistakes by comparing against the reference transcript
4. **Split combined cues**: Where one cue contains both Teacher and Student content, split into separate cues
5. **Merge fragmented cues**: Where a single sentence is split across multiple cues incorrectly, combine them
6. After finishing, run `grep -n "Speaker" XX.vtt` to verify no "Speaker" labels remain

## Common Issues & Fixes

### Merge script output issues
- **Wrong speaker**: Script may assign Teacher to Student lines or vice versa
- **Combined cues**: Multiple speakers merged into one cue (split them manually)
- **Missing formatting**: `<b>`, `<i>` tags not applied (add them)
- **Content misalignment**: Text from wrong part of transcript (realign manually)

### StrReplace failures
- Ensure `old_string` exactly matches file content (including formatting, newlines)
- Read the actual file content first to construct correct `old_string`
- For complex changes, split into smaller `StrReplace` operations

## Important Rules

- Do NOT stage files unless explicitly requested
- Do NOT remove existing formatting when fixing content
- Spanish words in Student responses should be `<b>bold</b>`
- English prompts from Teacher should be `<i>italic</i>`
- Speaker labels: `<v Teacher>` and `<v Student>`
