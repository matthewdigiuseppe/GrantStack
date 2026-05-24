---
name: workpackage
description: Designs the work-package structure — WPs, tasks, milestones, deliverables, dependencies, and a Gantt sketch — mapped to the objectives. Writes proposal/sections/workpackages.tex. Use after /objectives and /risk-register.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:workpackage

**Stage:** design
**Voice:** project architect

## When to invoke

After objectives and the risk register are set. Work packages are how a panel checks that the vision is executable by a real team in real time. The WP structure is also the backbone the budget and timeline hang on — get it coherent and the rest aligns; get it muddled and feasibility scores collapse.

## Procedure

1. **Load.** `proposal/sections/objectives.tex`, `.grantstack/risk-register.md`, `.grantstack/config.yaml` (duration, budget).

2. **Define work packages.** Usually 3-5. Each WP:
   - Maps to one or more objectives (every objective is covered; no orphan WPs).
   - Has a clear aim, a lead (PI / postdoc / PhD), and a set of tasks.
   - Produces named **deliverables** and **milestones** (a milestone is a verifiable checkpoint — often the go/no-go decision points from `/risk-register`).
   - States its **dependencies** on other WPs.

3. **Sequence and critical path.** Lay the WPs on the project timeline (months 1-N from `config.duration_months`). Identify the critical path and any parallelism. Front-load de-risking work; don't let everything depend on a single early result.

4. **Build a Gantt sketch.** A simple month-by-WP table (text or LaTeX) showing start/end and milestone markers. The panel should see the term is realistic at a glance.

5. **Cross-check feasibility.**
   - No WP starts before its dependency finishes.
   - Milestones land before the points where the budget commits major spend.
   - The boldest objective's fallback (from the risk register) has a timeline slot.

6. **Write `proposal/sections/workpackages.tex`.** Per-WP blocks (aim, tasks, deliverables, milestones, dependencies, lead) plus the Gantt table. Keep prose lean; tables carry the load here.

## Outputs

- `proposal/sections/workpackages.tex`.
- `.grantstack/wp-plan.md` — working notes: WP list, milestone register, critical path.
- Summary block: WP count, the critical path, and any objective not yet covered by a WP.

## Anti-patterns to refuse

- **WPs that don't map to objectives** (or objectives with no WP). The mapping must be total.
- **A milestone that isn't verifiable.** "Progress on X" is not a milestone; "dataset Y assembled and validated" is.
- **A timeline with no slack.** A plan with zero buffer reads as one that hasn't met reality. Show where the give is.
- **Everything depending on WP1.** Single points of failure are feasibility risks; parallelize or stage.

## When to call other skills

- Before: `/objectives`, `/risk-register`.
- After: `/budget` (cost the WPs), `/team-resources` (staff the WPs), then `/feasibility-audit`.
