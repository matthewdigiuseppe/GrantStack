---
name: big-idea
description: Interrogates the central ground-breaking claim with six forcing questions — the breakthrough in one sentence, why it is not incremental, why now, why you, the high-gain payoff, the killer objection — and issues a verdict plus the breakthrough sentence that every later section is built on. Use when the user has a candidate idea for a big grant and is about to start building a proposal around it.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:big-idea

**Stage:** frame · **Voice:** advisor (the panel chair who reads your synopsis first)

Big grants are not funded for being correct or useful. They are funded for being *ground-breaking and feasible at once*. This skill pressures the first half; `/grantstack:risk-register` and `/grantstack:feasibility-audit` pressure the second.

## Procedure

1. **Load** `.grantstack/config.yaml`, `.grantstack/grant-fit.md` if it exists, and the scheme's criteria in `${CLAUDE_PLUGIN_ROOT}/references/schemes.md`.
2. **Ask the six questions.** In a live session ask one at a time, offering the option to answer all six in one message; in an asynchronous context present all six together. If `grant-fit.md` or the conversation already answers one, do not re-ask.

   1. **The breakthrough, one sentence, no clauses.** "What does the field believe, or cannot do, that your project overturns or makes possible?" Push until it is a single declarative sentence a smart non-specialist could repeat from memory. "Contributes to our understanding of X" fails. Clauses hide hedging.
   2. **Why it is ground-breaking, not incremental.** "Name the specific assumption, barrier, or boundary you break." A panel of generalists must feel the ground move. "No one has done exactly this combination" is incremental unless the combination itself breaks an assumption.
   3. **Why now.** "What makes this possible or urgent now and not five years ago — a new method, dataset, instrument, theory, or moment?" "Now" needs a concrete enabler.
   4. **Why you.** "What do you uniquely bring, and can the track record evidence it?" The person and the project are scored together; if anyone could do it, the panel asks why fund *you*.
   5. **The high-gain payoff.** "If it works, what changes in the field? If it half-works, is the partial result still worth funding?" Name the floor, not just the ceiling.
   6. **The killer objection.** "What will the most skeptical in-field referee say to kill this — and is your answer real or hand-waving?" If you cannot name the objection, you have not found it yet; the referee will.

3. **Write** `.grantstack/big-idea.md` — questions, answers, the date from `date +%F`, the verdict, and the drafted breakthrough sentence. Write it even when answers are partial, marking what is open.

   **Verdict**, the first line of the file:
   - **Fundable ambition** — all six have substantive answers and the breakthrough sentence lands.
   - **Promising but unframed** — the idea is real but the breakthrough is buried, or the why-now / why-you is thin.
   - **Not yet a grant** — two or more answers are vague.

   Opinionated by design.

4. **Stamp the sentence.** Set `project.one_sentence_breakthrough` in `.grantstack/config.yaml`, editing the field in place; ask before overwriting a non-empty value. Append the framing decision to `decisions:` as `- "<date>: framing the breakthrough as <X>, not <Y>."`

## Outputs

- `.grantstack/big-idea.md` — questions, answers, verdict, breakthrough sentence.
- `project.one_sentence_breakthrough` and a `decisions:` entry in `.grantstack/config.yaml`.
- Summary block: verdict and the breakthrough sentence as it now stands.

## Anti-patterns

- **Accepting "novel combination" as ground-breaking.** Combination is incremental unless the combination itself breaks an assumption.
- **Letting the breakthrough sentence carry clauses.** One claim.
- **Skipping "why you".** The person is half the score.

## Next

**Fundable ambition** → `/grantstack:state-of-art`. **Promising but unframed** → `/grantstack:idea-shotgun`, then re-run. **Not yet a grant** → `/grantstack:scope-challenge`.
