# Scheme reference: ERC and NWO Talent

Read by `/grantstack:grant-fit`, `/grantstack:call-spec`,
`/grantstack:scope-challenge`, `/grantstack:budget`, `/grantstack:panel-mock`,
`/grantstack:interview-prep`, `/grantstack:rebuttal`, `/grantstack:admin-pack`,
and `/grantstack:resubmit`.

> **The call is the contract.** Everything in this file is background: how the
> schemes are *shaped*, so a skill knows what to ask and what a panel is for.
> Every number here — eligibility windows, ceilings, durations, page limits —
> moves between work programmes and calls, and some move between domains within
> one call. Treat them as order of magnitude only, and confirm against the
> actual call captured in `.grantstack/call-spec.md`. Where this file and the
> call disagree, the call wins and this file is wrong.
>
> Figures below were checked against the 2026 ERC Work Programme and the 2026
> NWO Talent calls. Structural facts (who interviews, who grants a right of
> reply) are far more stable than figures, but even they are worth a glance at
> the call.

## ERC (European Research Council)

One criterion: **excellence**, applied jointly to the research project and the
Principal Investigator. There is no separate impact criterion and no
consortium; the PI and the idea carry the whole application.

| | Starting | Consolidator | Advanced |
|---|---|---|---|
| Since PhD | ~2–7 years | ~7–12 years | no window; an established leader with a ~10-year track record |
| Typical ceiling | ~€1.5M | ~€2M | ~€2.5M |
| Typical duration | up to 5 years | up to 5 years | up to 5 years |
| Additional funding | on top of the ceiling, for start-up costs on moving to the EU/AC, major equipment, or access to large facilities | same | same |
| Interview | yes (step 2) | yes (step 2) | no |

**Eligibility windows** are counted from the date of PhD award to a fixed
reference date in the call, and are **extendable** — parental leave (a fixed
period per child), long-term illness, national service, and clinical training
are the usual grounds, each with its own evidence requirement. An applicant
outside the window on the raw date may well be inside it once extensions are
applied, which is why `/grantstack:grant-fit` asks for `pi.eligibility_notes`
rather than computing from `pi.phd_year` alone. Holding or having held another
ERC grant restricts which scheme you may apply to and when.

**Two-step evaluation.**

- **Step 1** — the panel (a domain panel: SH1–SH7 for social sciences and
  humanities, plus the LS and PE domains) reads **B1**: the extended synopsis
  plus the CV and track record. Most proposals are rejected here, by panel
  members who are *not* in the applicant's subfield. This is why the synopsis
  is the most consequential page in the proposal.
- **Step 2** — the panel plus **remote referees** in the subfield read **B2**,
  the full scientific proposal. StG and CoG applicants are then **interviewed**
  by the panel in Brussels or online; AdG has no interview.

**Scores** are A (meets the excellence criterion fully; recommended for
funding if budget allows), B (meets it in some but not all respects — above
the quality bar but not funded), and C (does not meet it). A B at step 2 is
the near-miss most resubmissions come from.

**Feedback and the absence of a rebuttal.** ERC gives applicants **no right of
reply**. The evaluation report — panel comments, plus the remote referees'
comments for proposals that reached step 2 — arrives **with the final
decision**, after the interview, not before it. So an ERC interview is a pitch
and a defence of the proposal as written, never a response to reports the
applicant has read. The reports feed `/grantstack:retro` and
`/grantstack:resubmit`, not `/grantstack:rebuttal`.

**Resubmission restrictions** exist and depend on the score and the step at
which it was given: a low score can bar the applicant from the next call, or
from the next two. The exact mapping changes between work programmes — read it
in the call before planning a resubmission, because it sets the earliest date
the next attempt can exist.

**Budget structure.** Direct costs (personnel including the PI's own time,
equipment, consumables, travel, publication and dissemination, subcontracting
within a cap) plus a flat-rate indirect-cost allowance. Additional funding, if
requested, is justified separately from the main budget and does not compete
with it.

## NWO Talent (Veni, Vidi, Vici)

Three criteria, weighted per call: the **quality of the researcher**, the
**quality of the research proposal**, and **knowledge utilisation** — the last
is a scored criterion in its own right, not a formality, which is the single
biggest structural difference from ERC and the reason
`/grantstack:impact` is required for NWO proposals.

| | Veni | Vidi | Vici |
|---|---|---|---|
| Since PhD | ~within 3 years | ~within 8 years | ~within 15 years |
| Typical ceiling | ~€320k | ~€800k | ~€1.5M |
| Typical duration | 3 years | 5 years | 5 years |
| Aimed at | a promising researcher just after the PhD | an experienced researcher building a group | a senior researcher building or renewing a group and a line of research |

Windows are counted to a reference date in the call and extended for care
leave, illness, and other grounds on the same logic as ERC. Domains (ENW, SGW,
ZonMw, AES, and the round's own arrangements) differ in deadlines, sometimes
in the process, and in how the embedding-institution nomination works —
several rounds cap how many candidates an institution may put forward, which is
an internal deadline months before NWO's.

**The process, and the rebuttal.** Most rounds run a **pre-proposal** stage
(routine for Vidi and Vici; per-domain for Veni): a short application, often
the synopsis and the CV, that decides who is invited to write the full
proposal. The full proposal goes to **external referees**; the applicant then
gets the referee reports and writes a **rebuttal** — a written right of reply,
with a tight word limit and a short turnaround. The committee reads proposal,
reports, and rebuttal together, and shortlisted applicants are **interviewed**.
So for NWO the reports *are* read before the decision, the rebuttal is a real
document with its own stage, and `/grantstack:rebuttal` applies.

A pre-proposal and full proposal live in the **same proposal folder**: the
synopsis and track record serve the pre-proposal, the rest is written once
invited, and `/grantstack:admin-pack` builds a checklist for whichever part is
due. Record "pre-proposal submitted <date>" in `decisions:` in
`.grantstack/config.yaml`.

**CV rules.** NWO applies narrative-CV rules and, as a DORA signatory, bars
journal impact factors, h-indices, and similar metrics from the CV; the case
for the researcher is made in prose about contribution and its significance.
Writing a metrics-led CV for an NWO committee is a self-inflicted wound. See
`proposal-conventions.md` for what to write instead.

**Budget structure.** Modular: personnel positions at standard rates, plus
material, investment, knowledge-utilisation, and (per scheme) money for the
applicant's own time or replacement teaching. The modules and their caps are
per call — read them before costing anything.

## Other investigator-led schemes

The GrantStack spine (frame → position → design → write → stress-test →
submit → defend → reflect) transfers to ANR JCJC, DFG Emmy Noether and
Heisenberg, UKRI Future Leaders Fellowships, SNSF Starting Grants, and similar
single-PI schemes. What transfers structurally: a two-reader audience, an
ambition-versus-feasibility tension, a person-plus-project score, and usually
an interview. What does not transfer: everything numeric, the criteria
weights, and whether there is a right of reply. Set `grant.scheme: "other"`,
run `/grantstack:call-spec capture` early, and let the captured spec carry the
rules.
