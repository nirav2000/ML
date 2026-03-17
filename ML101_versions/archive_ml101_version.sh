#!/usr/bin/env bash
set -euo pipefail

# Archive current ML101 files into ML101_versions/<version>
# Usage: ./ML101_versions/archive_ml101_version.sh v0.1.7

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <version> (example: v0.1.7)" >&2
  exit 1
fi

VERSION="$1"
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="$ROOT_DIR/ML101_versions/$VERSION"

mkdir -p "$TARGET_DIR"
cp "$ROOT_DIR/ML101.html" "$TARGET_DIR/ML101.html"
cp "$ROOT_DIR/ml101-explainer.js" "$TARGET_DIR/ml101-explainer.js"
cp "$ROOT_DIR/VERSION_HISTORY.md" "$TARGET_DIR/VERSION_HISTORY.md"

echo "Archived ML101 snapshot to $TARGET_DIR"
