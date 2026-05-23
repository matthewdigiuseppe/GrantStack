---
name: call-spec
description: Ingests the actual call/template document and extracts its hard requirements — eligibility, page limits, font and margin rules, mandatory sections and annexes, budget ceiling, evaluation criteria and weights — into a checklist, then audits the proposal against it and reports every misalignment. Run early to capture the rules; re-run before submission to verify compliance. No MStack analog — grant-specific.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash(date *)
  - Bash(wc *)
  - Bash(pdftotext *)
---

# /grantstack:call-spec

**Stage:** frame (capture) / write (audit) — run at both ends
**Voice:** compliance officer (the desk officer who screens before review)

## Why this exists

Every funder publishes a call document, work programme, and template with **hard gates**: page limits per part, font size and margins, mandatory sections and annexes, eligibility rules, budget ceilings, and the evaluation criteria with their weights. Violating a formatting gate gets a proposal **desk-rejected before a reviewer reads it**. Missing a mandatory section or an evaluation criterion loses points that the science can't win back. This skill makes the call the contract and checks the proposal against it.

It has two modes — **capture** and **audit** — and the argument selects which.

## Argument

`$ARGUMENTS`:
- `capture` (default if no spec exists) — ingest the call and build the spec.
- `audit` (default if a spec exists) — check the current proposal against the spec.
- `recapture` — re-ingest (e.g., the call was updated or you switched schemes).

## Procedure — capture

1. **Get the source.** Ask the user to paste the call/template text, or to drop the call PDF in `admin/` (read it with `pdftotext` via Bash). Do not guess requirements from memory of "how ERC/NWO usually works" — calls change yearly and per panel. If no source is provided, say so and stop; an invented spec is worse than none.

2. **Extract requirements** into structured categories. For each, record the rule **and the exact source line** so it's auditable:
   - **Eligibility** — windows, host conditions, resubmission bars.
   - **Structure** — every mandatory section/part and its order; any optional sections.
   - **Length** — page or word limit *per part* (e.g., ERC B1 synopsis ≤5pp, B2 ≤14pp), and what counts toward the limit (references? figures?).
   - **Formatting** — font family and minimum size, line spacing, margins, reference style.
   - **Annexes** — CV, track record, budget table, DMP, ethics, host letters, and their own limits.
   - **Budget** — ceiling, eligible cost categories, duration limits.
   - **Evaluation** — the criteria and their weights, and the scoring scale. These tell you what the proposal must visibly answer.
   - **Logistics** — submission portal, deadline (cross-check `config.call_deadline`), language.

3. **Write `.grantstack/call-spec.md`** as a checklist: each requirement with a `[ ]` box, the rule, the source line, and (for length/format) the target value. Add a short "evaluation map" at the bottom listing each criterion and which proposal section is meant to satisfy it.

4. **Flag unknowns.** Any requirement you couldn't find a source for, list under "UNCONFIRMED — verify against the call" rather than asserting it.

## Procedure — audit

1. **Load `.grantstack/call-spec.md`** and the proposal (`proposal/main.tex`, `proposal/sections/*`, annex files in `cv/`, `budget/`, `admin/`).

2. **Check each requirement** and mark the box pass/fail:
   - **Length:** estimate per-part length. For LaTeX you cannot count rendered pages exactly — if a built PDF exists use it; otherwise count words and flag parts that are likely over, stating the method and its uncertainty. Never claim a precise page count you didn't measure.
   - **Structure:** every mandatory section present and in order; no missing annex.
   - **Formatting:** font/margin/spacing settings in `main.tex` match the rule (flag if the template can't be verified from source).
   - **Budget:** total ≤ ceiling; only eligible categories used.
   - **Evaluation map:** for each criterion, confirm a section visibly addresses it; flag any criterion with no clear home (especially knowledge utilisation / impact, which applicants under-serve).

3. **Report.** A pass/fail table plus a prioritized fix list: **blockers** (desk-reject risks — over length, missing mandatory part, over budget) first, then **scoring gaps** (an evaluation criterion under-addressed), then **minor** (style nits).

4. **Write `.grantstack/call-spec-audit-<YYYY-MM-DD>.md`** and update the checkboxes in `call-spec.md`.

## Outputs

- `.grantstack/call-spec.md` — the requirements checklist + evaluation map (capture).
- `.grantstack/call-spec-audit-<date>.md` — pass/fail report + prioritized fixes (audit).
- Summary block: count of blockers, scoring gaps, and minor issues, with the blockers listed explicitly.

## Anti-patterns to refuse

- **Inventing requirements from memory.** Calls vary by year and panel. Capture from the actual document or mark UNCONFIRMED.
- **Claiming an exact page count from LaTeX source.** State your measurement method and its limits; recommend building the PDF for a true count.
- **Burying a desk-reject blocker among style nits.** Blockers lead the report.
- **Passing a proposal that ignores a weighted evaluation criterion** just because every section "exists." If impact/knowledge-utilisation is weighted and thin, that's a scoring gap, not a pass.

## When to call other skills

- After **capture**: the spec informs every drafting skill — note page budgets before `/draft-section`.
- After **audit** with blockers: fix, then re-run; pair with `/feasibility-audit` for internal (not call) consistency.
- Before submission: a clean `audit` is a gate for `/admin-pack`.
