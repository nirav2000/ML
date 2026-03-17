# Smart sync notes for ML101

This repository now treats top-level `ML101.html`, `ml101-explainer.js`, and `VERSION_HISTORY.md` as **live** files.

To avoid accidental overwrite loops when debugging:

1. Fetch remote main first.
2. Verify archived snapshot presence with:
   - `bash ML101_versions/verify_or_recreate_v0.1.6.sh`
3. If you need to preserve a working state, archive it first:
   - `bash ML101_versions/archive_ml101_version.sh vX.Y.Z`
4. Only then edit live top-level files.

## Verification status
- `v0.1.6` snapshot retrieval verified in this workspace and contains:
  - `ML101.html`
  - `ml101-explainer.js`
  - `VERSION_HISTORY.md`

5. To snapshot remote safely without changing live files:
   - `bash ML101_versions/safe_fetch_and_archive.sh <archive_name>`

This archives `ML101.html`, `ml101-explainer.js`, and `VERSION_HISTORY.md` from `FETCH_HEAD` into `ML101_versions/` for comparison or recovery.
