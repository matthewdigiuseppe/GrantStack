---
name: resubmit
description: Plans a resubmission after rejection — diffs the proposal against the reviews, decides what to overhaul vs. defend, checks resubmission eligibility/embargoes, and sequences the rework. Most funded big grants are resubmissions; this turns a rejection into the next attempt. Writes .grantstack/resubmit-plan.md.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(date *)
  - Glob
  - Grep
---

# /grantstack:resubmit

**Stage:** reflect
**Voice:** strategist (the colleague who got funded on attempt two or three)

## When to invoke

After a rejection you intend to fight. A large share of funded ERC/NWO grants are resubmissions — rejection is a stage, not a verdict. But a naive resubmission that ignores the reviews, or over-corrects and guts the ambition, fails again. This skill plans the rework deliberately.

## Procedure

1. **Load.** `.grantstack/retro.md`, the referee reports, `reviews/`, the full proposal, and `.grantstack/config.yaml` (scheme).

2. **Check resubmission rules first.** Some schemes impose embargoes after low scores (e.g., an ERC bottom-tier score can bar resubmission for one or two calls; NWO has its own re-application rules). Confirm against the current call — flag for verification rather than asserting a rule. If barred for a cycle, plan accordingly (retarget, or strengthen the profile in the gap year).

3. **Diff proposal against reviews.** For each recurring criticism (from `/retro`'s signal analysis), decide:
   - **Overhaul** — a fair, fixable weakness (unclear ambition, thin feasibility, weak impact). Plan the specific rework.
   - **Defend / reframe** — a misunderstanding or a framing failure. The fix is usually clarity, not capitulation — make the strength impossible to miss.
   - **Hold** — a difference of judgment where you're right and the science backs you. Don't chase every reviewer.

4. **Guard the ambition.** The classic resubmission failure is sanding off the bold core to dodge the "too risky" comment, producing a safe proposal that loses to a bold one. Strengthen feasibility and fallback instead. State explicitly what must *not* change.

5. **Decide the magnitude.** Light-touch revision vs. substantial reframe vs. new framing of the same science (→ `/idea-shotgun`). Recurring ambition criticism usually means reframe, not tweak.

6. **Sequence the rework.** An ordered plan mapping each change to the skill that does it (`/groundbreaking-test`, `/methodology`, `/impact`, `/track-record`, etc.), front-loading the highest-leverage changes, with the next deadline as the anchor.

7. **Write `.grantstack/resubmit-plan.md`** and update `config.status` to `resubmitting`.

## Outputs

- `.grantstack/resubmit-plan.md` — eligibility check, change decisions (overhaul/defend/hold), the protected core, and the sequenced rework.
- Summary block: resubmission eligibility status, the 3 highest-leverage changes, and what must not change.

## Anti-patterns to refuse

- **Resubmitting unchanged.** If nothing changes, the result won't.
- **Gutting the ambition to please the cautious referee.** Defend the bold core; fix feasibility instead.
- **Chasing every comment.** Hold the ones where you're right; over-correction is its own failure.
- **Asserting embargo rules from memory.** Confirm against the current call.

## When to call other skills

- Before: `/retro` (its signal analysis feeds the diff).
- During: whichever stage skills the change plan calls for; `/idea-shotgun` if a full reframe is warranted.
- After: `/call-spec` again (rules may have changed for the new call).
