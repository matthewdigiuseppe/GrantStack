---
name: budget
description: Builds the budget and its justification, every line mapped to a work package and a deliverable, within the scheme ceiling. Writes budget/budget.md. Use after /workpackage and /team-resources.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:budget

**Stage:** design
**Voice:** grants finance officer

## When to invoke

After the WPs and team are designed. The budget is a feasibility argument in numbers: a panel checks that the money buys the science, that nothing is padded, and that nothing essential is missing (a common own-goal is forgetting open-access, archiving, or audit costs). It must come in at or under the scheme ceiling.

## Procedure

1. **Load.** `.grantstack/team-plan.md`, `proposal/sections/workpackages.tex`, `.grantstack/config.yaml` (amount, currency, duration), `.grantstack/call-spec.md` (eligible cost categories and ceiling, if captured).

2. **Cost the categories:**
   - **Personnel** — from the team plan: role × FTE-months × institutional rate (use the host's real rates if known; otherwise mark `[rate: confirm with grants office]`). Usually the largest line.
   - **Equipment** — one-off purchases; for ERC, start-up/major-equipment costs may have their own envelope.
   - **Consumables** — materials, samples, compute, licences.
   - **Travel / fieldwork / dissemination** — conferences, fieldwork trips, workshops you host.
   - **Other** — open-access publishing, data archiving, audit certificate, recruitment, participant payments.

3. **Map every line to a WP and deliverable.** A reader should trace each euro to a piece of science. Add a per-WP allocation table.

4. **Check against the ceiling and rules.** Total ≤ ceiling from `call-spec`. Only eligible categories. Flag anything that needs grants-office confirmation rather than asserting a number you don't have.

5. **Write the justification.** Short prose per category explaining *why* — especially for the big and the unusual lines. "Two postdocs because WP2 and WP3 run in parallel and each needs full-time methodological depth" beats a bare number.

6. **Write `budget/budget.md`.** Headline table, per-WP allocation, and the category justifications. Note any figures pending host confirmation.

## Outputs

- `budget/budget.md` — headline table, per-WP allocation, justification prose.
- Summary block: total vs. ceiling, the three largest lines, and any figure flagged for grants-office confirmation.

## Anti-patterns to refuse

- **Numbers untraceable to WPs.** Every line maps to science.
- **Inventing institutional rates.** If you don't have the host's rates, mark them to confirm; don't fabricate.
- **Forgetting the boring mandatory costs** (open access, archiving, audit). Their absence reads as inexperience.
- **Padding.** A panel that smells padding distrusts the whole proposal. Justify, don't inflate.

## When to call other skills

- Before: `/workpackage`, `/team-resources`, and `/call-spec` (for the ceiling and eligible categories).
- After: `/feasibility-audit` (does budget ↔ WP ↔ timeline close).
