# Index Dashboard Maintenance Guide

This file explains how another AI agent or app generator should update `index.html` safely and consistently.

## Source of truth
The dashboard is driven by the `appCatalog` array inside `index.html`.

If you add, remove, or update an app card, make the change in `appCatalog` first. The hero summary stats are now generated from that array automatically.

## Required fields for each app
Each app entry should include:
- `name` — display name for the card and summary stats
- `version` — current visible version badge
- `href` — primary app URL
- `artLabel` — small label shown over the preview image
- `image` — image URL or `data:image/svg+xml` preview string
- `description` — short pitch
- `expect` — short paragraph describing user expectations
- `learn` — array of learning outcomes
- `links` — array of action links with:
  - `label`
  - `href`
  - `primary` (`true` for the main launch action)

## Update checklist for AI agents
When updating `index.html`:
1. Add or modify the app object in `appCatalog`.
2. Ensure the app has a working preview image or SVG generator.
3. Ensure the main `href` opens the app.
4. Add at least one primary action and useful secondary links.
5. Confirm the `version` field is current.
6. If you add a new supporting document, add it to the resources section too.
7. Do **not** hardcode the hero app count or version-summary text; those are generated automatically.
8. Preserve the visual style unless explicitly asked to redesign it.

## Preview guidance
If no screenshot exists:
- prefer an inline SVG preview tailored to the app
- keep the visual aligned with the app theme
- avoid generic placeholders if a themed preview can be created

## Resource section guidance
The resource links section is still hand-authored. Update it when:
- a new root README/doc is added
- a new archive folder becomes important
- a roadmap, changelog, or notes file should be surfaced

## Recommended workflow for another AI
1. Inspect the existing `appCatalog` entries.
2. Add the new app using the same structure.
3. Verify hero stats still make sense after rendering.
4. Verify all linked files exist.
5. Keep the dashboard polished and consistent with the existing visual language.
