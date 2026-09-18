---
name: budget
description: Costs the work packages and team within the scheme ceiling, maps every line to a WP and a deliverable, and writes the headline table, per-WP allocation and justification to budget/budget.md. Use after the work packages and team plan exist, or when the user needs to check the budget against the call's ceiling and eligible categories.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:budget

**Stage:** design · **Voice:** grants finance officer

The budget is a feasibility argument in numbers: a panel checks that the money buys the science, that nothing is padded, and that nothing essential is missing. A common own-goal is forgetting open access, archiving, or audit costs.

## Procedure

1. **Load** `.grantstack/team-plan.md`, `proposal/sections/workpackages.tex`, `.grantstack/config.yaml` (amount, currency, duration), `.grantstack/call-spec.md` (ceiling, eligible categories, modules), the budget bar in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`, and the budget structure for this scheme in `${CLAUDE_PLUGIN_ROOT}/references/schemes.md`.
2. **Cost the categories:**
   - **Personnel** — from the team plan: role × FTE-months × institutional rate. Use the host's real rates if known; otherwise mark `[rate: confirm with grants office]`. Usually the largest line.
   - **Equipment** — one-off purchases; note where the scheme gives major equipment its own envelope.
   - **Consumables** — materials, samples, compute, licences.
   - **Travel / fieldwork / dissemination** — conferences, fieldwork, workshops you host.
   - **Other** — open-access publishing, data archiving, audit certificate, recruitment, participant payments.
3. **Map every line to a WP and a deliverable**, in a per-WP allocation table. A reader should trace each euro to a piece of science.
4. **Check before saving:** the total is within the ceiling in `call-spec.md`; the column actually sums; personnel person-months equal the total in `.grantstack/team-plan.md`; the duration matches `budget.duration_months`; every category is eligible under the call; every activity the impact section promises has a line here; and every figure you could not source is marked for grants-office confirmation rather than invented.
5. **Write the justification** — short prose per category explaining *why*, especially for the big and unusual lines. "Two postdocs because WP2 and WP3 run in parallel and each needs full-time methodological depth" beats a bare number.
6. **Write `budget/budget.md`**: headline table, per-WP allocation, category justifications, and any figures pending host confirmation.

## Outputs

- `budget/budget.md` — headline table, per-WP allocation, justification prose.
- Summary block: total versus ceiling, the three largest lines, and every figure flagged for the grants office.

## Anti-patterns

- **Numbers untraceable to WPs.** Every line maps to science.
- **Inventing institutional rates.** Mark them to confirm; do not fabricate.
- **Forgetting the boring mandatory costs** (open access, archiving, audit). Their absence reads as inexperience.
- **Padding.** A panel that smells padding distrusts the whole proposal. Justify, do not inflate.

## Next

`/grantstack:feasibility-audit` — whether budget, WPs, timeline and team close against each other.
