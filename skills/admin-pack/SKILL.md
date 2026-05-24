---
name: admin-pack
description: Assembles and checks the administrative submission package — eligibility declaration, host support/commitment letter, budget forms, DMP, ethics self-assessment, and the call's required annexes — so nothing administrative sinks a strong proposal. Writes admin/ files and a submission checklist. Analog to MStack's /cover-letter, broadened to the full grant admin pack.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
  - Glob
---

# /grantstack:admin-pack

**Stage:** submit/defend
**Voice:** grants-office coordinator

## When to invoke

In the run-up to the deadline, once the science is fixed. Strong proposals get rejected on administrivia — a missing host letter, an unsigned declaration, a budget form in the wrong format, an unaddressed ethics flag. This skill assembles the non-science package and checks it against the call.

## Procedure

1. **Load.** `.grantstack/call-spec.md` (the required annexes and forms), `.grantstack/config.yaml` (host, deadline, eligibility notes), `budget/budget.md`, `admin/*`, `proposal/sections/data-management.tex`, `proposal/sections/ethics.tex`.

2. **Build the submission checklist** from the call's annex requirements. For each item, mark have / draft / missing:
   - Eligibility declaration (windows, extensions, prior-grant statements).
   - Host support / commitment letter (space, cost-sharing, hosting statement).
   - Budget form in the funder's required format.
   - Data management plan.
   - Ethics self-assessment / statement (and any flagged-issue documentation).
   - CV / track-record annex in the prescribed format.
   - Any scheme-specific forms (e.g., funding ID, PI commitment statement, letters of support from partners).

3. **Draft what can be drafted.** For documents you can author from on-file material — eligibility declaration, host-letter skeleton (for the host to finalize), DMP, ethics statement — produce drafts into `admin/`. Mark anything that needs a signature, an official rate, or a third party as `[ACTION: <who> must provide]`.

4. **Cross-check the boring killers.**
   - Eligibility window math against `pi.phd_year` and any extensions — flag if close to a cutoff and tell the user to confirm against the call.
   - Deadline (`config.call_deadline`) and timezone; portal cutoff is usually a hard wall.
   - Budget total matches `budget/budget.md` and the proposal text.
   - Every ethics category addressed (no blanks).

5. **Write** `admin/submission-checklist.md` plus the drafted documents.

## Outputs

- `admin/submission-checklist.md` — every required item with status and owner.
- Drafted `admin/eligibility.md`, `admin/host-support.md`, and updated DMP/ethics as applicable.
- Summary block: missing items, items awaiting third parties, and any deadline/eligibility risk.

## Anti-patterns to refuse

- **Faking a signature, rate, or letter.** Draft skeletons and mark who must sign/provide; never fabricate institutional commitments.
- **Asserting eligibility you can't verify.** Flag close cases for confirmation against the call and the grants office.
- **Treating admin as trivial.** A missing annex is as fatal as a weak methodology — and far cheaper to fix.

## When to call other skills

- Before: `/call-spec` (the checklist comes from the captured spec) and `/budget`.
- Pair with: `/call-spec audit` (formatting/length) for total pre-submission coverage.
