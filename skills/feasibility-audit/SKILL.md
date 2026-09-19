---
name: feasibility-audit
description: Audits the proposal against itself — objectives against work packages, timeline against duration, team against person-months, budget against both — and reports every contradiction with the two sides quoted. Use before submission once the design and budget are drafted, or when the user wants the internal-consistency check a panel will run for free.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash(date *)
---

# /grantstack:feasibility-audit

**Stage:** stress-test · **Voice:** staff project auditor — skeptical, numerate, pedantic on purpose

Where `/grantstack:call-spec audit` checks the proposal against the *funder's rules*, this checks it against *itself*. A budget that funds five people for a four-person plan, a milestone that lands after the WP depending on it — these are catnip for a panel, free to find, and cheap to fix beforehand.

## Procedure

1. **Load everything quantitative and structural:** `proposal/sections/objectives.tex`, `workpackages.tex`, `feasibility.tex`, `budget/budget.md`, `.grantstack/team-plan.md`, `.grantstack/risk-register.md`, `.grantstack/wp-plan.md`, `.grantstack/config.yaml` (duration, amount), and the whole of `${CLAUDE_PLUGIN_ROOT}/references/feasibility-catalog.md`, which is the check list this skill runs.
2. **Compute the three arithmetic checks first**, because they are the ones that either close or do not: total person-months in the WP table against the team plan against FTE × months in the budget; the budget column against its stated total and against the ceiling; the critical path against `budget.duration_months`.
3. **Run the consistency checks** from the catalog: objective ↔ WP coverage with no orphans either way; the timeline closing, with dependencies ordered and recruitment lead time allowed; team load with nobody over 1.0 FTE across concurrent WPs; every budget line mapping to a WP; milestones verifiable and ordered before the spend they gate; every high-risk objective having a fallback with a slot in the plan and the budget; and the headline numbers agreeing wherever they appear.
4. **Classify every finding** as a **Contradiction** (two parts of the proposal disagree — must fix), a **Gap** (something the plan requires that is unfunded, unstaffed, or unscheduled), or a **Soft spot** (defensible, but a panel will probe). Quote **both sides** of each contradiction with the file each came from; a contradiction stated in the abstract is not actionable, because the applicant cannot see which number to change.
5. **Check your own recommendations against your findings** before saving: a fix you propose must not create a contradiction elsewhere in the table — moving a WP later cannot push the critical path past the duration you just checked.
6. **Write `.grantstack/audits/<YYYY-MM-DD>-feasibility.md`** (date from `date +%F`), opening with the verdict line, then the checklist results, then the findings with contradictions first.

   **Verdict:** **Closes** (no contradictions), **Closes with gaps** (only minor or cosmetic ones), or **Does not close — N contradictions**. Do not soften it.

   Set `grant.status: "review"` in `.grantstack/config.yaml` if it still says `writing`.

## Outputs

- `.grantstack/audits/<date>-feasibility.md`.
- Summary block: the counts of contradictions, gaps, and soft spots, with every contradiction listed explicitly.

## Anti-patterns

- **Passing a proposal with a number that disagrees with itself.** A budget total that differs between the table and the text is a credibility hit; flag every instance.
- **Hand-waving "looks feasible".** Show the check: which WP, which month, which euro.
- **Confusing this with call compliance.** Page limits and fonts are `/grantstack:call-spec`'s job; this is internal logic.

## Next

Pair with `/grantstack:call-spec audit` for full pre-submission coverage; after fixes, `/grantstack:panel-mock expert` to confirm the feasibility now reads as solid.
