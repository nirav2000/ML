# ML101: Browser Q-Learning Gridworld (No Frameworks)

This project is a single-file style reinforcement learning demo for learning ML/RL fundamentals quickly in plain JavaScript.

## Files

- `ML101.html` — UI + environment + Q-learning loop.
- `ml101-explainer.js` — right-side explanation panel and live math update view.

## What it demonstrates

- State, action, reward, policy.
- Exploration vs exploitation (`epsilon`-greedy).
- Tabular Q-learning updates over episodes.
- Live visualization of both behavior and **numeric Q-update math** per step.

## Controls

- **Train 100 Episodes / Train 1000 Episodes**: batch training.
- **Step Training Move**: perform exactly one learning update (great for slow/manual learning).
- **Run Learned Policy**: run greedy policy from start.
- **Reset Q-Table**: reset all learned values.
- **Stop**: interrupt current async run.
- **Show learning while training**: animate updates instead of fast background training.
- **Speed**: controls animation delay (intentionally supports very slow playback).

## Math in the UI

The right-side panel includes:

1. Q-learning equation and term-by-term interpretation.
2. A worked numeric example.
3. A **live last-update block** showing:
   - current state/action/reward
   - old Q value
   - max next-state Q
   - target
   - TD error
   - new Q value

So you can map each visual movement directly to the weight update in the Q-table.

## Run locally

```bash
python3 -m http.server 8000
```

Then open:

- `http://127.0.0.1:8000/ML101.html`

## Suggested learning flow

1. Click **Step Training Move** repeatedly and watch the live math panel.
2. Enable **Show learning while training** and run **Train 100 Episodes** at slow speed.
3. Run **Run Learned Policy** and compare behavior before/after training.
