# ML101 version snapshots

This folder stores archived ML101 app snapshots to avoid overwriting the live top-level files.

## Included snapshots
- `v0.1.6` (recovered from commit `44fbee3`):
  - `ML101.html`
  - `ml101-explainer.js`
  - `VERSION_HISTORY.md`

Use these files only for recovery/reference unless explicitly promoted.


## Maintenance helpers
- `archive_ml101_version.sh <version>`: archives current root `ML101.html`, `ml101-explainer.js`, and `VERSION_HISTORY.md` into `ML101_versions/<version>/`.
- `verify_or_recreate_v0.1.6.sh`: verifies `v0.1.6` snapshot files exist and recreates them from current root files if missing.

## Smart-sync guidance
See `smart_sync_notes.md` for a cautious fetch/archive workflow that avoids touching live top-level version files until snapshots are secured.

