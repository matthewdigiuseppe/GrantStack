---
name: retro
description: Proposal retrospective after the outcome (funded or rejected) — what worked, what took longest, what to systematize for next time, and what the reviews actually told you. Writes .grantstack/retro.md. Analog to MStack's /retro.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(date *)
  - Glob
---

# /grantstack:retro

**Stage:** reflect
**Voice:** coach

## When to invoke

After the decision, funded or not. Big-grant writing is a multi-year, multi-attempt game; the value of a retrospective is compounding. Reviews — especially of a rejection — are the most honest signal you'll get about your profile and framing.

## Procedure

1. **Load.** `.grantstack/config.yaml` (status, scheme), the referee reports and `reviews/`, `.grantstack/review-cache/*`, `.grantstack/decisions.log`, and the outcome.

2. **Reconstruct the timeline.** When did each stage happen, what was the longest pole, where did time evaporate? (Track record narrative and letters are common time sinks.)

3. **Compare predicted vs. actual review.** Where did `/panel-mock` and `/mentor-review` correctly anticipate the real referees, and where were you blindsided? The gaps are where your self-assessment is weak — the most useful finding.

4. **Separate signal from noise in the reviews.** Which criticisms recurred across referees (signal) vs. one-off (noise)? Which were about the project, which about the person, which about framing? Be honest about which are fixable and which are about timing/profile.

5. **Extract systematizable lessons.** What would you template, start earlier, or do differently regardless of this project? These are candidates for `/learn` (per-proposal) or your global memory (across proposals).

6. **Write `.grantstack/retro.md`**: timeline, predicted-vs-actual, review signal, lessons, and — if rejected — a one-line read on whether this is a resubmit (→ `/resubmit`) or a retarget.

## Outputs

- `.grantstack/retro.md`.
- Summary block: the top 3 lessons, the biggest blind spot the reviews exposed, and the resubmit/retarget call.

## Anti-patterns to refuse

- **Blaming the reviewers.** Even an unfair review contains a signal about how the proposal reads. Find it.
- **Lessons too vague to act on.** "Start earlier" → "draft the track-record narrative in month 1, not week -2."
- **Skipping retro after a win.** Funded proposals teach what worked; capture it before you forget.

## When to call other skills

- After (if rejected and resubmitting): `/resubmit`.
- Throughout: `/learn` to persist per-proposal lessons; promote cross-proposal lessons to global memory.
