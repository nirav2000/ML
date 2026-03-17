# ML101 App Version History

## v0.1.6
- Added built-in startup self-check to detect missing critical UI/runtime hooks before interaction.
- Added safe event wrappers so runtime handler errors are captured and surfaced via debug tools instead of failing silently.
- Added `robustness_check.sh` to run repeatable local syntax + hook integrity checks before shipping changes.

## v0.1.3
- Added clickable version navigation inside the Version History dialog to move back and forth between releases.
- The current active app version is highlighted and marked as active.
- Added iPad-friendly debug tools (device snapshot, runtime error log, module-load test, copy report) to help diagnose browser-specific issues.
- Rolled back active app version label to `v0.1.3` to stabilize debugging scope.

## v0.1.2
- Fixed rendering order bug so the **Last Q-update (live)** panel is not overwritten by other explainer sections.
- Highlighted the live-update panel in yellow and stronger border so it is immediately visible.
- Added a move-by-move one-line trace list so each Q update can be followed step-by-step for faster learning.

## v0.1.1
- Pinned the **Last Q-update (live)** panel at the top-right explanation column so it stays visible while reading other info.
- Added sticky styling to keep live update details prominent next to the grid.

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
