# Feasibility catalog: the contradictions panels find

Read by `/grantstack:feasibility-audit`, `/grantstack:workpackage`,
`/grantstack:budget`, `/grantstack:team-resources`,
`/grantstack:risk-register`, and `/grantstack:draft-section feasibility`.

A proposal is a system of claims that must agree: objectives, work packages,
timeline, team, budget, and the risk register are five views of one project. A
panel does not need to be in the subfield to find a disagreement between them,
which is why these are the cheapest possible points to lose — and the easiest
to catch before submission. Each item below is a check, not a topic.

## Objectives ↔ work packages

- **An objective with no work package.** Read the objectives list and the WP
  table side by side; every objective must appear in at least one WP's aim.
- **A work package serving no objective.** Usually a leftover from an earlier
  framing, and it reads as scope creep to the panel.
- **A deliverable that no objective needs.** Same problem, one level down.
- **The count drifts.** Four objectives in the synopsis, three in the
  objectives section, five in the Gantt — this happens constantly after
  revisions and is spotted instantly.

## Timeline

- **Hiring lead time ignored.** A postdoc starting in month 1 is fiction:
  advertising, shortlisting, notice periods, visas, and relocation take
  months. Work that depends on that person cannot start in month 1 either.
- **The Gantt outlasts the grant.** Sum the critical path and compare it with
  `budget.duration_months`.
- **No writing-up time.** Deliverables due in the final month with analysis
  running until then.
- **Serial dependencies drawn as parallel bars.** If WP3 needs WP2's dataset,
  the bars cannot overlap by more than the handover.
- **Data access, ethics approval, or collaboration agreements assumed
  instantaneous.** Each is a dependency with a lead time and a failure mode;
  ethics review for human participants is routinely measured in months.
- **Fieldwork or collection scheduled without a season, a site, or a permit.**

## Team ↔ person-months ↔ budget

- **The arithmetic does not close.** Total person-months in the WP table must
  equal the person-months in the team plan, which must equal FTE × months in
  the budget. Compute all three and compare; this is the single most common
  hard error.
- **Roles with no WP**, or a WP with no named role.
- **Supervision load implausible.** Count the people the PI supervises
  simultaneously against the PI's own committed time.
- **The PI's own time missing** where the scheme expects it, or claimed where
  the scheme does not fund it.
- **A part-time hire doing full-time work**, or one person on two WPs whose
  bars overlap.

## Budget

- **Lines that buy no science.** Every line maps to a WP and a deliverable.
- **The total exceeds the ceiling** in `.grantstack/call-spec.md`, or the
  requested duration exceeds the scheme's maximum.
- **The sum is wrong.** Add the column.
- **Costs the narrative promises but the budget omits** — open-access fees,
  archiving, data acquisition, participant payments, the
  knowledge-utilisation activities the impact section commits to.
- **Equipment justified by the lab rather than the method.**
- **Rates that do not match the host's actual salary scales**, or a flat rate
  applied where the scheme uses modules.

## Milestones and deliverables

- **Milestones that are not decisions.** A milestone is a go/no-go point with
  a date and a criterion; "dataset assembled" is a deliverable.
- **No milestone on the high-risk objective**, which is precisely where the
  panel wants a decision point and a fallback trigger.
- **Deliverables with no date, or all dated in the final six months.**

## Risk and fallbacks

- **A bold objective with no risk entry.** Every high-risk element in the
  synopsis needs a row.
- **A risk with a mitigation but no fallback.** Mitigation reduces
  probability; the fallback is what still produces a fundable result when the
  risk lands anyway.
- **A fallback that abandons the ambition** — "we would do the safe version
  instead" converts a high-risk/high-gain proposal into an incremental one in
  the reader's mind.
- **Single points of failure unacknowledged:** one collaborator, one archive,
  one instrument, one cohort, one data provider whose terms can change.
- **Risks that are really admissions** ("the method may not work") with no
  evidence either way; those need pilot data, not a mitigation sentence.

## Cross-document consistency

- **The acronym, title, duration, budget total, and number of objectives**
  agree across the proposal, the budget, the CV, and the annexes.
- **The abstract's claims are the objectives' claims.**
- **Ethics and data management promise what the budget and timeline fund.**
- **The track record claims capacity the project plan then does not use**, or
  the plan needs a skill the track record never evidences.

## How to run the audit

Read the documents, compute the three arithmetic checks (person-months, budget
sum, critical path against duration), then walk the pairs above. Report each
contradiction with both sides quoted and the file each came from — a
contradiction stated in the abstract is not actionable, and the applicant must
be able to see which of the two numbers to change.

Close with a verdict line: **Closes** (no contradictions), **Closes with
gaps** (only minor or cosmetic ones), or **Does not close — N contradictions**
(at least one a panel would find). Do not soften it; the whole point is to be
the cheaper version of the reader who finds these for real.
