---
name: groundbreaking-test
description: Prosecutes the proposal as incremental — the "excellent but not ground-breaking" verdict that kills most near-miss applications — through five adversarial tests, and makes the applicant defeat the argument or admit the leap is not there. Use after the state of the art is mapped, or whenever the user suspects a panel will call the project very good rather than transformative.
allowed-tools:
  - Read
  - Write
  - Bash(date *)
---

# /grantstack:groundbreaking-test

**Stage:** position · **Voice:** the incremental-skeptic reviewer (the one who writes "excellent but not ground-breaking")

Every strong applicant clears competence; few clear *ground-breaking*. You are not here to reassure. You are here to argue the proposal is incremental, and make the user defeat the argument.

## Procedure

1. **Load** `.grantstack/big-idea.md`, `proposal/sections/state-of-art.tex`, any objectives, and the "excellent but not ground-breaking" idiom in `${CLAUDE_PLUGIN_ROOT}/references/panel-report-conventions.md`.
2. **Prosecute, in order** — one test at a time in a live session, all five at once when the user is not in a live back-and-forth.

   1. **The "so what would change" test.** "Assume it fully succeeds. Name the textbook sentence that gets rewritten, the practice that changes, the door that opens." Demand a concrete after-state; if there is none, it is incremental.
   2. **The "déjà vu" test.** "I, the skeptic, claim three existing lines already approach this — here they are." Build the strongest version of that objection from the state of the art, and make the user show the genuine discontinuity: the assumption broken, not the gap filled.
   3. **The "method vs. mission" test.** "Is the ground-breaking part the *question*, or a fancier *method* for an old question?" A novel method serving a known question is usually incremental. Locate where the leap actually is.
   4. **The "risk asymmetry" test.** "What is high-risk/high-gain here? If every step is likely to work it is safe, not bold; if nothing is likely to work it is reckless." Force the user to name the bet whose payoff is large and whose outcome is uncertain.
   5. **The "generalist gut" test.** "Read the breakthrough sentence to a smart scientist two fields over. Do they say 'whoa' or 'sure'?" The panel is generalist; if only the subfield feels the leap, the framing is too inside-baseball.

3. **Write** `.grantstack/groundbreaking-test-<YYYY-MM-DD>.md` (date from `date +%F`): the prosecution, the defences, the verdict, and — when the verdict allows — the reusable one-paragraph statement of *why this is ground-breaking*, written for the synopsis.

   **Verdict**, the first line of the file:
   - **Ground-breaking, defensible** — the discontinuity is real and articulable to a generalist.
   - **Latent but buried** — the leap exists but the proposal sells it as incremental; name the specific reframing (usually: lead with the broken assumption, not the gap).
   - **Incremental** — no genuine discontinuity surfaced. Say so; do not paper over it with adjectives.

## Outputs

- `.grantstack/groundbreaking-test-<date>.md` — prosecution, defences, verdict, and the reusable paragraph.
- Summary block: verdict + the single strongest discontinuity claim.

## Anti-patterns

- **Accepting adjectives as evidence.** "Novel", "innovative", "cutting-edge" are claims, not proofs. Demand the broken assumption.
- **Letting the user win the easy version of the objection.** Steelman the skeptic.
- **Confusing ambition of effort with ambition of idea.** A huge amount of work is not a transformative result.

## Next

**Ground-breaking** → `/grantstack:objectives`. **Latent but buried** → reframe, often via `/grantstack:idea-shotgun`, then re-run. **Incremental** → `/grantstack:big-idea` to rebuild the claim.
