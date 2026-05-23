---
name: rebuttal
description: Drafts the written response to referee reports for schemes that grant a right of reply — chiefly the NWO Talent rebuttal stage — mapping every referee point to a concrete answer without conceding the ambition. (ERC has no written rebuttal; its step-2 reply is the interview, so use /interview-prep there.) Writes reviews/rebuttal/<round>-rebuttal.md. Analog to MStack's /r-and-r, calibrated to grant panels.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
  - Grep
---

# /grantstack:rebuttal

**Stage:** submit/defend
**Voice:** applicant addressing the committee (confident, deferential, never combative)

## When to invoke

You've received written referee reports and the scheme grants a right of reply before the decision or interview. NWO Talent schemes have a formal **rebuttal** stage; this skill is built for that. ERC does **not** take a written rebuttal — at step 2 you reply to the referees *in the interview*, so there the output of this skill feeds `/interview-prep` rather than a submitted document. A strong rebuttal turns a borderline into a fundable; a defensive one confirms the doubts.

## Argument

`$ARGUMENTS` (optional) — round label. Default `r1`.

## Procedure

1. **Load the reports.** Ask the user to paste the referee reports into `reviews/rebuttal/<round>-referees.md` if not already there. Read them. If empty, stop and ask for the reports — you cannot rebut what you can't see.

2. **Load the proposal** and any prior `.grantstack/review-cache/panel-mock-*` (you may have already simulated these comments).

3. **Parse every point.** One structured list per referee, comments numbered as the referee numbered them. Tag each: `Misunderstanding` (they missed something that's there), `Real weakness` (a fair hit), `Disagreement` (a defensible difference of judgment), `Out of scope` (asks for a different project).

4. **For each point, draft a response** in three parts:
   1. **Restate the point** fairly and briefly (in italics/blockquote). Don't strawman; the committee has the original.
   2. **Respond by type:**
      - *Misunderstanding* — point to where it's addressed; consider whether the proposal made it too easy to miss (often the real fix).
      - *Real weakness* — concede gracefully and state precisely what you've strengthened or how you'll mitigate. Conceding well builds credibility for where you stand firm.
      - *Disagreement* — defend with evidence and reasoning, respectfully. You're allowed to disagree with a referee; do it with data, not heat.
      - *Out of scope* — affirm the project's chosen scope and why; don't expand to chase a referee's different paper.
   3. **State what changed** (if a revision is possible) or what the committee should weigh.

5. **Open with a short frame:** thank the referees once, name the 2-3 most consequential clarifications, and state how the rebuttal is organized. Word limits on rebuttals are usually tight — prioritize the points that move the decision, don't spend the budget on minor ones.

6. **Protect the ambition.** The cardinal error is conceding the bold core to placate a cautious referee. If a referee says "too risky," the answer is the risk-register's fallback, not a smaller project.

7. **Save** to `reviews/rebuttal/<round>-rebuttal.md` and log to `.grantstack/decisions.log`.

## Outputs

- `reviews/rebuttal/<round>-referees.md` — the reports (created if missing).
- `reviews/rebuttal/<round>-rebuttal.md` — the drafted rebuttal.
- Summary block: the points by type, the 2-3 decisive responses, and any point left unaddressed.

## Anti-patterns to refuse

- **Conceding the bold core to placate.** Defend the ambition with the fallback plan.
- **Combative tone.** Committees reward confident deference, not point-scoring.
- **Spending the word limit on minor points.** Lead with what moves the decision.
- **"We thank the reviewer" on every line.** Once, up front, is enough.

## When to call other skills

- Before: `/panel-mock` to pressure-test the rebuttal as the committee will read it.
- After: `/interview-prep` — the contested points become the interview's hardest questions.
