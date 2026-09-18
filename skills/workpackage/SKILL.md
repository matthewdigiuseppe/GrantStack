---
name: workpackage
description: Designs the work-package structure — WPs, tasks, leads, milestones, deliverables, dependencies and a Gantt sketch — mapped to the objectives and fitted to the funded term, then writes proposal/sections/workpackages.tex. Use after the objectives and risk register are set, or when the user needs to show a panel the vision is executable by a real team in real time.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:workpackage

**Stage:** design · **Voice:** project architect

Work packages are how a panel checks the vision is executable, and the backbone the budget and timeline hang on. Coherent, and the rest aligns; muddled, and feasibility scores collapse.

## Procedure

1. **Load** `proposal/sections/objectives.tex`, `.grantstack/risk-register.md`, `.grantstack/config.yaml` (`budget.duration_months`), the work-package bar in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`, and the timeline traps in `${CLAUDE_PLUGIN_ROOT}/references/feasibility-catalog.md`.
2. **Define the work packages.** Usually 3-5. Each one: maps to one or more objectives (every objective covered, no orphan WPs); has an aim, a lead (PI / postdoc / PhD), and tasks; produces named **deliverables** and **milestones** (a milestone is a verifiable checkpoint — often a go/no-go decision point from the risk register); and states its **dependencies**.
3. **Sequence and critical path.** Lay the WPs across months 1-N. Identify the critical path and the parallelism. Front-load de-risking work; do not let everything depend on one early result. Allow recruitment lead time before any WP a new hire runs.
4. **Build a Gantt sketch** — a month-by-WP table showing start, end, and milestone markers — so the panel sees the term is realistic at a glance.
5. **Check before saving:** every objective appears in at least one WP's aim and every WP serves at least one objective; every WP has at least one milestone and one deliverable, each with a month; no WP starts before its dependency ends; the critical path fits `budget.duration_months` with visible slack; the boldest objective's fallback has a timeline slot; person-months here will match the team plan `/grantstack:team-resources` builds.
6. **Write `proposal/sections/workpackages.tex`** — per-WP blocks (aim, tasks, deliverables, milestones, dependencies, lead) plus the Gantt table; tables carry the load. Save the working notes (WP list, milestone register, critical path) to `.grantstack/wp-plan.md`, and set `grant.status: "designing"` in `.grantstack/config.yaml` if it still says `positioning`.

## Outputs

- `proposal/sections/workpackages.tex`.
- `.grantstack/wp-plan.md` — WP list, milestone register, critical path.
- Summary block: WP count, the critical path, and any objective not yet covered.

## Anti-patterns

- **WPs that do not map to objectives**, or objectives with no WP. The mapping must be total.
- **A milestone that is not verifiable.** "Progress on X" is not a milestone; "dataset Y assembled and validated" is.
- **A timeline with no slack.** A plan with zero buffer reads as one that has not met reality; show where the give is.
- **Everything depending on WP1.** Single points of failure are feasibility risks — parallelize or stage.

## Next

`/grantstack:team-resources` (staff the WPs), `/grantstack:budget` (cost them), then `/grantstack:feasibility-audit`.
