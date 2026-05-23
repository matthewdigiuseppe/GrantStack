---
name: feasibility-audit
description: Internal-consistency audit across the whole proposal — do the objectives, work packages, timeline, team, and budget actually line up, and do milestones and deliverables match. Catches the contradictions a panel pounces on. Writes .grantstack/audits/<date>-feasibility.md. Analog to MStack's /results-audit.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Grep
  - Glob
  - Bash(date *)
---

# /grantstack:feasibility-audit

**Stage:** stress-test
**Voice:** staff project auditor (skeptical, numerate, pedantic on purpose)

## When to invoke

Before submission, after the design and budget are drafted. Where `/call-spec audit` checks the proposal against the *funder's rules*, this checks the proposal against *itself*. Internal contradictions — a budget that funds five people for a four-person plan, a milestone that lands after the WP that depends on it — are catnip for a panel and cheap to fix before they see them.

## Procedure

1. **Load everything quantitative and structural.** `proposal/sections/objectives.tex`, `workpackages.tex`, `feasibility.tex`, `budget/budget.md`, `.grantstack/team-plan.md`, `.grantstack/risk-register.md`, `.grantstack/wp-plan.md`, `.grantstack/config.yaml` (duration, amount).

2. **Run the consistency checks:**
   - **Objective ↔ WP coverage.** Every objective has at least one WP; every WP serves an objective. No orphans.
   - **Timeline closes.** WP start/end fit within `duration_months`; no WP starts before its dependency ends; the critical path fits the term with visible slack.
   - **Team ↔ WP load.** No person exceeds 1.0 FTE across concurrent WPs; recruitment lead times are allowed; PhD arcs are coherent.
   - **Budget ↔ team ↔ WP.** Personnel costs match the FTE plan; every budget line maps to a WP; total ≤ ceiling and ≤ `config.amount`.
   - **Milestones verifiable and ordered.** Each milestone is checkable, and decision points from the risk register appear in the timeline before the spend they gate.
   - **Risk ↔ fallback ↔ timeline.** Every high-risk objective has a fallback that has a slot in the plan and the budget.
   - **Numbers agree across sections.** The headcount, budget total, duration, and objective count are the same wherever they appear.

3. **Classify findings:** **Contradiction** (two parts of the proposal disagree — must fix), **Gap** (something required by the plan is unfunded/unstaffed/unscheduled), **Soft spot** (defensible but a panel will probe). Cite the file and line for each.

4. **Write `.grantstack/audits/<YYYY-MM-DD>-feasibility.md`** with the checklist results and the classified findings, contradictions first.

## Outputs

- `.grantstack/audits/<date>-feasibility.md`.
- Summary block: count of contradictions / gaps / soft spots, with every contradiction listed explicitly.

## Anti-patterns to refuse

- **Passing a proposal with a number that disagrees with itself.** A budget total that differs between the table and the text is a credibility hit; flag every instance.
- **Hand-waving "looks feasible."** Show the check: which WP, which month, which euro.
- **Confusing this with call compliance.** Page limits and fonts are `/call-spec`'s job; this is internal logic.

## When to call other skills

- Before: `/budget`, `/workpackage`, `/team-resources` should be drafted.
- Pair with: `/call-spec audit` (external rules) for full pre-submission coverage.
- After fixes: `/panel-mock expert` to confirm the feasibility now reads as solid.
