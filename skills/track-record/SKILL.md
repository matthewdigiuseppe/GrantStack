---
name: track-record
description: Builds the PI track-record / CV narrative — the "excellence of the applicant" half of the score — selecting and framing achievements to evidence ground-breaking capacity, not dumping a CV. Scheme-aware (ERC "CV and Track Record" section vs. NWO CV + key output). Writes cv/track-record.md and proposal/sections/pi-track-record.tex.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:track-record

**Stage:** write
**Voice:** advocate (a senior colleague writing your case, evidence in hand)

## When to invoke

Once the project is taking shape. In ERC and NWO the **person and the project are scored together** — a brilliant project with a weak track-record case loses. This section must argue, with evidence, that you are the right person to deliver *this* breakthrough. It is curation, not enumeration.

## Procedure

1. **Load.** `cv/track-record.md` (raw material), `.grantstack/big-idea.md` (the "why you" answer), `.grantstack/config.yaml` (scheme), `.grantstack/call-spec.md` (the CV/track-record format and limits the call dictates).

2. **Select against the project.** From the raw material, choose the achievements that evidence the specific capacities this project demands — the method you've pioneered, the independence you've shown, the hard problems you've cracked. Cut anything that doesn't build the case, however nice.

3. **Frame each achievement with its significance.** Not "published in X" but "established Y, now the basis for Z." For ERC's "CV and Track Record" section, choose a curated set of achievements (papers, monographs, datasets, talks, prizes, supervision, leadership) that together tell one story: this person opens new ground. Follow the call's current CV format and item counts from `call-spec` — the exact structure has changed across recent work programmes, so don't assume a fixed number.

4. **Evidence independence and leadership.** Last-author/sole work, own funding, group built, infrastructure created, students graduated. These tell the panel you can run the group the grant funds.

5. **Handle the career arc honestly.** Use eligibility extensions and any non-linear path as context, not apology. Show trajectory and momentum.

6. **Match the scheme's format.**
   - **ERC** — the "CV and Track Record" section (CV, funding ID, and a curated set of achievements evidencing independence and ground-breaking capacity), per the current call's format.
   - **NWO** — CV + key-output list + academic-profile narrative.
   Follow the call's structure exactly (from `call-spec`).

7. **Write outputs.** The narrative/profile prose to `proposal/sections/pi-track-record.tex`; keep the structured CV/output lists in `cv/track-record.md`.

## Outputs

- `proposal/sections/pi-track-record.tex` — the narrative case.
- `cv/track-record.md` — updated structured CV + curated achievement list.
- Summary block: the through-line ("this person can do this because…"), and any gap in the case worth strengthening before submission.

## Anti-patterns to refuse

- **A CV dump.** Length is not strength; relevance is. Curate to the project.
- **Modesty that reads as weakness.** State significance plainly; the panel won't infer it.
- **Listing outputs without their meaning.** Each item needs a "why this matters."
- **Ignoring the call's format.** Wrong CV format can be a desk-reject; follow `call-spec`.

## When to call other skills

- Before: `/big-idea` (the "why you" answer feeds this).
- After: `/panel-mock` (the person is part of what the panel scores); `/call-spec audit` to confirm CV format compliance.
