# Proposal conventions: what each section owes the two readers

Read by `/grantstack:draft-section`, `/grantstack:synopsis-shotgun`,
`/grantstack:lay-summary`, `/grantstack:state-of-art`,
`/grantstack:objectives`, `/grantstack:methodology`,
`/grantstack:workpackage`, `/grantstack:impact`, `/grantstack:track-record`,
`/grantstack:panel-mock` (chair persona) and `/grantstack:mentor-review`.

Voice, rhythm, and vocabulary come from the user's writing-style skill
(`voice.writing_style`); this file is about the substance each section owes.
Criteria and scoring live in `schemes.md`; page limits live in the call, via
`.grantstack/call-spec.md`.

**The two readers.** Every section is read by a **generalist panel member**
who is not in the subfield and decides funding, and an **in-field referee**
who reads deeply and prosecutes novelty and feasibility. A section that serves
only one of them loses the other.

## Extended synopsis / project summary

- Opens with the breakthrough as a single declarative sentence a smart
  non-specialist could repeat from memory. Not with the field, not with
  "despite decades of research".
- Then: why it is not already known, why it is possible *now* (the new data,
  method, theory, or access that changed), and why this applicant.
- The objectives named, the approach in a few sentences, and what the world
  knows at the end that it does not know today.
- The high-risk element stated as a bet, with its payoff — a synopsis that
  hides the risk reads as incremental to the very reader who is looking for
  ambition.
- Written for the generalist, top to bottom. It is the most-read page in the
  application and the one that decides step 1.

## State of the art

- The field as a landscape, not an annotated bibliography: the prevailing
  account, the two or three live disagreements, and where the frontier
  actually is.
- The gap named as a *specific* thing the field cannot currently do or
  explain, positioned against the closest three or four works — including the
  competitors most likely to be reading this proposal.
- Says what those works do not answer without disparaging them. A panel
  containing an author of a cited paper is common.
- Cites only what exists in `proposal/refs.bib`; gaps are marked
  `\cite{TODO-...}` (or `[@TODO-...]` when `grant.format` is markdown), never
  invented.

## Objectives

- Three to four, numbered, each a falsifiable statement with a success
  criterion — what result would count as achieving it, and what result would
  count as failing.
- Each maps to the breakthrough: an objective that does not move the central
  claim is a side project and invites "this is three grants".
- Ordered so the risk is legible: which objective carries the bold bet, which
  de-risk it.
- No objective that is really a task ("build the dataset"); that is a work
  package.

## Methodology / approach

- Rigorous enough for the referee, legible for the generalist: state the
  approach in plain language first, then the technical specification.
- Each method tied to the objective it serves and the work package that
  executes it. A method with no objective is padding; an objective with no
  method is a wish.
- The critical design choices argued, with the alternatives considered and why
  they lose — this is where the in-field referee decides whether the applicant
  knows the terrain.
- Pilot data, preliminary results, or prior work that shows the method works in
  the applicant's hands, where it exists.

## Feasibility and risk

- Per bold objective: the risk, its likelihood and impact, the mitigation, and
  the **fallback that still yields a fundable result**. A high-risk/high-gain
  proposal with no fallbacks reads as reckless; one with no risks reads as
  incremental.
- The fallback preserves the ambition at reduced scope — never "we would
  instead do the safe version of the project".
- Dependencies stated: data access, ethics approval, collaborators,
  infrastructure, and what happens if each is late.

## Work packages

- Every objective covered by at least one WP; every WP serving at least one
  objective; the mapping shown, usually as a table.
- Each WP: aim, tasks, the person doing it, months, deliverables, milestones,
  and its dependencies on other WPs.
- A Gantt or timeline that fits the duration in `budget.duration_months`, with
  hiring lead time at the front and writing-up time at the end.
- Milestones are decision points with dates ("go/no-go on the archival
  strand"); deliverables are artifacts.

## Team and resources

- Who is hired, when, for how long, and which WP they serve — not a wish list
  of roles.
- The applicant's own time on the project, and why the host is the right place:
  infrastructure, collections, cohorts, computing, named collaborators.
- Supervision capacity: a panel notices when one PI is supervising six people
  on a five-year grant with no senior support.

## Budget justification

- Every line maps to a work package and a deliverable; the panel is asking
  "what does this money buy, scientifically?".
- Personnel as FTE × months × rate, matching the team plan exactly.
- Equipment justified by the method that needs it, not by the lab's wishlist.
- The total within the scheme ceiling recorded in `.grantstack/call-spec.md`,
  and the arithmetic correct — a budget that does not sum is the cheapest
  possible way to look unserious.

## Impact / knowledge utilisation

- A scored criterion at NWO and a framing question at ERC (see `schemes.md`);
  write it as a pathway, not a promise.
- Named audiences — specific communities, agencies, practitioners — and the
  concrete activity that reaches each, with timing, responsibility, and cost
  that appears in the budget.
- Scientific impact counts and belongs here: who changes what they do if this
  works.
- "We will publish in leading journals and present at conferences" is the null
  answer and reads as one.

## Track record / CV narrative

- An argument that this applicant can deliver something ground-breaking, not a
  list. Select; do not dump.
- Each selected achievement carries a one-line "why this matters" that
  evidences independence, capacity, or the specific skill the project needs.
- Independence markers: own funding, own group, last-author or sole-author
  work, infrastructure built, people trained.
- Career breaks and non-linear paths stated plainly in the eligibility notes,
  not apologised for.
- **Follow the call's CV format exactly** — ERC's has changed between work
  programmes, and **NWO's narrative-CV rules bar journal impact factors,
  h-indices, and similar metrics** (`schemes.md`). Writing a metrics-led CV for
  an NWO committee is a self-inflicted wound.

## Lay summary

- Plain language for a non-specialist reader — a board, a journalist, a
  taxpayer — without dumbing the claim down.
- The stakes made vivid and concrete; one image or example beats three
  abstractions.
- No jargon, no acronyms beyond the project's own, no hedging stack.
- Usually a portal field rather than part of the PDF; keep it versioned with
  the proposal anyway.

## Reporting rules

- The acronym used consistently everywhere — proposal, budget, CV, annexes.
- Figures and tables numbered and referenced in the text; a Gantt chart and an
  objectives-to-WP map are worth their space, decorative diagrams are not.
- Page and font limits from `.grantstack/call-spec.md` treated as hard gates;
  trim content rather than shrinking margins.
- Every number that appears twice — budget total, duration, number of hires,
  objective count — agreeing everywhere it appears.
- Citations only from `proposal/refs.bib`.

## Complaints panels make most, by section

| Section | Complaint |
|---|---|
| Synopsis | Could not follow the central claim; ambition buried under background; no "why now" |
| State of the art | Reads as a literature review; gap asserted rather than shown; closest competitor not engaged |
| Objectives | Not falsifiable; no success criteria; really three separate projects |
| Methodology | Legible to no one; method not tied to objective; no evidence the applicant can do it |
| Feasibility | Risks listed without fallbacks, or no risks at all; timeline ignores hiring |
| Work packages | An objective with no WP; milestones that are not decisions; Gantt longer than the grant |
| Team and resources | Roles without WPs; supervision load implausible; host advantage unstated |
| Budget | Lines that buy no science; arithmetic that does not sum; over the ceiling |
| Impact | Audiences with no activities; no timing, no cost, no responsibility |
| Track record | A CV dump; independence unevidenced; metrics where the call bars them |
