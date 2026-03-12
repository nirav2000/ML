# ML101 App Version History

## v0.1.0
- Implemented APP_REVIEW medium-priority recommendation #4: exposed core hyperparameters in the UI (alpha, gamma, epsilon start/decay/min).
- Added validation guardrails and an explicit reset-to-defaults action for hyperparameters.
- Persisted hyperparameters in localStorage and surfaced active values in the stats line.

## v0.0.5
- Moved the **Last Q-update (live)** section to the top of the right-side panel so it appears first next to the grid.
- Added a footer app version control that opens this history when clicked.
- Added in-app loading of this markdown history via a dialog.

## v0.0.4
- Added rolling metrics (success rate, trap hits, timeouts, average steps).
- Added localStorage persistence for Q-table and training progress.
- Added `aria-live` status/metrics updates and updated README docs.

## v0.0.3
- Added step-by-step training mode and richer live learning visual feedback.
- Added right-side math explainer panel and live last-update details.

## v0.0.2
- Improved interactive controls and training visualization behaviors.

## v0.0.1
- Initial browser-based Q-learning gridworld demo.
