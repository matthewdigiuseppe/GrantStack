---
name: panel-mock
description: Writes a mock evaluation in the voice of a real reviewer — generalist panel member, in-field referee, incremental skeptic, or panel chair — scored against the call's own criteria and weights, with major concerns that cite the section. Use when the proposal is near submission-ready, or when the user wants to know how a panel will react before the panel does.
argument-hint: "[generalist|expert|skeptic|chair]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(date *)
  - Bash(wc *)
  - Bash(git rev-parse *)
---

# /grantstack:panel-mock

**Stage:** stress-test · **Voice:** reviewer, anchored to `voice.reviewer_style` in `.grantstack/config.yaml`

Your last line of defence before the real panel, and the fast one: **one** reviewer, one report. When you want the whole room — several reviewers reading blind and then arguing with each other — use `/grantstack:panel-convene` instead. Run this more than once with different personas: proposals are killed by the reader you did not simulate.

`$ARGUMENTS` selects the persona, defaulting to `generalist` (also the fallback for an unrecognized value):

- `generalist` — a panel member **not in your subfield**, who reads the synopsis and lay summary hardest and decides funding. The reader applicants most under-serve.
- `expert` — the in-field remote referee, who reads methodology and state-of-the-art deeply and prosecutes rigour, feasibility, and genuine novelty.
- `skeptic` — the incremental-skeptic who defaults to "excellent but not ground-breaking" and looks for the reason to rank you below the line.
- `chair` (or `editor`) — prosecutes scheme fit, the person-versus-project balance, clarity, and whether every weighted criterion is visibly met.

## Procedure

1. **Load the proposal in full:** every file in `proposal/sections/`, `cv/track-record.md`, `budget/budget.md`, `.grantstack/config.yaml`, and `.grantstack/call-spec.md` — the **evaluation criteria and weights** the review must score against, rather than generic taste. Load prior reports in `.grantstack/review-cache/`; if this persona reviewed an earlier draft, say explicitly what improved and what did not.
2. **Reviewer voice.** If `voice.reviewer_style` names an installed skill, use it for voice, tone, and structure; otherwise `${CLAUDE_PLUGIN_ROOT}/references/panel-report-conventions.md`.

   **Persona ammunition.** `generalist`: the synopsis and lay-summary bars in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md` — press every place the claim stops being legible. `expert`: the methodology bar there plus `${CLAUDE_PLUGIN_ROOT}/references/feasibility-catalog.md`, and raise every contradiction the proposal has not closed. `skeptic`: the tests in the newest `.grantstack/groundbreaking-test-*.md`, and whether the proposal's own answers survive. `chair`: the scheme's criteria in `${CLAUDE_PLUGIN_ROOT}/references/schemes.md` and the complaints-by-section table in `proposal-conventions.md`.
3. **Review with the persona's bias dialed in:**

   | Persona | Presses hardest on |
   |---|---|
   | `generalist` | Is the synopsis legible and exciting to a non-expert? Is the ambition obvious? Does the jargon lose me? Would I champion this in the room? |
   | `expert` | Rigour, feasibility of the methods, command of the literature, genuine novelty against the state of the art, realism of the risk plan |
   | `skeptic` | Is this actually ground-breaking or just very good? Where is the real high-risk/high-gain bet? Why fund this over the next proposal? |
   | `chair` | Scheme fit, person↔project balance, every weighted criterion addressed (especially impact / knowledge utilisation), clarity, page discipline |

4. **Score to the scheme** using the criteria and weights in `call-spec.md`: a per-criterion assessment and an overall standing relative to the funding line, in the scheme's own vocabulary. Be the reviewer you fear, not the one you hope for.
5. **Write the report** in this structure: **Summary** (one paragraph, what the project claims and proposes, in your words); **Strengths** (2-4, genuine and specific); **Major concerns** (3-6, the issues that move it below the line, each citing the section); **Minor concerns** (5-12); **per-criterion assessment**; **overall standing**.
6. **Check your own recommendations against your findings.** A fix you recommend must not contradict a concern you raised elsewhere in the report — do not ask for a broader scope in one paragraph and warn about over-scoping in another. Reconcile before saving.
7. **Save** to `.grantstack/review-cache/panel-mock-<persona>-<YYYY-MM-DD>.md` (date from `date +%F`) with a header carrying persona, scheme, panel, date, and the draft's identity — `git rev-parse --short HEAD` in a git repo, otherwise a `wc -w` word count across `proposal/sections/`. Open with the **Recommendation** line so the standing is the first thing read. Set `grant.status: "review"` in `.grantstack/config.yaml` if it still says `writing`.

## Outputs

- `.grantstack/review-cache/panel-mock-<persona>-<date>.md`.
- Summary block: the top three major concerns, the per-criterion standing, the overall call, and a prompt to run the persona you have not run.

## Anti-patterns

- **Sycophancy.** "Strong proposal, fund it" with no major concern fails the user. If you cannot find a major concern, you are not reading as the panel will.
- **Generic comments.** "Strengthen the impact" is useless; cite the section and say how it falls short of the criterion.
- **Scoring on personal taste instead of the call's criteria.**
- **Speaking outside the persona.** A `generalist` does not critique a clustering algorithm; a `skeptic` does not praise.

## Next

Below the line → `/grantstack:feasibility-audit`, `/grantstack:groundbreaking-test`, or `/grantstack:impact`, depending on where it fell short. Once revised, re-run with a different persona to triangulate, or `/grantstack:panel-convene` to see where a full panel would split. Before the real interview, `/grantstack:interview-prep` turns the major concerns into questions.
