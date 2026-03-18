# ML Repo Dashboard

This repository contains interactive browser-based experiments focused on machine learning concepts and playful educational demos.

## Launch points
- `index.html` — repo dashboard for discovering the apps.
- `ML101.html` — interactive ML-focused playground.
- `pong_evolution.html` — evolutionary Pong simulation.
- `pong_RL/pong_RL.html` — reinforcement-learning Pong simulation.
- `pong_compare.html` — side-by-side comparison lab for the evolution and RL Pong apps.
- `pong_duel.html` — head-to-head arena where the trained evolution and RL agents can play each other directly.

## Pong apps

### `pong_evolution.html`
`pong_evolution.html` is a Pong app where the blue paddle is controlled by a small neural network, but the network is **not** trained with standard backpropagation-based reinforcement learning. Instead, it uses **neuroevolution**: a genetic algorithm evaluates a whole population of neural-network controllers, keeps the best performers, and creates the next population by mutating copies of those stronger bots.

#### What a generation means
In the neuroevolution app, one **generation** is one full population-level training cycle:
1. evaluate all bots,
2. assign fitness from how well each bot plays,
3. keep a small elite set unchanged,
4. mutate copies of those elites to form the next generation.

The charts and generation log in this app therefore summarize how the **population** is improving from one generation to the next, rather than how a single agent improves step-by-step.

### `pong_RL`
A `pong_RL` style app would represent the more standard reinforcement-learning setup: a **single agent** improves from experience over time, with training organized around **rewards** and **episodes** instead of evolutionary generations. In that style of app, the agent interacts with the environment, receives reward signals, and updates its policy or value estimates from those experiences.

That differs from neuroevolution because reinforcement learning usually trains one policy directly from reward feedback, while neuroevolution scores many candidate policies, selects the fittest ones, and searches by mutation/selection rather than gradient-based updates.

> Note: this repository currently ships `pong_evolution.html` as the dedicated Pong app. For the runnable reward/episode-based learning example already present in the repo, open `ML101.html`.

### Comparison

| Topic | `pong_evolution.html` | `pong_RL` style app |
| --- | --- | --- |
| Optimization method | Neuroevolution / genetic algorithm over neural-network weights | Reinforcement learning from experience and reward |
| Unit of progress | **Generation** | **Episode** |
| Number of agents trained | Many bots are evaluated each generation | Usually one learning agent is trained over many episodes |
| What charts / metrics mean | Population metrics such as best fitness, average fitness, returns, points, and conceded values per generation | Learning metrics such as episode reward, episode length, success rate, loss/value estimates, or moving averages over episodes |

### Runnable entry points
- [Open Pong Evolution](./pong_evolution.html)
- [Open Pong RL](./pong_RL/pong_RL.html)
- [Open the new Pong Compare Lab](./pong_compare.html)
- [Open the Pong Duel Lab](./pong_duel.html)
- [Open the repo dashboard](./index.html)
- [Open the reward/episode-based learning example currently in the repo (`ML101.html`)](./ML101.html)

## Supporting docs
- `VERSION_HISTORY.md` — ML101 version notes.
- `ML101_versions/README.md` — ML101 archive details.
- `version_archive_system.md` — notes on the version archive approach.
- `ML101_versions/smart_sync_notes.md` — future-development and sync notes.

## Future additions
As more apps are added, they can be listed on `index.html` with:
- an image or preview,
- version info,
- a short description,
- learning outcomes,
- and links to relevant docs or archived builds.

## Pong compare lab

`pong_compare.html` is a comparison shell that embeds both Pong apps side by side so you can inspect them in one browser view while still keeping each original app intact. It adds synchronized controls for common actions like stepping training forward, watching both policies, stopping animation, resetting both apps, and aligning playback speed / matched training cadence values. In the comparison layout it now loads both source apps in a compact responsive embed mode so the full playfield fits more reliably side by side.

The compare lab now also includes a shared side-by-side results panel that pulls headline metrics out of both embedded apps, auto-aligns the visible gameplay bands, and links vertical scrolling between the two embedded views so they stay aligned while you inspect them. The originating apps were also updated to behave more smoothly in watch mode by using delta-time-aware animation, limiting background training work per frame, and throttling heavy stats-panel rewrites.

Because the compare lab reuses the original apps inside same-origin iframes, you can still use all native controls inside each panel when you want app-specific behavior, but the top-level page makes quick A/B comparisons much easier.


## Pong duel lab

`pong_duel.html` is a dedicated arena app where the best evolved controller and the learned RL policy can train separately against their usual scripted practice opponent and then play each other directly in one shared Pong match.

It includes quick training controls for each side, a continuous joint-training toggle, duel evaluation batches, a live watch mode, and a simple duel-margin chart so you can track whether Evolution or RL is winning more often across repeated matches.
