---
name: resubmit
description: Plans the next attempt after a rejection — checks the resubmission embargo, diffs the proposal against the recurring criticisms, decides what to overhaul, defend or hold, names what must not change, and sequences the rework against the next deadline. Use after a rejection the user intends to fight; most funded big grants are resubmissions.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(date *)
---

# /grantstack:resubmit

**Stage:** reflect · **Voice:** strategist — the colleague who got funded on attempt two

Rejection is a stage, not a verdict. But a naive resubmission that ignores the reviews fails again, and so does one that over-corrects and guts the ambition.

## Procedure

1. **Load** `.grantstack/retro.md`, `reviews/received/*`, `reviews/rebuttal/*`, the full proposal, `.grantstack/config.yaml`, and the resubmission rules in `${CLAUDE_PLUGIN_ROOT}/references/schemes.md`.
2. **Check the embargo first.** Schemes restrict resubmission after low scores, and the mapping between score, step, and the number of calls barred changes between work programmes. Confirm it against the current call and flag it for verification rather than asserting it. If barred for a cycle, plan accordingly: retarget, or use the gap year to strengthen the profile.
3. **Diff the proposal against the reviews.** For each recurring criticism from the retro's signal analysis, decide:
   - **Overhaul** — a fair, fixable weakness (unclear ambition, thin feasibility, weak impact). Plan the specific rework.
   - **Defend / reframe** — a misunderstanding or a framing failure. The fix is clarity, not capitulation: make the strength impossible to miss.
   - **Hold** — a difference of judgement where the science backs you. Do not chase every reviewer.
4. **Guard the ambition.** The classic failure is sanding off the bold core to dodge "too risky", producing a safe proposal that loses to a bold one. Strengthen feasibility and the fallback instead, and state explicitly what must *not* change.
5. **Decide the magnitude:** light-touch revision, substantial reframe, or new framing of the same science. Recurring criticism of the ambition usually means reframe, not tweak.
6. **Sequence the rework** as an ordered plan mapping each change to the skill that does it — `/grantstack:groundbreaking-test`, `/grantstack:methodology`, `/grantstack:impact`, `/grantstack:track-record` — front-loading the highest-leverage changes, anchored to the next deadline.
7. **Write `.grantstack/resubmit-plan.md`**: the eligibility check, the change decisions, the protected core, and the sequenced rework as a checklist so `/grantstack:proposal-status` can read the next unfinished item. Set `grant.status: "resubmitting"` in `.grantstack/config.yaml` if it still says `rejected`, and append the decision to `decisions:`.

## Outputs

- `.grantstack/resubmit-plan.md` — embargo check, overhaul/defend/hold decisions, the protected core, the sequenced rework.
- Summary block: resubmission eligibility, the three highest-leverage changes, and what must not change.

## Anti-patterns

- **Resubmitting unchanged.** If nothing changes, the result will not.
- **Gutting the ambition to please the cautious referee.** Defend the bold core; fix feasibility instead.
- **Chasing every comment.** Hold the ones where you are right; over-correction is its own failure.
- **Asserting embargo rules from memory.** Confirm against the current call.

## Next

`/grantstack:call-spec recapture` — the new call may have changed the rules — then the stage skills the plan calls for, and `/grantstack:idea-shotgun` if a full reframe is warranted.
