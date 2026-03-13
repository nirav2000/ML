export const learningSummary = {
  title: "What this demo is showing",
  bullets: [
    "The agent starts with no idea which move is good.",
    "Each action gives a reward signal (small penalty per step, bigger penalty for traps, positive reward for goal).",
    "A Q-table acts like adjustable weights: one value per (state, action).",
    "With exploration (epsilon), the agent still tries random moves to discover better paths.",
    "Over episodes, the best-action arrows stabilize into a short, safe route to the goal."
  ],
  meaning:
    "This is reinforcement learning in tabular form: behavior improves from reward feedback without labeled correct actions."
};

let lastUpdateEl = null;

export function renderLearningSummary(targetEl) {
  if (!targetEl) return;

  targetEl.innerHTML = `
    <h3>${learningSummary.title}</h3>
    <ul>
      ${learningSummary.bullets.map((item) => `<li>${item}</li>`).join("")}
    </ul>
    <p><strong>Why it matters:</strong> ${learningSummary.meaning}</p>
  `;
}

export function renderMathWalkthrough(targetEl) {
  if (!targetEl) return;

  const section = document.createElement("section");
  section.innerHTML = `
    <h3>Math view (what changes each step)</h3>
    <p><strong>Update rule:</strong> Q(s, a) = Q(s, a) + alpha × (reward + gamma × max Q(s′, a′) − Q(s, a))</p>
    <p>Interpretation:</p>
    <ul>
      <li><strong>Q(s, a)</strong> is the current weight for action <code>a</code> in state <code>s</code>.</li>
      <li><strong>reward + gamma × max Q(s′, a′)</strong> is the target estimate.</li>
      <li><strong>TD error</strong> = target − old Q, and the new Q moves a fraction <code>alpha</code> toward the target.</li>
      <li>Terminal state: future term is 0, so target = reward only.</li>
    </ul>
    <p><strong>Worked example:</strong> if oldQ = 0.20, reward = -0.04, maxNextQ = 0.60, alpha = 0.10, gamma = 0.95, then target = -0.04 + 0.95×0.60 = 0.53, TD error = 0.33, newQ = 0.20 + 0.10×0.33 = 0.233.</p>
  `;

  targetEl.appendChild(section);
}

export function renderLastUpdatePanel(targetEl) {
  if (!targetEl) return;

  const section = document.createElement("section");
  section.id = "lastUpdateSection";
  section.innerHTML = `
    <h3>Last Q-update (live)</h3>
    <div id="lastUpdate"></div>
  `;

  targetEl.appendChild(section);
  lastUpdateEl = section.querySelector("#lastUpdate");
}

export function updateLastUpdatePanel(data) {
  if (!lastUpdateEl) return;

  if (!data) {
    lastUpdateEl.textContent = "No updates yet. Start training or click Step Training Move.";
    return;
  }

  lastUpdateEl.textContent = [
    `state s      = (${data.state.x}, ${data.state.y})`,
    `action a     = ${data.action}`,
    `next state s'= (${data.nextState.x}, ${data.nextState.y})`,
    `reward r     = ${data.reward.toFixed(3)}`,
    `done         = ${String(data.done)}`,
    "",
    `old Q(s,a)   = ${data.oldQ.toFixed(6)}`,
    `max Q(s',.)  = ${data.nextBest.toFixed(6)}`,
    `target       = r + gamma*maxQ = ${data.target.toFixed(6)}`,
    `td error     = target - oldQ = ${data.tdError.toFixed(6)}`,
    `new Q(s,a)   = oldQ + alpha*td = ${data.newQ.toFixed(6)}`,
    "",
    `alpha=${data.alpha}, gamma=${data.gamma}`
  ].join("\n");
}
