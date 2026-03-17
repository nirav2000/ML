# Version Archive System (Reusable Guide)

This guide defines how each single-file app (for example `MLGA101.html` or `pong_evolution.html`) should support archived versions while always loading one canonical history JSON from the repository root.

## Goals
- Keep one authoritative history file per app at repo root: `<app>.versions.json`.
- Let any loaded version (current page or archived page) navigate to any other version.
- Prevent stale history with cache-busting + `cache: 'no-store'`.

## Directory pattern
- Current app: `<app>.html`
- History file: `<app>.versions.json`
- Archived files: `versions/<version>/<app>.html`

## History file contract
Each `versions[]` entry should include:
- `version`
- `label`
- `appFile` (repo-root relative path, e.g. `versions/1.1.0/pong_evolution.html`)
- `changes` (string array)
- `config` (optional)

## Required runtime helpers in every app file
- `getRootPathPrefix()`
- `getRootUrl()`
- `withBust(url)`
- `getCurrentAppFile()`

These helpers ensure correct navigation whether the app is loaded at repo root or from `versions/...`.

## Fetch rule
Always fetch the history file from root using:

```js
fetch(withBust(`${getRootUrl()}<app>.versions.json`), { cache: 'no-store' })
```

## Switch behavior
1. Read `entry.appFile` from the history JSON.
2. If it differs from `getCurrentAppFile()`, navigate to it with `withBust(...)`.
3. If it is the same file, stay in-place (or apply in-page config updates).

## Applied to Pong Evolution
`pong_evolution.html` and archived files under `versions/` now follow this system:
- root history source: `pong_evolution.versions.json`
- root and archived files share the same navigation helper logic.
