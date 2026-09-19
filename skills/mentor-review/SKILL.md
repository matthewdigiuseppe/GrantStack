---
name: mentor-review
description: Gives the honest read from an ally — a funded PI, a grants officer, or a respected generalist — leading with the single highest-value change, then the strengths to protect and a prioritized fix list. Use on a near-complete draft, alongside the adversarial mock review, when the user wants the truths a reviewer will not bother to tell them.
argument-hint: "[senior-pi|grants-officer|field-elder]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(date *)
  - Bash(wc *)
---

# /grantstack:mentor-review

**Stage:** stress-test · **Voice:** mentor — on your side, but unsparing

Where `/grantstack:panel-mock` simulates the adversary, this simulates the ally: the senior colleague or grants officer who reads it wanting you to succeed. Different lens, different catches.

`$ARGUMENTS` selects the persona, defaulting to `senior-pi`:

- `senior-pi` — a funded PI in your broad area; focuses on whether the ambition and the case for *you* are pitched right.
- `grants-officer` — institutional research support; focuses on compliance, eligibility, host commitment, and submission logistics.
- `field-elder` — a respected generalist; focuses on whether the framing will land with a panel, and where you are being tone-deaf to the field.

## Procedure

1. **Load** every file in `proposal/sections/`, `cv/track-record.md`, `budget/budget.md`, `.grantstack/config.yaml`, `.grantstack/call-spec.md`, prior reviews in `.grantstack/review-cache/`, and — for tone and structure — `voice.reviewer_style` if it names an installed skill, otherwise `${CLAUDE_PLUGIN_ROOT}/references/panel-report-conventions.md`.
2. **Read as the ally.** The mentor's questions are not the reviewer's:

   | Persona | Asks |
   |---|---|
   | `senior-pi` | Is the ambition pitched at the right altitude for this scheme? Are you underselling yourself? Is the bold core actually bold, or sanded down to feel safe? |
   | `grants-officer` | Are you eligible beyond doubt? Is the host visibly committed? Are the annexes and budget compliant? What will trip the submission system at 23:59? |
   | `field-elder` | Will the panel's framing of the field match yours? Are you ignoring someone who might be in the room? Is the tone confident or arrogant? |

3. **Give the honest read.** Lead with the single most valuable change — the thing that, fixed, most improves the odds. Then the strengths to protect, so revision does not sand off what is working. Then the concrete fixes, ranked. Mentors prioritize; they do not list everything equally.
4. **Be specific and kind but firm.** "This is good" helps no one; "your synopsis buries the breakthrough in paragraph three — a panel may not reach it; move it to sentence one" helps.
5. **Save** to `.grantstack/review-cache/mentor-<persona>-<YYYY-MM-DD>.md` (date from `date +%F`), opening with the **Recommendation** line — the one highest-value change, in one sentence — so it is the first thing read. Set `grant.status: "review"` in `.grantstack/config.yaml` if it still says `writing`.

## Outputs

- `.grantstack/review-cache/mentor-<persona>-<date>.md`.
- Summary block: the one highest-value change, the strengths to protect, and the prioritized fix list.

## Anti-patterns

- **Cheerleading.** An ally who only praises is useless; the kindest read is an honest one.
- **A flat list with no priority.** The mentor's value is judgement about what matters most. Rank.
- **Duplicating the panel.** If this just reproduces `/grantstack:panel-mock`, it adds nothing — focus on what a well-meaning insider sees that a reviewer will not say.

## Next

Pair with `/grantstack:panel-mock` (adversary plus ally is full coverage); `/grantstack:feasibility-audit` if internal inconsistencies were flagged, `/grantstack:call-spec audit` if compliance was.
