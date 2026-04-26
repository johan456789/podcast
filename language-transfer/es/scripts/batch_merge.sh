#!/bin/bash
# Batch process all tracks to merge human transcriptions with machine-generated subtitles
#
# Usage:
#   ./batch_merge.sh                    # Process all tracks
#   ./batch_merge.sh 01 02 03          # Process specific tracks
#   ./batch_merge.sh --dry-run          # Show what would be done

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
MARKDOWN_DIR="$PROJECT_DIR/transcripts/extracted/markdown"
VTT_DIR="$PROJECT_DIR/transcripts"

DRY_RUN=false

# Parse arguments
TRACKS=()
for arg in "$@"; do
    case $arg in
        --dry-run)
            DRY_RUN=true
            ;;
        *)
            TRACKS+=("$arg")
            ;;
    esac
done

# If no tracks specified, find all available
if [ ${#TRACKS[@]} -eq 0 ]; then
    for md_file in "$MARKDOWN_DIR"/track-*.md; do
        if [ -f "$md_file" ]; then
            # Extract track number from filename
            basename=$(basename "$md_file")
            track_num=$(echo "$basename" | sed 's/track-\([0-9]*\)\.md/\1/')
            TRACKS+=("$track_num")
        fi
    done
fi

echo "Processing ${#TRACKS[@]} tracks..."
echo ""

success_count=0
error_count=0

for track in "${TRACKS[@]}"; do
    # Pad track number if needed
    track_padded=$(printf "%02d" "$track" 2>/dev/null || echo "$track")
    
    md_file="$MARKDOWN_DIR/track-${track_padded}.md"
    vtt_file="$VTT_DIR/${track_padded}.vtt"
    # Check if files exist
    if [ ! -f "$md_file" ]; then
        echo "⚠ Track $track_padded: Markdown file not found: $md_file"
        ((error_count++))
        continue
    fi
    
    if [ ! -f "$vtt_file" ]; then
        echo "⚠ Track $track_padded: VTT file not found: $vtt_file"
        ((error_count++))
        continue
    fi
    
    if $DRY_RUN; then
        echo "Would process: track-${track_padded}.md + ${track_padded}.vtt (overwrite)"
    else
        echo -n "Processing track $track_padded... "
        # Overwrite the original VTT file directly (no --output flag)
        if python "$SCRIPT_DIR/merge_subtitles.py" "$md_file" "$vtt_file" > /dev/null 2>&1; then
            echo "✓"
            ((success_count++))
        else
            echo "✗ (error)"
            ((error_count++))
        fi
    fi
done

echo ""
echo "Summary: $success_count succeeded, $error_count failed"
