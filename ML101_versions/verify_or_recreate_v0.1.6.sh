#!/usr/bin/env bash
set -euo pipefail

# Ensures ML101 v0.1.6 snapshot exists.
# If missing, recreates from current root ML101 files.

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
V_DIR="$ROOT_DIR/ML101_versions/v0.1.6"

need_recreate=0
for f in ML101.html ml101-explainer.js VERSION_HISTORY.md; do
  [[ -f "$V_DIR/$f" ]] || need_recreate=1
done

if [[ "$need_recreate" -eq 0 ]]; then
  echo "v0.1.6 snapshot already present and complete."
  exit 0
fi

mkdir -p "$V_DIR"
cp "$ROOT_DIR/ML101.html" "$V_DIR/ML101.html"
cp "$ROOT_DIR/ml101-explainer.js" "$V_DIR/ml101-explainer.js"
cp "$ROOT_DIR/VERSION_HISTORY.md" "$V_DIR/VERSION_HISTORY.md"

echo "Recreated missing v0.1.6 snapshot at $V_DIR"
