---
name: interview-prep
description: Prepares the committee or step-2 interview — a timed spoken pitch, a slide skeleton, and a drilled question bank built from the mock reviews, the risk register and the track record, with the killer question rehearsed. Use when the user has been invited to interview; for ERC Consolidator and NWO Vici this is where the funding is actually decided.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(date *)
---

# /grantstack:interview-prep

**Stage:** defend · **Voice:** interview coach who has sat on the panel

The proposal is fixed; the defence decides it. Panels fund people who are clear, confident, and unflappable under challenge, and sink people who get defensive or lost.

What the interview *is* depends on the scheme, and getting this wrong wastes the preparation. At **ERC** (StG and CoG; AdG has no interview) the applicant has not seen the referee comments — they arrive with the final decision — so the interview is a pitch and a defence of the proposal as written, and the hard questions must be anticipated from the proposal's own weak points. At **NWO** the referee reports and the applicant's rebuttal are already on the table, so the contested points are known and the committee will return to them. Check `${CLAUDE_PLUGIN_ROOT}/references/schemes.md` and the format in `.grantstack/call-spec.md` before building anything.

## Procedure

1. **Load** every file in `proposal/sections/`, `.grantstack/big-idea.md`, `.grantstack/risk-register.md`, the newest `.grantstack/groundbreaking-test-*.md`, `.grantstack/review-cache/panel-mock-*`, and — where the scheme has them — `reviews/received/*` and `reviews/rebuttal/*`. The hardest questions are already in those documents.
2. **Confirm the format** from `.grantstack/call-spec.md`, or ask: length, whether there is a presentation, slide and time limits, panel composition (generalist or mixed). Calibrate everything to it.
3. **Build the pitch** — a spoken opening to the call's limit, typically five minutes: the breakthrough in one sentence, why now, why you, the plan in three beats, the high-gain payoff. Written to be *said*, not read: short sentences, one idea per breath. Provide a timed version.
4. **Build the slide skeleton**, if slides are allowed: title and acronym, the breakthrough, the gap, one visual of objectives and work packages, feasibility and risk, the team, the payoff. One idea per slide, no wall of text.
5. **Drill the question bank**, drafting from `${CLAUDE_PLUGIN_ROOT}/skills/interview-prep/assets/qbank-template.md` and grouping:
   - **Ambition** — "What is genuinely new here?" "Isn't this incremental?" Answer from the groundbreaking-test discontinuity.
   - **Feasibility** — "What if your central assumption is wrong?" "Why five years and not ten?" Answer from the risk-register fallbacks.
   - **The person** — "Why are you the one to do this?" "What is your role day to day?" Answer from the track-record through-line.
   - **The contested points** — at NWO, every point from the reports and rebuttal; at ERC, every major concern from the mock reviews, since the real comments are not available.
   - **Resources** — "Why two postdocs?" "Why this equipment?" Answer from the budget justification.
   - **The killer** — the one question the applicant most hopes not to get. Name it and rehearse the calm answer.

   Each answer is 45–90 seconds spoken, with a one-line core to fall back on if flustered.
6. **Coach the delivery.** Name the traps — rambling past the time, getting defensive, conceding the ambition under pressure, answering a different question than the one asked — and prescribe: pause, answer the question, bridge to a strength.
7. **Write** `reviews/interview/pitch.md`, `reviews/interview/slides-outline.md`, and `reviews/interview/qbank.md`. Set `grant.status: "interview"` in `.grantstack/config.yaml` if it still says `submitted` or `rebuttal`.

## Outputs

- `reviews/interview/pitch.md` — the timed spoken pitch.
- `reviews/interview/slides-outline.md` — the slide skeleton, where slides are allowed.
- `reviews/interview/qbank.md` — grouped questions with answers and fallback cores.
- Summary block: the pitch's opening sentence, the three hardest questions, and the killer question.

## Anti-patterns

- **A pitch written to be read, not spoken.** Rewrite for the ear.
- **Skipping the killer question** because it is uncomfortable. That is the one to drill most.
- **Answers that concede the ambition under pressure.** Defend with the fallback, not by shrinking the project.
- **Slides that are the proposal in miniature.** One idea per slide; the panel listens to you, not the screen.

## Next

After the decision: `/grantstack:retro`, and `/grantstack:resubmit` if it is a rejection worth fighting.
