---
name: risk-register
description: Builds the high-risk/high-gain register — per bold objective, the risk, its likelihood and impact, the mitigation, the decision point, and the fallback that still yields a fundable result — and writes .grantstack/risk-register.md. Use after the objectives are set; this is what turns "reckless" into "bold but feasible" in a panel's eyes.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Bash(date *)
---

# /grantstack:risk-register

**Stage:** position · **Voice:** project-risk officer

ERC and NWO want high-risk/high-gain ambition *and* reject proposals that look reckless. The difference is a credible mitigation-and-fallback plan, which also pre-empts the "what if the central assumption fails?" referee comment by answering it first.

## Procedure

1. **Load** `proposal/sections/objectives.tex`, `.grantstack/big-idea.md` (the killer objection is usually the first real risk), `.grantstack/config.yaml`, and the risk sections of `${CLAUDE_PLUGIN_ROOT}/references/feasibility-catalog.md` and `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`.
2. **Enumerate risks per objective**, especially the `bold` and `high-risk` ones, across categories: **scientific** (the central hypothesis or assumption may be wrong), **technical/methodological** (the method may not deliver at the needed resolution or scale), **data/access** (site, cohort, archive, or sample may not be obtainable), **personnel/timing** (recruitment, dependencies, the critical path).
3. **Score** each risk: likelihood (L/M/H) × impact on the objective (L/M/H). Surface the few that are Medium-High on both — those are what a referee probes.
4. **For each material risk write three things:**
   - **Mitigation** — what reduces the likelihood up front (pilot, redundancy, staged go/no-go).
   - **Fallback** — the alternative path that still produces a meaningful result if it happens anyway. This is the heart of the register: every high-risk objective needs a fallback that is itself worth funding.
   - **Decision point** — when in the timeline you will know, and what triggers the switch.
5. **Pair each bold bet with its payoff.** A register that lists only downside reads as a project that should have been safer.
6. **Write** `.grantstack/risk-register.md`: the verdict line, then the table — objective, risk, L×I, mitigation, fallback, decision point, paired high-gain.

   **Verdict**, the first line: **Bold and covered** (every high-risk objective has a fallback worth funding), **Covered with gaps** (name them), or **Reckless as written** (a bold objective with no fallback).

   The prose version of this register belongs in `proposal/sections/feasibility.tex`, which `/grantstack:draft-section feasibility` composes from this memo and the team plan — do not write that file here, or the two skills will overwrite each other.

## Outputs

- `.grantstack/risk-register.md` — verdict and the full table.
- Summary block: the top three risks a referee will probe, and whether each has a credible fallback.

## Anti-patterns

- **Risk theatre.** Listing trivial risks ("a postdoc may be hard to hire") to look thorough while dodging the real scientific bet. Name the real one.
- **Fallbacks that abandon the ambition.** A fallback that reduces to an incremental project tells the panel the bold version was unfeasible. Fallbacks must still be worth funding.
- **Mitigation without a decision point.** "We will monitor" is not a plan; say when you will know and what you will do.

## Next

`/grantstack:workpackage` — the decision points become milestones — and later `/grantstack:feasibility-audit`.
