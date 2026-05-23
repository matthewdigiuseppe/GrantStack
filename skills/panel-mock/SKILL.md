---
name: panel-mock
description: Generates a mock evaluation of the proposal in the voice of a real review panel — a generalist panel member, an in-field remote referee, or a skeptic — scored to the scheme's criteria. Front-runs the actual panel so problems surface pre-submission. Wraps grant-reviewer-style. Writes to .grantstack/review-cache/. The grant analog to MStack's /referee-mock.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(date *)
  - Glob
  - Grep
---

# /grantstack:panel-mock

**Stage:** stress-test (pre-submission)
**Voice:** reviewer (anchored to `grant-reviewer-style`)

## When to invoke

When the proposal sections exist and it's "submission-ready." This is your last line of defense before the real panel. Run it more than once with different personas — proposals are killed by the reader you didn't simulate.

## Argument

`$ARGUMENTS` (optional) — reviewer persona:
- `generalist` (default) — a panel member **not in your subfield**. Reads the synopsis and lay summary hardest. Decides funding. The reader most applicants under-serve.
- `expert` — the in-field remote referee. Reads methodology and state-of-art deeply; prosecutes rigour, feasibility, and whether it's truly beyond the state of the art.
- `skeptic` — the incremental-skeptic who defaults to "excellent but not ground-breaking" and looks for the reason to rank you below the funding line.
- `editor` / `chair` — prosecutes fit to the scheme, balance of person-vs-project, clarity, and whether each weighted criterion is visibly met.

If unrecognized, default to `generalist`.

## Procedure

1. **Load the proposal.** All `proposal/sections/*`, `cv/track-record.md`, `budget/budget.md`, `.grantstack/config.yaml` (scheme), and `.grantstack/call-spec.md` (the **evaluation criteria and weights** — the review must score against these, not generic taste).

2. **Load prior mock reports** in `.grantstack/review-cache/`. If this persona reviewed an earlier draft, note explicitly what improved and what didn't.

3. **Invoke the reviewer voice.** Use `grant-reviewer-style` for the tone and structure of a panel report; honor `voice.reviewer_style` if overridden in config.

4. **Review with the persona's bias dialed in:**

   | Persona | Presses hardest on |
   |---|---|
   | `generalist` | Is the synopsis legible and exciting to a non-expert? Is the ambition obvious? Does the jargon lose me? Would I champion this in the room? |
   | `expert` | Rigour, feasibility of the methods, command of the literature, genuine novelty vs. the state of the art, the realism of the risk plan |
   | `skeptic` | Is this actually ground-breaking or just very good? Where's the real high-risk/high-gain bet? Why fund this over the next proposal? |
   | `editor`/`chair` | Scheme fit, person↔project balance, every weighted criterion addressed (esp. impact / knowledge utilisation), clarity, page-budget discipline |

5. **Score to the scheme.** Use the call's actual criteria and weights from `call-spec`. Give a per-criterion assessment and an overall standing relative to the funding line (e.g., for ERC-style: roughly A / B / C; for NWO: per-criterion qualitative + fund/no-fund call). Be the reviewer you fear, not the one you hope for.

6. **Report structure:**
   - **Summary** (1 para): what the project claims and proposes.
   - **Strengths** (2-4): genuine, specific.
   - **Major concerns** (3-6): the issues that move it below the line if unaddressed. Cite the section/page.
   - **Minor concerns** (5-12): clarity, gaps, presentation, missing detail.
   - **Per-criterion scores** + **overall recommendation** relative to the funding line.

7. **Save** to `.grantstack/review-cache/panel-mock-<persona>-<YYYY-MM-DD>.md` with a header: persona, scheme, panel, draft word count or commit hash, date.

## Outputs

- `.grantstack/review-cache/panel-mock-<persona>-<date>.md`.
- Summary block: top 3 major concerns, the per-criterion standing, the overall call, and a prompt to run the persona you haven't run.

## Anti-patterns to refuse

- **Sycophancy.** "Strong proposal, fund it" with no major concern fails the user. If you can't find a major concern, you're not reading as the panel will.
- **Generic comments.** "Strengthen the impact" is useless; cite the section and say how it falls short of the criterion.
- **Scoring on personal taste instead of the call's criteria.** Use the weights in `call-spec`.
- **Speaking outside the persona.** A `generalist` doesn't critique a clustering algorithm; a `skeptic` doesn't praise.

## When to call other skills

- After a `Major concerns` or below-line verdict: `/feasibility-audit`, `/groundbreaking-test`, or `/impact` depending on where it fell short.
- Once revised: re-run with a different persona to triangulate.
- Before the real interview: `/interview-prep` (the mock major-concerns become interview questions).
