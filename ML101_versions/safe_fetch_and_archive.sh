#!/usr/bin/env bash
set -euo pipefail

# Fetches remote main safely and archives selected ML101 files into ML101_versions/
# without modifying live top-level files.
#
# Usage:
#   bash ML101_versions/safe_fetch_and_archive.sh [archive_name]
#
# Optional env var:
#   REMOTE_URL=https://github.com/<owner>/<repo>.git
#
# Example:
#   bash ML101_versions/safe_fetch_and_archive.sh fetched-main-2026-03-17

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ARCHIVE_NAME="${1:-fetched-main-$(date +%Y-%m-%d-%H%M%S)}"
ARCHIVE_DIR="$ROOT_DIR/ML101_versions/$ARCHIVE_NAME"
REMOTE_URL="${REMOTE_URL:-https://github.com/nirav2000/ML.git}"

cd "$ROOT_DIR"

echo "[1/4] Fetching remote main into FETCH_HEAD (no checkout changes)"
git fetch "$REMOTE_URL" main --prune

echo "[2/4] Creating archive directory: $ARCHIVE_DIR"
mkdir -p "$ARCHIVE_DIR"

echo "[3/4] Archiving candidate files from FETCH_HEAD"
for file in ML101.html ml101-explainer.js VERSION_HISTORY.md; do
  if git cat-file -e "FETCH_HEAD:$file" 2>/dev/null; then
    git show "FETCH_HEAD:$file" > "$ARCHIVE_DIR/$file"
    echo "  archived: $file"
  else
    echo "  missing in FETCH_HEAD: $file"
  fi
done

echo "source=FETCH_HEAD remote=main status=archived" > "$ARCHIVE_DIR/RECOVERY_STATUS.txt"

echo "[4/4] Done. Live files untouched. Archive at: $ARCHIVE_DIR"
