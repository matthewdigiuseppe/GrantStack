---
name: track-record
description: Builds the "excellence of the applicant" case — selecting and framing achievements that evidence independence and ground-breaking capacity for this specific project, in the CV format the call dictates — and writes proposal/sections/pi-track-record.tex plus the curated cv/track-record.md. Use once the project is taking shape; the person is half the score.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:track-record

**Stage:** write · **Voice:** advocate — a senior colleague writing your case, evidence in hand

In ERC and NWO the **person and the project are scored together**: a brilliant project with a weak track-record case loses. This section argues, with evidence, that you are the right person to deliver *this* breakthrough. Curation, not enumeration.

## Procedure

1. **Load** `cv/track-record.md` (the raw material), `.grantstack/big-idea.md` (the "why you" answer), `.grantstack/config.yaml`, `.grantstack/call-spec.md` (the CV format and limits this call dictates), `.grantstack/learnings.jsonl`, the track-record bar in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`, and the scheme's CV rules in `${CLAUDE_PLUGIN_ROOT}/references/schemes.md`.
2. **Select against the project.** Choose the achievements that evidence the capacities *this* project demands — the method you pioneered, the independence you have shown, the hard problems you cracked. Cut anything that does not build the case, however nice.
3. **Frame each achievement with its significance.** Not "published in X" but "established Y, now the basis for Z". Together they must tell one story: this person opens new ground.
4. **Evidence independence and leadership.** Last-author or sole work, own funding, group built, infrastructure created, students graduated. These tell the panel you can run the group the grant funds.
5. **Handle the career arc honestly.** Eligibility extensions and non-linear paths are context, not apology; show trajectory and momentum.
6. **Match the scheme's format exactly**, from `call-spec.md`: ERC's CV and track-record structure has changed between work programmes, and **NWO's narrative-CV rules bar journal impact factors, h-indices and similar metrics** — a metrics-led CV for an NWO committee is a self-inflicted wound. Do not assume a fixed item count.
7. **Write** the narrative case to `proposal/sections/pi-track-record.tex` and keep the structured CV and curated output list in `cv/track-record.md`. Set `grant.status: "writing"` in `.grantstack/config.yaml` if it still says `designing`.

## Outputs

- `proposal/sections/pi-track-record.tex` — the narrative case.
- `cv/track-record.md` — updated structured CV and curated achievement list.
- Summary block: the through-line ("this person can do this because…") and any gap in the case worth strengthening before submission.

## Anti-patterns

- **A CV dump.** Length is not strength; relevance is.
- **Modesty that reads as weakness.** State significance plainly; the panel will not infer it.
- **Listing outputs without their meaning.** Each item needs its "why this matters".
- **Ignoring the call's format.** The wrong CV format can be a desk reject, and barred metrics are worse than none.

## Next

`/grantstack:panel-mock` — the person is part of what the panel scores — and `/grantstack:call-spec audit` to confirm CV-format compliance.
