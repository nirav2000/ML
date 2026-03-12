export const learningSummary = {
  title: "What this demo is showing",
  bullets: [
    "The agent starts with no idea which move is good.",
    "Each action gives a reward signal (small penalty per step, bigger penalty for traps, positive reward for goal).",
    "Q-values estimate how useful each action is in each cell.",
    "With exploration (epsilon), the agent still tries random moves to discover better paths.",
    "Over episodes, the best-action arrows stabilize into a short, safe route to the goal."
  ],
  meaning:
    "This is reinforcement learning in its simplest form: behavior improves from reward feedback without labeled correct answers."
};

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

export function renderUpdateRule(targetEl) {
  if (!targetEl) return;

  const note = document.createElement("p");
  note.innerHTML =
    "<strong>Q-learning update:</strong> Q(s, a) = Q(s, a) + alpha × (reward + gamma × max Q(s′, a′) − Q(s, a)). In terminal states, future value is treated as 0.";
  targetEl.appendChild(note);
}
