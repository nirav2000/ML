# ML101 version snapshots

This folder stores archived ML101 app snapshots so recovery work does not overwrite the live top-level files.

## Current policy
- Keep active app files at repository root (`ML101.html`, `ml101-explainer.js`, `VERSION_HISTORY.md`).
- Place recovered or historical copies in versioned subfolders under `ML101_versions/`.
- Prefer retrieving snapshots from `origin/main` first.
- If a target snapshot cannot be retrieved from remote history, recreate it from current root files and mark that in `RECOVERY_STATUS.txt`.

## Included snapshots
- `v0.1.6/`
  - `ML101.html`
  - `ml101-explainer.js`
  - `VERSION_HISTORY.md`
  - `RECOVERY_STATUS.txt`

Use archived files for recovery/reference unless explicitly promoted.

## Maintenance helpers
- `archive_ml101_version.sh <version>`: archives current root ML101 files into `ML101_versions/<version>/`.
- `verify_or_recreate_v0.1.6.sh`: verifies `v0.1.6` snapshot files exist and recreates them if missing.
- `smart_sync_notes.md`: cautious fetch/archive workflow to avoid accidental live-file overwrites.

- `safe_fetch_and_archive.sh [archive_name]`: fetches remote main and archives target ML101 files from FETCH_HEAD without touching live top-level files.
