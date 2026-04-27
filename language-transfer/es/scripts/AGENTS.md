# Merge Subtitles Post-Processing

After running `merge_subtitles.py` on a VTT file, always perform a manual diff review before committing.

## Required Review Steps

1. **Load the full diff into context**:
   ```bash
   git diff <file>.vtt
   ```

2. **Check for these common issues**:

   ### Issues from corrupted markdown source
   - **Garbled/merged text**: OCR artifacts like `"***I****want*` or merged lines
   - **Wrong content**: Text from wrong part of transcript aligned to a cue
   - **Truncated sentences**: Partial content like `something.` instead of full sentence
   - **Extra characters**: Trailing letters like `Intento publicarlo.I`

   ### Issues from merge algorithm
   - **Lost formatting**: Bold (`<b>`) or italic (`<i>`) tags removed when they should be preserved
   - **Speaker misattribution**: Wrong speaker assigned to a cue (check T→Teacher, S→Student mapping)
   - **Content drift**: Alignment getting progressively more wrong as file progresses

3. **Remediation**:

   ### If markdown source is corrupted
   - **Do NOT merge** - the VTT machine transcription is likely more accurate
   - Fix the markdown source first, then re-run merge
   - Or manually edit VTT to add formatting from markdown while preserving VTT text

   ### If merge algorithm issues
   - For lost formatting: Restore formatting from markdown
   - For speaker issues: Correct speaker tags based on markdown labels
   - For alignment drift: Restore VTT and re-run with `--verbose` to debug

4. **Verify markdown quality first**:
   Before running merge, scan the markdown for:
   - Lines with garbled formatting markers (`***`, `****`, mismatched `*`)
   - Merged speaker lines (content from T and S on same line)
   - Orphaned text fragments without speaker labels
   - Obvious OCR errors in Spanish words

## Red Flags in Diff Output

**Markdown source issues (DO NOT COMMIT):**
- Content completely different from original VTT (wrong alignment)
- Truncated sentences replacing full sentences
- Garbled formatting markers in output
- Same content appearing in multiple cues

**Fixable merge issues:**
- Lines only gaining/losing `<b>`, `<i>` tags (formatting changes)
- Speaker label corrections (Speaker 1 → Teacher)
- Minor text corrections (e.g., "Nocchiero" → "No quiero")
