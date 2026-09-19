---
name: team-resources
description: Designs the team and resources — who you hire, their remit and FTE-months, the infrastructure and host facilities the project needs — mapped to the work packages, and writes the role table to .grantstack/team-plan.md for the budget to cost. Use after the work packages exist, before or alongside costing them.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:team-resources

**Stage:** design · **Voice:** group leader planning a five-year team

A panel reads the team plan to check that the people the budget buys can deliver the WPs in the term, and that the PI has thought about who does what rather than only how much it costs. At ERC and Vici scale it is also where you show you can *lead a group*.

## Procedure

1. **Load** `proposal/sections/workpackages.tex`, `.grantstack/wp-plan.md`, `.grantstack/config.yaml` (duration, budget), the team bar in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`, and the person-month checks in `${CLAUDE_PLUGIN_ROOT}/references/feasibility-catalog.md`.
2. **Staff each WP.** For each work package decide the roles:
   - **PI** — the intellectual lead and the WPs they run hands-on; be honest about PI time, which these schemes often expect to be substantial.
   - **Postdocs** — for the bold, methodologically demanding WPs; specify the profile and the months.
   - **PhD students** — for sustained, well-scoped strands; a PhD is ~3-4 years and needs a coherent thesis arc, not scattered tasks.
   - **Technicians / RSEs / RAs** — infrastructure, data, engineering.

   Give each role a one-line remit and an FTE-months figure; these feed `/grantstack:budget`.
3. **Check the staffing is deliverable.** No person is on the critical path of two WPs at once beyond 1.0 FTE; each hire's start aligns with their WP, with recruitment lead time allowed; the PhD arcs are coherent theses, not labour pools; the PI's supervision load is plausible against the PI's own committed time.
4. **Resources and host facilities.** Equipment, compute, access, lab or archive space, partnerships. Separate what the host already provides — which strengthens feasibility and evidences host commitment — from what the grant must buy.
5. **Write** `.grantstack/team-plan.md`: the role × WP × FTE-months table and the resource list, with total person-months stated so the budget and the WP table can be checked against it.

   The prose version belongs in `proposal/sections/feasibility.tex`, which `/grantstack:draft-section feasibility` composes from this memo and the risk register — do not write that file here, or the two skills will overwrite each other.

## Outputs

- `.grantstack/team-plan.md` — role × WP × FTE-months table, total person-months, resource list.
- Summary block: headcount, total FTE-years, and any WP that looks under- or over-staffed.

## Anti-patterns

- **A team that cannot cover the WPs in the term**, or one padded beyond what the WPs need.
- **PhD students assigned the highest-risk core.** High-risk work belongs with a postdoc or the PI; a student's thesis should not hinge on the riskiest bet.
- **Ignoring recruitment lead time.** A hire starting in month 1 is rarely real; show the ramp.
- **Vague "research staff".** Name roles and remits; the panel costs people, not placeholders.

## Next

`/grantstack:budget` to cost the roles, then `/grantstack:feasibility-audit`.
