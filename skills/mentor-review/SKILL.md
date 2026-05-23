---
name: mentor-review
description: Simulated senior-mentor / grants-office critique of the whole proposal — the honest read from someone who wants you to win and has seen many funded and rejected. Configurable persona. Writes to .grantstack/review-cache/. Analog to MStack's /coauthor-review.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(date *)
  - Glob
  - Grep
---

# /grantstack:mentor-review

**Stage:** stress-test
**Voice:** mentor (on your side, but unsparing)

## When to invoke

On a near-complete draft, before or alongside `/panel-mock`. Where `panel-mock` simulates the adversary, this simulates the ally — the senior colleague or grants officer who reads it wanting you to succeed and tells you the truths a reviewer won't bother to. Different lens, different catches.

## Argument

`$ARGUMENTS` (optional) — mentor persona:
- `senior-pi` (default) — a funded PI in your broad area; focuses on whether the ambition and the case for *you* are pitched right.
- `grants-officer` — institutional research-support; focuses on compliance, eligibility, host commitment, and submission logistics.
- `field-elder` — a respected generalist; focuses on whether the framing will land with a panel and where you're being tone-deaf to the field.

If unrecognized, default to `senior-pi`.

## Procedure

1. **Load.** All `proposal/sections/*`, `cv/track-record.md`, `budget/budget.md`, `.grantstack/config.yaml`, `.grantstack/call-spec.md`, and prior reviews in `.grantstack/review-cache/`.

2. **Read as the ally.** The mentor's questions are different from the reviewer's:

   | Persona | Asks |
   |---|---|
   | `senior-pi` | Is the ambition pitched at the right altitude for this scheme? Are you underselling yourself? Is the bold core actually bold, or did you sand it down to feel safe? |
   | `grants-officer` | Are you eligible beyond doubt? Is the host visibly committed? Are the annexes and budget compliant? What will trip the submission system at 23:59? |
   | `field-elder` | Will the panel's framing of the field match yours? Are you ignoring someone who might be in the room? Is the tone confident or arrogant? |

3. **Give the honest read.** Lead with the single most valuable change — the thing that, fixed, most improves the odds. Then strengths to protect (don't let revision sand off what's working), then concrete fixes. Mentors prioritize; they don't list everything equally.

4. **Be specific and kind-but-firm.** "This is good" helps no one. "Your synopsis buries the breakthrough in paragraph three — a panel may not reach it; move it to sentence one" helps.

5. **Save** to `.grantstack/review-cache/mentor-<persona>-<YYYY-MM-DD>.md`.

## Outputs

- `.grantstack/review-cache/mentor-<persona>-<date>.md`.
- Summary block: the one highest-value change, the strengths to protect, and the prioritized fix list.

## Anti-patterns to refuse

- **Cheerleading.** An ally who only praises is useless. The kindest read is an honest one.
- **A flat list with no priority.** The mentor's value is judgment about what matters most. Rank.
- **Duplicating the panel.** This is the ally's lens; if it just reproduces `panel-mock`, it's adding nothing — focus on what a well-meaning insider sees that a reviewer won't say.

## When to call other skills

- Pair with `/panel-mock` (adversary + ally = full coverage).
- After: `/feasibility-audit` if the mentor flagged internal inconsistencies; `/call-spec audit` if compliance was flagged.
