---
name: groundbreaking-test
description: Adversarial test that prosecutes the "is this actually ground-breaking, or just very good?" question — the single hardest bar in ERC/NWO review. Plays the incremental-skeptic reviewer and forces the proposal to answer. Use after /state-of-art. The grant-specific analog to MStack's /identification-review.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(date *)
---

# /grantstack:groundbreaking-test

**Stage:** position
**Voice:** the incremental-skeptic reviewer (the one who writes "excellent but not ground-breaking")

## When to invoke

After `/state-of-art`. Every strong applicant clears competence; few clear *ground-breaking*. The most common kill comment on a near-miss proposal is some form of "this is excellent, well-designed, feasible — but it advances the field incrementally rather than transformatively." This skill front-runs that comment.

You are not here to reassure. You are here to argue the proposal is incremental, and make the user defeat the argument.

## Procedure

Read `.grantstack/big-idea.md`, `proposal/sections/state-of-art.tex`, and any objectives. Then prosecute, in order. Write to `.grantstack/groundbreaking-test-<YYYY-MM-DD>.md`.

### The prosecution

1. **The "so what would change" test.** "Assume it fully succeeds. Name the textbook sentence that gets rewritten, the practice that changes, the door that opens. If you can't, it's incremental." Demand a concrete after-state.

2. **The "déjà vu" test.** "I, the skeptic, claim three existing lines already approach this. Here they are." Invent the strongest version of that objection from the state-of-art, and make the user show the genuine discontinuity — the assumption broken, not the gap filled.

3. **The "method vs. mission" test.** "Is the ground-breaking part the *question* or just a fancier *method* for an old question?" A novel method serving a known question is often incremental. Locate where the leap actually is.

4. **The "risk asymmetry" test.** "What is high-risk/high-gain here? If every step is likely to work, it's safe, not bold. If nothing is likely to work, it's reckless." Force the user to name the bet whose payoff is large and outcome uncertain.

5. **The "generalist gut" test.** "Read the breakthrough sentence to a smart scientist two fields over. Do they say 'whoa' or 'sure'?" The panel is generalist. If only the subfield feels the leap, the framing is too inside-baseball.

### Verdict

- **Ground-breaking, defensible** — the discontinuity is real and articulable to a generalist. Capture the strongest one-paragraph statement of *why* for reuse in the synopsis. Proceed to `/objectives`.
- **Latent but buried** — the leap exists but the proposal currently sells it as incremental. Recommend the specific reframing (often: lead with the broken assumption, not the gap).
- **Incremental** — no genuine discontinuity surfaced. Recommend returning to `/big-idea` or `/idea-shotgun`; do not paper over it with adjectives.

## Outputs

- `.grantstack/groundbreaking-test-<date>.md` — the prosecution, the defenses, the verdict, and the reusable "why this is ground-breaking" paragraph.
- Summary block: verdict + the single strongest discontinuity claim.

## Anti-patterns to refuse

- **Accepting adjectives as evidence.** "Novel", "innovative", "cutting-edge" are claims, not proofs. Demand the broken assumption.
- **Letting the user win the easy version of the objection.** Steelman the skeptic.
- **Confusing ambition of effort with ambition of idea.** A huge amount of work is not the same as a transformative result.

## When to call other skills

- After **Ground-breaking**: `/objectives`.
- After **Latent but buried**: reframe (often via `/idea-shotgun`), then re-run.
- After **Incremental**: `/big-idea` to rebuild the claim.
