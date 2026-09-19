---
name: call-spec
description: Ingests the actual call, work programme, or template and extracts its hard requirements — eligibility, page and word limits per part, font and margin rules, mandatory sections and annexes, budget ceiling, evaluation criteria and weights — into a checklist, then audits the proposal against it and reports every blocker. Use early to capture the rules, and again before submission to check compliance and catch desk-reject risks.
argument-hint: "[capture|audit|recapture]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - WebFetch
  - Bash(date *)
  - Bash(wc *)
  - Bash(pdftotext *)
---

# /grantstack:call-spec

**Stage:** frame (capture) / stress-test (audit) — run at both ends · **Voice:** compliance officer (the desk officer who screens before review)

Every funder publishes hard gates: page limits per part, font and margins, mandatory sections and annexes, eligibility rules, budget ceilings, and the evaluation criteria with their weights. Violating a formatting gate gets a proposal **desk-rejected before a reviewer reads it**; missing a weighted criterion loses points the science cannot win back. This skill makes the call the contract.

`$ARGUMENTS`: `capture` (default when no spec exists), `audit` (default when one does), or `recapture` (the call was updated, or the scheme changed).

## Procedure — capture

1. **Take delivery of the source.** Read whatever is in `admin/call/`. If it is empty, ask the user to paste the call text or drop the PDF there, or give a URL to fetch. Pasted text is saved verbatim to `admin/call/<scheme>-<year>-call.md` **before** anything is extracted, so the spec is auditable against its source and the status script can tell when the call is newer than the spec. A revised call is a new file, never an edit: `admin/call/` is read-only once a file exists. Read a PDF directly, or with `pdftotext` when that fails. If no source is provided, say so and stop — an invented spec is worse than none.
2. **Read** `${CLAUDE_PLUGIN_ROOT}/references/schemes.md` for the shape of the scheme, so you know what to look for and what its absence would mean. It is background only: every value comes from the source document.
3. **Extract requirements** into categories, recording the rule **and the exact source line** so it is auditable:
   - **Eligibility** — windows, extensions, host conditions, resubmission bars.
   - **Structure** — every mandatory part and its order; the optional ones.
   - **Length** — page or word limit *per part*, and what counts toward it (references? figures?).
   - **Formatting** — font family and minimum size, line spacing, margins, reference style.
   - **Annexes** — CV and track record, budget table, DMP, ethics, host letters, each with its own limit and format.
   - **Budget** — ceiling, eligible cost categories, duration limits, modules.
   - **Evaluation** — criteria, weights, scoring scale. These say what the proposal must visibly answer.
   - **Logistics** — portal, deadline (cross-check `grant.call_deadline`), language, AI-use disclosure rule if the call has one.
4. **Write `.grantstack/call-spec.md`** as a checklist: each requirement with a `[ ]` box, the rule, the source line, and the target value. Add an **evaluation map** at the bottom: each criterion and the section meant to satisfy it.
5. **Flag unknowns** under "UNCONFIRMED — verify against the call" rather than asserting them.

## Procedure — audit

1. **Load** `.grantstack/call-spec.md` and the proposal in full: `proposal/main.tex`, every file in `proposal/sections/`, `cv/track-record.md`, `budget/budget.md`, `admin/`.
2. **Check each requirement** and mark it pass/fail:
   - **Length:** if a built PDF exists, use it. Otherwise count words with `wc -w` and flag parts likely over, stating the method and its uncertainty. Never claim a precise page count you did not measure.
   - **Structure:** every mandatory part present and in order; no missing annex.
   - **Formatting:** the settings in `proposal/main.tex` match the rule; flag what cannot be verified from source.
   - **Budget:** total within the ceiling; only eligible categories.
   - **Evaluation map:** each criterion visibly addressed by some section; flag any with no clear home — especially impact / knowledge utilisation, which applicants under-serve.
3. **Run the cleanliness sweep** and report the literal counts as evidence: `TODO`, `UNCONFIRMED`, `[ACTION:`, `\cite{TODO`, and the template placeholders `ACRONYM --- TITLE`, `PI NAME`, `HOST INSTITUTION`. Each must be zero in every file that gets submitted.
4. **Write `.grantstack/call-spec-audit-<YYYY-MM-DD>.md`** (date from `date +%F`): the verdict line, then a pass/fail table, then a prioritized fix list — **blockers** (desk-reject risks: over length, missing mandatory part, over budget, a surviving placeholder) first, then **scoring gaps** (a weighted criterion under-addressed), then **minor**. Do not tick boxes in `call-spec.md`: the spec is the contract and stays as captured, or every audit is stale against its own input.

   **Verdict**, the first line of the audit: **Compliant**, or **N blockers**.
5. **Advance the stage.** Set `grant.status: "review"` in `.grantstack/config.yaml` if it still says `writing`.

## Outputs

- `admin/call/<scheme>-<year>-call.md` — the call as supplied, when the user pasted it (capture).
- `.grantstack/call-spec.md` — requirements checklist + evaluation map (capture).
- `.grantstack/call-spec-audit-<date>.md` — verdict, pass/fail table, prioritized fixes (audit).
- Summary block: blockers listed explicitly, then the counts of scoring gaps and minor issues.

## Anti-patterns

- **Inventing requirements from memory.** Calls vary by year, panel, and domain. Capture from the document or mark UNCONFIRMED.
- **Claiming an exact page count from LaTeX source.** State the method and its limits; recommend building the PDF for a true count.
- **Burying a desk-reject blocker among style nits.** Blockers lead.
- **Passing a proposal that ignores a weighted criterion** because every section "exists". A thin impact section against a weighted criterion is a scoring gap, not a pass.

## Next

After capture, the spec sets the page budget for `/grantstack:draft-section` and the ceiling for `/grantstack:budget`. After an audit with blockers: fix and re-run. A clean audit is the gate for `/grantstack:admin-pack`; `/grantstack:feasibility-audit` checks internal consistency, which is a different question.
