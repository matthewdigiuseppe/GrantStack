---
name: team-resources
description: Designs the team and resources — who you hire (PhDs, postdocs, technicians), what each does, and the infrastructure/host facilities the project needs — mapped to the work packages. Use after /workpackage, before or alongside /budget.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:team-resources

**Stage:** design
**Voice:** group leader planning a five-year team

## When to invoke

After work packages exist. A panel reads the team plan to check that the people the budget buys can actually deliver the WPs in the term — and that the PI has thought about who does what, not just how much it costs. For ERC/Vici this is also where you show you can *lead a group*, which is part of being fundable at this level.

## Procedure

1. **Load.** `proposal/sections/workpackages.tex`, `.grantstack/wp-plan.md`, `.grantstack/config.yaml` (duration, budget).

2. **Staff each WP.** For each work package, decide the roles:
   - **PI** — the intellectual lead and the WPs they run hands-on. Be honest about PI time (these grants often expect a substantial PI commitment).
   - **Postdocs** — for the bold, methodologically demanding WPs; specify the profile and the months.
   - **PhD students** — for sustained, well-scoped strands; remember a PhD is ~3-4 years and needs a coherent thesis arc, not scattered tasks.
   - **Technicians / RSEs / RAs** — for infrastructure, data, engineering.
   Give each role a one-line remit and an FTE-months figure (these feed `/budget`).

3. **Check the staffing is deliverable.**
   - No person is on the critical path of two WPs at the same time beyond 1.0 FTE.
   - Each hire's start aligns with when their WP begins (and recruitment lead time is allowed for).
   - The PhD arcs are coherent theses, not labour pools.

4. **Resources and host facilities.** Equipment, compute, access, lab/archive space, partnerships. Note what the host already provides (strengthens feasibility and shows host commitment) versus what the grant must buy.

5. **Write outputs.** A team-and-resources block into `proposal/sections/feasibility.tex` (or a dedicated subsection if the template wants one), and a role/FTE table to `.grantstack/team-plan.md` for `/budget` to cost.

## Outputs

- `proposal/sections/feasibility.tex` — team and resources prose (created or appended; coordinate with `/risk-register` and `/methodology`).
- `.grantstack/team-plan.md` — role × WP × FTE-months table + resource list.
- Summary block: headcount, total FTE-years, and any WP that looks under- or over-staffed.

## Anti-patterns to refuse

- **A team that can't cover the WPs in the term**, or one padded beyond what the WPs need.
- **PhD students assigned the highest-risk core.** High-risk work usually belongs with a postdoc or the PI; a student's thesis shouldn't hinge on the riskiest bet.
- **Ignoring recruitment lead time.** A hire starting in month 1 is rarely real; show the ramp.
- **Vague "research staff."** Name roles and remits; the panel costs people, not placeholders.

## When to call other skills

- Before: `/workpackage`.
- After: `/budget` (cost the roles), `/feasibility-audit`.
