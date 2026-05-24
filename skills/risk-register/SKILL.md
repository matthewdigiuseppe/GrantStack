---
name: risk-register
description: Builds the high-risk/high-gain risk register — for each bold objective, the risk, its likelihood and impact, the mitigation, and the fallback that still yields a fundable result. Use after /objectives. This is what turns "reckless" into "bold but feasible" in a panel's eyes.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:risk-register

**Stage:** position
**Voice:** methodologist / project-risk officer

## When to invoke

After `/objectives`. ERC and NWO explicitly want high-risk/high-gain ambition — *and* they reject proposals that look reckless. The difference between bold and reckless is a credible mitigation-and-fallback plan. A risk register also pre-empts the "what if the central assumption fails?" referee comment by answering it first.

## Procedure

1. **Load.** `proposal/sections/objectives.tex`, `.grantstack/config.yaml`, `.grantstack/risk` notes if any.

2. **Enumerate risks per objective.** For each objective (especially the `bold` / `high-risk` ones), identify the genuine risks across categories:
   - **Scientific** — the central hypothesis or assumption may be wrong.
   - **Technical / methodological** — the method or instrument may not deliver at the needed resolution/scale.
   - **Data / access** — site, cohort, archive, or sample may not be obtainable.
   - **Personnel / timing** — recruitment, dependencies, the critical path.

3. **Score each risk** simply: likelihood (L/M/H) × impact on the objective (L/M/H). Surface the few that are Medium-High on both — those are the ones a referee will probe.

4. **For each material risk, write three things:**
   - **Mitigation** — what reduces the likelihood up front (pilot, redundancy, staged go/no-go).
   - **Fallback** — if it happens anyway, the alternative path that still produces a meaningful result. This is the heart: every high-risk objective needs a fallback that is itself worth funding.
   - **Decision point** — when in the timeline you'll know, and what triggers the switch to the fallback.

5. **State the high-gain explicitly.** For each bold bet, pair the risk with the payoff: this is what makes the risk worth taking. A register that lists only downside reads as a project that should be safer.

6. **Write outputs.** A risk table to `.grantstack/risk-register.md`, and a tightened prose version into `proposal/sections/feasibility.tex` (creating or appending — coordinate with `/methodology` and `/workpackage`, which also feed feasibility).

## Outputs

- `.grantstack/risk-register.md` — full table: objective, risk, L×I, mitigation, fallback, decision point, paired high-gain.
- `proposal/sections/feasibility.tex` — prose risk-and-mitigation paragraph(s).
- Summary block: the top 3 risks a referee will probe and whether each has a credible fallback.

## Anti-patterns to refuse

- **Risk theatre.** Listing trivial risks ("a postdoc may be hard to hire") to look thorough while dodging the real scientific bet. Name the real one.
- **Fallbacks that abandon the ambition.** A fallback that reduces to an incremental project tells the panel the bold version was unfeasible. Fallbacks must still be worth funding.
- **Mitigation without a decision point.** "We will monitor" is not a plan. Say when you'll know and what you'll do.

## When to call other skills

- Before: `/objectives` if objectives aren't on file.
- After: `/workpackage` (decision points become milestones) and later `/feasibility-audit`.
