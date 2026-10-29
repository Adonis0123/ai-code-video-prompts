#!/usr/bin/env bash
# Re-render the tutorial with the real replica film, then compress and QC.
# Usage: bash scripts/rerender.sh            (run from anywhere)
# Needs: replica/renders/editor-replica.mp4, ffmpeg, assets/wb/ (WorkBuddy mascot art, not in git)
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$HERE/../replica/renders/editor-replica.mp4"
OUT="$HERE/renders/workbuddy-tutorial.mp4"

if [ ! -f "$SRC" ]; then
  echo "missing $SRC: render replica/ first (cd replica && npm run render)" >&2
  exit 1
fi
cp "$SRC" "$HERE/assets/editor-replica.mp4"
echo "using replica: $SRC"

cd "$HERE"
npm run check
npm run render
RAW="$(ls -t renders/*.mp4 | grep -v 'workbuddy-tutorial.mp4' | head -1)"
ffmpeg -v error -y -i "$RAW" -an -c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p -movflags +faststart "$OUT"
ffmpeg -v error -y -i "$OUT" -vf "fps=1,scale=320:-1,tile=9x5" -frames:v 1 renders/contact-sheet.jpg
echo "blackdetect (empty = no black segments):"
ffmpeg -v info -i "$OUT" -vf "blackdetect=d=0.3:pix_th=0.10" -an -f null - 2>&1 | grep blackdetect || true
ffprobe -v error -show_entries format=duration,size -of default=nw=1 "$OUT"
