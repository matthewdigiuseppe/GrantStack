# Panel composition: who is actually in the room

Read by `/grantstack:panel-convene`. Scheme mechanics — criteria, steps, who
interviews — live in `schemes.md`; the conventions of a written report live in
`panel-report-conventions.md`. This file is about **who the reviewers are** and
how to build a defensible simulation of a panel.

## The ethics, first

- **Never contact a reviewer.** The ERC states plainly that applicants,
  potential applicants, and host institutions must not contact panel members.
  Knowing who sits on a panel is public information; approaching them is
  misconduct. This plugin simulates a panel so you can anticipate it. It must
  never help you reach one.
- **A simulated panellist's opinion is an inference, never a person's view.**
  Where a simulation is grounded in a named individual's published work, the
  output says "a panellist whose published work emphasises X would press on Y",
  never "Professor X thinks Y". You are modelling a *type of reader* that the
  roster tells you is in the room, not ventriloquising a colleague.
- **Roster data stays in the proposal folder.** Fetch it, use it, leave it in
  `.grantstack/`. It is not plugin data and does not belong in a repository.
- **Say when the simulation is weaker than it looks.** An inferred year, a
  small sample, a panel composed from a description rather than a roster, or a
  run where blind reading could not be enforced — each is disclosed in the
  output. A confident-looking panel report built on a guessed roster is worse
  than no panel report.

## What the ERC publishes

The ERC publishes the membership of each evaluation panel, one document per
call per scheme, **after the evaluation round** — roughly a year's lag, so the
most recent competition's panel is typically not yet available when you are
writing for it. Chairs are marked.

The roster gives you **names, affiliations, and countries. It does not give you
disciplines, methods, or theoretical commitments.** The panel code carries the
broad field; everything finer has to be inferred from what those people have
published. That inference is the expensive step, and it is why the composition
pipeline samples rather than enumerates.

Panels sit in three domains — Physical Sciences and Engineering (PE), Life
Sciences (LS), Social Sciences and Humanities (SH) — with roughly 28 panels in
total and about 12–16 members plus a chair in each. **The structure moves:** the
2024 restructure added an eighth SH panel and redrew several boundaries. Never
work from a hardcoded list of panel codes; read the current call or the current
roster document.

Other funders differ. NWO publishes committee composition for some schemes and
not others, and often later. National agencies (ANR, DFG, UKRI, SNSF) vary from
full publication to none. Where nothing is published, compose from the call's
own description of the committee and say that is what you did.

## What actually varies between reviewers

A panel is not N interchangeable experts. The differences that change a verdict:

**Orientation** — the deepest split, and the one applicants most often fail to
anticipate:

| Orientation | Presses hardest on | Moved by |
|---|---|---|
| positivist | identification, measurement validity, whether the estimand answers the question, power | a falsification test, a pre-analysis plan, a sensitivity analysis |
| interpretive | whether the categories travel, what the coding erases, context stripped by aggregation | evidence of fieldwork depth, reflexivity about the instrument |
| critical | whose interests the framing serves, who is absent from the data, what the project naturalises | engagement with the critique rather than a citation gesturing at it |
| formal | whether the mechanism is derived or asserted, equilibrium logic, comparative statics | a stated model with its assumptions visible |
| historical | periodisation, the archive's silences, anachronism in the categories | source criticism, awareness of what the record cannot show |
| mixed | whether the components answer the same question | a clear division of labour between methods |

**Discipline** decides which literature the reviewer expects to see engaged, and
which omission reads as not knowing the field.

**Seniority and role.** A chair manages consensus and watches scheme fit and
the person-versus-project balance rather than prosecuting methodology. A
rapporteur owns the summary and is the member most likely to have read
everything. A junior-but-rising member is often the closest reader of the
methods.

**Dogmatism** — how readily a member updates when challenged. Every real panel
has someone who does not move; a simulation where everyone converges politely
is not simulating a panel.

## Composing a panel

1. **Field from the panel code**, not from the applicant's self-description.
   The panel the proposal is submitted to is the one that reads it, whether or
   not it is the natural home for the work — a proposal landing in the wrong
   panel is itself a finding worth reporting.
2. **Sample, do not enumerate.** Five or six members looked up properly beats
   sixteen looked up badly, and the point is the *distribution*, not a census.
   State the sample size in the output.
3. **Preserve the distribution, not the individuals.** If the sample is three
   quantitative, two interpretive, one formal, build a panel in those
   proportions. This is what makes an archetype panel defensible: the mix is
   evidence, the individuals are not.
4. **Always seat the chair**, and always seat at least one member whose
   orientation is furthest from the applicant's own. The reviewer you find
   least congenial is the one the simulation exists to surface.
5. **Spread the dogmatism.** A uniform panel converges falsely.

## Reading the result

The value is not the score. It is **where the panel splits**, because that
locates the work:

- Two positivists agreeing that the identification is weak is a **finding**.
- A critical theorist and a formal theorist disagreeing about whether the
  framing is the right one is a **structural split** — the applicant cannot
  satisfy both, and the question is which of them the real panel has more of.
- A lone objection from the orientation furthest from the proposal is a **risk**
  rather than a verdict: it matters if that reviewer is the rapporteur, and
  much less if they are outnumbered.

An objection survives the meeting for one of four reasons, and they call for
different work: the proposal has the substance but does not show it (**rewrite**);
it lacks the content and needs new work (**rework**); the objection goes to the
core and only a different framing answers it (**reframe**); or it is a genuine
disciplinary disagreement no revision resolves (**unanswerable** — and then what
matters is how many such readers the real panel holds).
