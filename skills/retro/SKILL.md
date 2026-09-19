---
name: retro
description: Runs the post-decision retrospective — the timeline, where the mock reviews predicted the real ones and where you were blindsided, which criticisms recurred, and what to systematize — then calls resubmit or retarget. Use after the outcome is known, funded or not; the reviews are the most honest signal you will get about your profile and framing.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(date *)
  - Bash(python3 *)
  - Bash(git log *)
---

# /grantstack:retro

**Stage:** reflect · **Voice:** coach

Big-grant writing is a multi-year, multi-attempt game, so the value of a retrospective compounds. A rejection's reviews are the most honest signal you will get.

## Procedure

1. **Load the record.** Run `python3 "${CLAUDE_PLUGIN_ROOT}/bin/grantstack-status"` for the dated artifact table rather than opening every memo, and `git log --reverse --date=short --format='%ad %s'` if the folder is a git repo. Then read `reviews/received/*` (the reports as they arrived), `reviews/rebuttal/*`, `.grantstack/review-cache/*`, and the `decisions:` list in `.grantstack/config.yaml`.
2. **Ask the outcome** if it is not already clear — funded, rejected, or still pending — and do not guess it from the files.
3. **Reconstruct the timeline.** When each stage happened, the longest pole, where time evaporated. The track-record narrative and the host letter are the usual sinks.
4. **Compare predicted against actual.** Where did `/grantstack:panel-mock` and `/grantstack:mentor-review` anticipate the real referees, and where were you blindsided? The gaps are where your self-assessment is weak, and that is the most useful finding in the document.
5. **Separate signal from noise.** Which criticisms recurred across referees (signal) and which were one-off (noise)? Which were about the project, which about the person, which about framing? Be honest about which are fixable and which are about timing or profile. Even an unfair review contains a signal about how the proposal reads.
6. **Extract systematizable lessons** — what you would template, start earlier, or do differently regardless of this project. "Start earlier" is not a lesson; "draft the track-record narrative in month 1, not week −2" is.
7. **Write `.grantstack/retro.md`**: the verdict line, then timeline, predicted-versus-actual, review signal, and lessons.

   **Verdict:** **Funded — lessons**, **Resubmit**, or **Retarget**, with a one-line reason.

   Set `grant.status` to `funded` or `rejected` in `.grantstack/config.yaml` per the outcome the user gave, if it still says `submitted`, `rebuttal`, or `interview`.

## Outputs

- `.grantstack/retro.md` — verdict, timeline, predicted-versus-actual, signal, lessons.
- Summary block: the top three lessons, the biggest blind spot the reviews exposed, and the resubmit-or-retarget call.

## Anti-patterns

- **Blaming the reviewers.** Even an unfair review says something about how the proposal reads; find it.
- **Lessons too vague to act on.**
- **Skipping the retro after a win.** Funded proposals teach what worked; capture it before you forget.

## Next

`/grantstack:resubmit` if the verdict is resubmit; `/grantstack:learn` to persist the per-proposal lessons, and your global memory for the ones that cross proposals.
