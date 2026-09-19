---
name: admin-pack
description: Assembles and checks the administrative submission package — eligibility declaration, host support letter, budget form, DMP, ethics self-assessment, AI-use disclosure and the call's required annexes — into a checklist where every row carries evidence. Use in the run-up to the deadline once the science is fixed, or when the user asks what is still missing before submitting.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(date *)
---

# /grantstack:admin-pack

**Stage:** submit · **Voice:** grants-office coordinator

Strong proposals get rejected on administrivia: a missing host letter, an unsigned declaration, a budget form in the wrong format, an unaddressed ethics flag. This skill assembles the non-science package and checks it against the call.

## Procedure

1. **Load** `.grantstack/call-spec.md` (the required annexes and forms), `.grantstack/config.yaml` (host, deadline, eligibility notes), `budget/budget.md`, everything in `admin/`, `proposal/sections/data-management.tex`, `proposal/sections/ethics.tex`, the newest `.grantstack/call-spec-audit-*.md`, and the scheme's annex expectations in `${CLAUDE_PLUGIN_ROOT}/references/schemes.md`.
2. **Draft the checklist** from `${CLAUDE_PLUGIN_ROOT}/skills/admin-pack/assets/submission-checklist-template.md`, keeping its rule: every row is PASS, FAIL or WAIVED **and carries evidence** — the count, the date, the file, the command run. A verdict with no evidence has not been checked. Delete rows this call does not require rather than marking them N/A.
3. **Work the required items:** eligibility declaration (windows, extensions, prior-grant statements); host support / commitment letter; budget form in the funder's format; data management plan; ethics self-assessment and any flagged-issue documentation; CV / track-record annex in the prescribed format; AI-use disclosure exactly as the call words it, never asserted from memory; and any scheme-specific forms — funding ID, PI commitment statement, partner letters.
4. **Draft what can be drafted** from on-file material into `admin/`: the eligibility declaration, a host-letter skeleton for the host to finalize, the standalone DMP and ethics annexes composed from the proposal sections. Mark anything needing a signature, an official rate, or a third party as `[ACTION: <who> must provide]`.
5. **Cross-check the boring killers.** Eligibility window against `pi.phd_year` and the claimed extensions, flagged for confirmation rather than asserted. Deadline and timezone from `grant.call_deadline` — a portal cutoff is a hard wall, and the host research office's internal deadline is usually days earlier. Budget total matching `budget/budget.md` and the proposal text. Every ethics category answered explicitly, including the ones that do not apply.
6. **Write `admin/submission-checklist.md` last**, after every annex it reports on, so the checklist is never stale against its own run.
7. **Gate and hand off.** The package is **not ready** while any required row is FAIL without a waiver the user has explicitly acknowledged; say so plainly rather than presenting a near-miss as done. Then remind the user to set `grant.status: "submitted"` in `.grantstack/config.yaml` **once the portal confirms** — do not set it yourself, because submitting is something only they can do.

## Outputs

- `admin/submission-checklist.md` — every required item with verdict, evidence, and owner.
- Drafted `admin/eligibility.md`, `admin/host-support.md`, and the DMP and ethics annexes as applicable.
- Summary block: the blocking rows, the items awaiting third parties, and any deadline or eligibility risk.

## Anti-patterns

- **Faking a signature, rate, or letter.** Draft skeletons and mark who must provide; never fabricate an institutional commitment.
- **Asserting eligibility you cannot verify.** Flag close cases for the grants office and the call.
- **A tick with no evidence.** The evidence column is the point.
- **Treating admin as trivial.** A missing annex is as fatal as a weak methodology, and far cheaper to fix.

## Next

`/grantstack:call-spec audit` covers formatting and length; together they are full pre-submission coverage. After the decision, `/grantstack:rebuttal` (NWO) or `/grantstack:interview-prep`.
