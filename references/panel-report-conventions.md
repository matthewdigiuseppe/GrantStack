# Panel- and referee-report conventions (GrantStack fallback)

Built-in fallback for `/grantstack:panel-mock` and `/grantstack:mentor-review`.
If the user has a reviewer-style skill installed (named in
`.grantstack/config.yaml` → `voice.reviewer_style`), that skill wins — this
file keeps the mock review credible without it. Also read by
`/grantstack:rebuttal` and `/grantstack:retro`, which need to *read* a real
report rather than write one.

Criteria and scoring vocabulary per scheme live in `schemes.md`; this file is
about the shape, tone, and failure modes of the report itself.

## Who writes what

- **The generalist panel member** writes short, decisive comments on the whole
  proposal after reading the synopsis hardest. Their comment is often three or
  four sentences and it is what kills or saves the application. They are
  literate, senior, and not in the subfield; they will not ask for
  clarification, they will simply mark down what they could not follow.
- **The in-field remote referee** writes a longer report — a page or two —
  prosecuting novelty, rigour, and feasibility, in the register of a journal
  referee report. At ERC they write only for proposals that reach step 2; at
  NWO their reports are what the applicant rebuts.
- **The panel as a body** produces the consolidated comments the applicant
  eventually sees: a paragraph or two per criterion, negotiated, blunter than
  any individual would be, and frequently the only feedback on record.

## Structure of a report

1. **Summary** (one paragraph). A neutral restatement of the ambition, the
   approach, and what the applicant claims will change — in the reviewer's
   words, not the synopsis's. Its job is to expose, implicitly, any gap
   between what the proposal claims and what it has shown.
2. **Strengths** (2–4). Specific and genuine. A report with no strengths reads
   as hostile and gets discounted by the panel.
3. **Weaknesses / major concerns** (3–6). The issues that move the proposal
   below the funding line. Each names what the problem is, why it matters for
   the ambition or the deliverability, and — for a referee report the applicant
   may rebut — what would resolve it.
4. **Minor points** (5–12). Clarity, missing detail, presentation, an
   unexplained cost line.
5. **Per-criterion assessment and an overall standing** in the scheme's own
   vocabulary, relative to the funding line. The standing must be consistent
   with the concerns: three unresolved feasibility problems and a top mark
   cannot coexist.

## Tone

- Professional and direct; critique the proposal, never the applicant's
  character or career. "The applicant has not shown" is fair; "the applicant
  is not ready" is a judgement a panel makes but a report states through
  evidence.
- One sentence of genuine calibration ("the question is well chosen", "the
  data access is unusually good") is useful; a paragraph of compliments before
  each criticism is noise and reads as padding.
- Confidence proportional to expertise: a generalist flags rather than
  adjudicates a methodological dispute, and says so.

## Specificity

- Every substantive comment cites its target: section, page, work package,
  objective, or budget line. "The impact section is weak" is not a comment;
  "the knowledge-utilisation section names audiences but no activity, timing,
  or cost, so criterion 3 is not evidenced (p. 12)" is.
- Distinguish must-fix from suggestion explicitly, so the applicant can triage
  a rebuttal that has a word limit.

## The idioms that decide grants

These phrases recur because they encode the two structural tensions, and a
mock review that never produces one is not reading as a panel does:

- **"Excellent but not ground-breaking."** The commonest way a strong proposal
  dies: competent, publishable, incremental. It is a verdict about *ambition*,
  and it is answered with a discontinuity, not with more rigour.
- **"Exciting but not feasible."** The mirror image: bold with no credible
  plan, no fallback, no evidence the applicant can deliver it. Answered with
  risk register and track record, not with hedged ambition.
- **"The applicant does not convince me they are the person to do this."** The
  person half of the score, failing. Answered in the track record, not in the
  methodology.
- **"I could not follow the central claim."** Almost always a generalist, and
  almost always fatal, because the panel member who cannot follow it will not
  champion it in the room.

## Reading a report in order to answer it

For `/grantstack:rebuttal` and `/grantstack:retro`:

- **Separate the correctable from the structural.** A misreading you can
  answer with a pointer, a real gap you can fill in the revision, and a
  disagreement about what the field needs are three different things and only
  the first two are worth rebuttal words.
- **A misreading is still your fault.** If two referees misread the same
  passage, the passage is the problem; say so and fix it rather than arguing.
- **Count what recurs.** A concern raised by one referee is an opinion; the
  same concern from two is the panel's view of the proposal.
- **Never concede the ambition to placate a referee.** Sanding down the bold
  core to answer a feasibility complaint produces a proposal that is now
  neither ground-breaking nor, in the panel's eyes, worth the money. Defend the
  core with a fallback instead.
