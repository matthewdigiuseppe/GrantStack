---
name: big-idea
description: Forcing-question interrogation of the central ground-breaking idea — what the breakthrough is, why now, why you — before committing to a proposal. Use after /grant-fit, at the start of a project. Analog to MStack's /research-question, raised to grant ambition.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(date *)
---

# /grantstack:big-idea

**Stage:** frame
**Voice:** advisor (the panel chair who will read your synopsis first)

## When to invoke

You are eligible (via `/grant-fit`) and have a candidate idea. Before you build a proposal around it, this skill forces the questions that, if dodged now, become the reviewer comments that sink the grant.

Big grants are not funded for being correct or useful. They are funded for being *ground-breaking and feasible at once*. This skill pressures the first half; `/risk-register` and `/feasibility-audit` pressure the second.

## Procedure

Read `.grantstack/config.yaml` and any `.grantstack/grant-fit.md`. Ask each question, one at a time. After all six, write `.grantstack/big-idea.md` with a verdict and a single drafted breakthrough sentence.

### The six questions

1. **The breakthrough, one sentence, no clauses.** "What does the field believe or cannot do today, that your project overturns or makes possible?" — Push until it is a single declarative sentence a smart non-specialist could repeat. "Contributes to our understanding of X" fails. This sentence becomes `project.one_sentence_breakthrough` in config.

2. **Why it's ground-breaking, not incremental.** "Name the specific assumption, barrier, or boundary you break." — A panel of generalists must feel the ground move. If the honest answer is "no one has done exactly this combination", that is incremental. Press for the conceptual or methodological leap.

3. **Why now.** "What makes this possible or urgent now and not five years ago — a new method, dataset, instrument, theory, or moment?" — Grants reward timeliness. "Now" should have a concrete enabler.

4. **Why you.** "What do you uniquely bring that makes you the person to do this — and can the track record evidence it?" — The person and the project are scored together. If anyone could do it, the panel asks why fund *you*.

5. **The high-gain payoff.** "If it works, what changes in the field? If it half-works, is the partial result still worth funding?" — Strong proposals win even on partial success. Name the floor, not just the ceiling.

6. **The killer objection.** "What will the most skeptical in-field referee say to kill this — and is your answer real or hand-waving?" — If you can't name the objection, you haven't found it yet; the referee will.

### Verdict

Write to `.grantstack/big-idea.md`:

- **Fundable ambition** — All six have substantive answers; the breakthrough sentence lands. Proceed to `/state-of-art`.
- **Promising but unframed** — The idea is real but the breakthrough is buried in incrementalism or the "why now/why you" is thin. Proceed to `/idea-shotgun` to find sharper framings, then re-run.
- **Not yet a grant** — Two or more answers are vague. Recommend either deferring, or `/scope-challenge` if the problem is that it's three ideas wearing one coat.

The verdict is opinionated by design.

## Outputs

- `.grantstack/big-idea.md` — questions, answers, verdict, and the drafted one-sentence breakthrough.
- Write the breakthrough sentence into `.grantstack/config.yaml` → `project.one_sentence_breakthrough` (ask before overwriting a non-empty value).
- Summary block with verdict and next step.

## Anti-patterns to refuse

- **Accepting "novel combination" as ground-breaking.** Combination is incremental unless the combination itself breaks an assumption.
- **Letting the breakthrough sentence carry clauses.** Clauses hide hedging. One claim.
- **Skipping "why you".** The person is half the score.

## When to call other skills

- After **Fundable ambition**: `/state-of-art`.
- After **Promising but unframed**: `/idea-shotgun`, then re-run.
- After **Not yet a grant**: `/scope-challenge`.
