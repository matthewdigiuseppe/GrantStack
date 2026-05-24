---
name: interview-prep
description: Prepares the step-2 / committee interview — the elevator pitch, the slide skeleton, and a drilled bank of likely and killer questions with crisp answers. ERC CoG and NWO Vici both decide at interview; this is where funding is won or lost. Writes reviews/interview/ prep materials.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
  - Glob
  - Grep
---

# /grantstack:interview-prep

**Stage:** submit/defend
**Voice:** interview coach who has sat on the panel

## When to invoke

You've been invited to interview (ERC Consolidator step 2; NWO Vici committee). At this stage the proposal is fixed and the *defense* decides it. Panels fund people who are clear, confident, and unflappable under challenge — and sink people who get defensive or lost. Prepare deliberately.

## Procedure

1. **Load.** All `proposal/sections/*`, `.grantstack/big-idea.md`, `.grantstack/risk-register.md`, the referee reports and `reviews/rebuttal/*`, and prior `.grantstack/review-cache/panel-mock-*`. The hardest interview questions are already in those documents.

2. **Confirm the format** from `.grantstack/call-spec.md` or ask: length, whether there's a presentation, slide/time limits, panel composition (generalist vs. mixed). Calibrate everything to this.

3. **Build the pitch.** A tight spoken opening (typically 5 minutes or the call's limit): the breakthrough in one sentence, why now, why you, the plan in three beats, the high-gain payoff. Written to be *said*, not read — short sentences, one idea per breath. Provide a timed version.

4. **Build the slide skeleton** (if slides are allowed): title/acronym, the breakthrough, the gap, the objectives-and-WP picture (one visual), feasibility/risk, the team, the payoff. One idea per slide; no wall of text.

5. **Drill the question bank.** Generate and answer, grouped:
   - **Ambition** — "What's genuinely new here?" "Isn't this incremental?" Use the `/groundbreaking-test` discontinuity.
   - **Feasibility** — "What if your central assumption is wrong?" "Why will this take five years not ten?" Use the risk-register fallbacks.
   - **The person** — "Why are you the one to do this?" "What's your role day-to-day?" Use the track-record through-line.
   - **The referee's points** — every contested point from the reports becomes a question; answer from the rebuttal.
   - **Resources** — "Why two postdocs?" "Why this equipment?" Use the budget justification.
   - **The killer** — the one question you most hope they don't ask. Name it and rehearse the calm answer.
   For each: a crisp 30-60 second answer, plus the one-line core to fall back on if flustered.

6. **Coach the delivery.** Note the traps: rambling past the time, getting defensive, conceding the ambition under pressure, answering a different question than asked. Prescribe: pause, answer the question, bridge to a strength.

7. **Write** `reviews/interview/pitch.md`, `reviews/interview/slides-outline.md`, and `reviews/interview/qbank.md`.

## Outputs

- `reviews/interview/pitch.md` — timed spoken pitch.
- `reviews/interview/slides-outline.md` — slide skeleton (if applicable).
- `reviews/interview/qbank.md` — grouped questions with answers and fallback cores.
- Summary block: the pitch's one-sentence open, the three hardest questions, and the killer question.

## Anti-patterns to refuse

- **A pitch written to be read, not spoken.** Rewrite for the ear.
- **Skipping the killer question** because it's uncomfortable. That's the one to drill most.
- **Answers that concede the ambition under pressure.** Defend with the fallback, not by shrinking the project.
- **Slides that are the proposal in miniature.** One idea per slide; the panel listens to you, not the screen.

## When to call other skills

- Before: `/panel-mock` and `/rebuttal` (their outputs are the question bank).
- After (if rejected): `/retro` then `/resubmit`.
