---
name: rebuttal
description: Drafts the written response to referee reports for schemes that grant a right of reply — chiefly the NWO Talent rebuttal stage — mapping every referee point to a typed response without conceding the ambition. Use when reports have arrived and a reply is due. ERC grants no written rebuttal, so there the reports feed /grantstack:retro and /grantstack:resubmit instead.
argument-hint: "[r1|r2]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(date *)
---

# /grantstack:rebuttal

**Stage:** defend · **Voice:** the applicant addressing the committee — confident, deferential, never combative

NWO Talent runs a formal **rebuttal** stage: the referee reports come back, the applicant replies in writing under a tight word limit, and the committee reads proposal, reports, and reply together. A strong rebuttal turns a borderline into a fundable; a defensive one confirms the doubts.

**ERC has no written rebuttal.** Its applicants do not see the referee comments before the interview — the evaluation report arrives with the final decision. So for an ERC proposal this skill does not apply: the step-2 interview is a pitch and a defence of the proposal as written (`/grantstack:interview-prep`), and the reports, when they come, feed `/grantstack:retro` and `/grantstack:resubmit`. Check the scheme in `${CLAUDE_PLUGIN_ROOT}/references/schemes.md` before drafting anything, and say so rather than producing a document that has nowhere to go.

`$ARGUMENTS` is the round label, default `r1`.

## Procedure

1. **Take delivery of the reports.** Read `reviews/received/<round>-*.md` and any PDFs there. If the user has the reports but they are not on disk, save them as a **new** file — `reviews/received/<round>-referees.md` — never appending to or editing an existing one: `reviews/received/` is read-only once a file exists, because the report as received is the record. If nothing is there, stop and ask; you cannot rebut what you cannot see.
2. **Load** the proposal, any prior `.grantstack/review-cache/panel-mock-*` (you may already have simulated these comments), and the "reading a report in order to answer it" section of `${CLAUDE_PLUGIN_ROOT}/references/panel-report-conventions.md`.
3. **Parse every point** into one structured list per referee, numbered as the referee numbered them. Tag each: **Misunderstanding** (they missed something that is there), **Real weakness** (a fair hit), **Disagreement** (a defensible difference of judgement), **Out of scope** (asks for a different project). Count what recurs: a concern raised by one referee is an opinion, the same concern from two is the committee's view.
4. **Draft a response per point**, in three parts: **restate** the point fairly and briefly, without strawmanning — the committee has the original; **respond by type** —
   - *Misunderstanding* — point to where it is addressed, and consider whether the proposal made it too easy to miss. If two referees misread the same passage, the passage is the problem.
   - *Real weakness* — concede gracefully and say precisely what is strengthened or how it is mitigated. Conceding well buys credibility for where you stand firm.
   - *Disagreement* — defend with evidence and reasoning, respectfully. You may disagree with a referee; do it with data, not heat.
   - *Out of scope* — affirm the chosen scope and why; do not expand to chase a referee's different paper.

   — and **state what changed**, or what the committee should weigh.
5. **Open with a short frame:** thank the referees once, name the two or three most consequential clarifications, and say how the reply is organized. The word limit is tight — spend it on the points that move the decision.
6. **Protect the ambition.** The cardinal error is conceding the bold core to placate a cautious referee. "Too risky" is answered with the risk register's fallback, not with a smaller project.
7. **Save** to `reviews/rebuttal/<round>-rebuttal.md` (date from `date +%F`), append a line to `decisions:` in `.grantstack/config.yaml` recording the round and the stance taken, and set `grant.status: "rebuttal"` if it still says `submitted`.

## Outputs

- `reviews/rebuttal/<round>-rebuttal.md` — the drafted reply.
- `reviews/received/<round>-referees.md`, when the user supplied the reports as text.
- Summary block: the points by type, the two or three decisive responses, and any point left unaddressed.

## Anti-patterns

- **Conceding the bold core to placate.** Defend the ambition with the fallback plan.
- **Combative tone.** Committees reward confident deference, not point-scoring.
- **Spending the word limit on minor points.** Lead with what moves the decision.
- **"We thank the reviewer" on every line.** Once, up front, is enough.

## Next

`/grantstack:panel-mock chair` to pressure-test how the committee will read the reply; then `/grantstack:interview-prep`, where the contested points become the hardest questions.
