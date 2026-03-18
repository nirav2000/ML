# Dashboard Brand Theme

This folder packages the look and feel of the repository dashboard so it can be reused in new apps such as ML101, Pong Evolution, Pong RL, and future projects.

## Files
- `theme.css` — shared design tokens, typography, panel styling, and page shell primitives.
- `components.css` — reusable buttons, cards, pills, and small utility classes.
- `app-shell.html` — starter HTML shell showing how to apply the theme to a new app.
- `preview_manifest.json` — source data for generated preview images.
- `generate_previews.py` — creates SVG preview assets in `previews/`.
- `previews/*.svg` — generated preview art for dashboard cards and future reuse.

## How to reuse this brand theme
1. Link `theme.css` and `components.css` from a new app.
2. Use the `brand-app`, `brand-shell`, and `brand-panel` classes for page layout.
3. Use `brand-button`, `brand-button-secondary`, `brand-card`, and `brand-pill` for controls/components.
4. Copy `app-shell.html` as a starting point if you want a new app page to match the dashboard style quickly.

## Preview workflow
- Add a new entry to `preview_manifest.json`.
- Run `python dashboard_brand/generate_previews.py`.
- The generated SVG can be used in `index.html` or inside the app itself.

## Automation
The active GitHub Actions workflow now lives at `.github/workflows/generate-dashboard-previews.yml`, and the original example copy remains at `dashboard_brand/workflow_examples/generate-dashboard-previews.yml.example`.
The workflow regenerates preview SVGs whenever `index.html` or the preview manifest/script changes.

## Notes
- The generated preview art is intentionally theme-consistent and now uses bespoke animated SVG scenes rather than literal browser screenshots.
- If you want real screenshots later, this workflow can be extended with Playwright to capture app pages automatically during CI.
