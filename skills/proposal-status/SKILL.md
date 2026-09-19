---
name: proposal-status
description: Reports where a proposal stands from its .grantstack/ memory and the files on disk — stage, missing artifacts, stale reviews and audits, and the one recommended next skill. Use when the user asks where they left off or what's next, wants a status check, or opens a session on an existing proposal.
allowed-tools:
  - Bash(python3 *)
  - Read
  - Grep
  - Glob
  - Edit
---

# /grantstack:proposal-status

**Stage:** any · **Voice:** project-manager

Opening a session, returning after a gap, "where were we?", "what's next?", "how far off is this from submittable?". Read-only apart from an offered `grant.status` correction.

## Procedure

1. **Inventory in one call:**

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/bin/grantstack-status"
   ```

   It finds `.grantstack/` at or above the current directory (exit 1 and a pointer to `/grantstack:grantstack-init` if there is none), reads `.grantstack/config.yaml`, and prints: every artifact by stage with its state (present / thin / stub / missing / optional), date, and verdict line, where `thin` means the file exists but is too small or too repetitive to be a real artifact of its kind; the artifacts that are stale because an input changed after they were written (a panel-mock older than the sections it reviewed, a feasibility audit older than the budget, a call spec older than the call in `admin/call/`, reports in `reviews/received/` that no rebuttal or retro answers); the stage the artifacts imply; whether that matches `grant.status`; the required artifacts still missing; and its own next-step recommendation. Do not re-derive any of this with your own globs and greps.
2. **Spot-check what the verdict rests on.** Open every artifact the script marks `thin`, and the one `present` artifact that anchors the derived stage (the furthest one). If any is placeholder text, say so and derive the stage yourself from the last real artifact; the script's heuristics are size and repetition, and your reading beats them.
3. **Reconcile `grant.status`.** If the script's derived stage, or your corrected one, disagrees with config, say so and offer to update the field in `.grantstack/config.yaml`; never change it unasked. Config *ahead* of the folder is normal and not an error — an invited applicant sets `interview` before the prep exists — and the script already works to the later of the two.
4. **Recommend exactly one next step:** the earliest required gap wins over a shinier later stage, and a stale verdict counts as a gap. Name the skill and the reason in one sentence. When `grant.status` is `resubmitting`, the next step is instead the first unfinished item in `.grantstack/resubmit-plan.md`.

## Outputs

A printed report, in this order, and nothing written to the proposal folder:

1. **The config line** as the script prints it: acronym or title, `grant.status`, scheme, deadline, budget, format.
2. **Bottom line, four short sentences (under 80 words):** the stage and whether it matches `grant.status`; what is stale (an input changed after it was written; a placeholder is a gap, not a stale artifact); the one next skill and why. If the deadline is close, say how close.
3. **One per-stage table**, the script's rows with your spot-check corrections already applied (state, date, verdict or a short note). One table is the inventory; do not paste raw script output and then re-summarize it.
4. **Only what changes the next step:** a placeholder you found behind a `present` or `thin` label, a mismatch to correct. Observations that do not change the recommendation stay out.

Write for the applicant, not about the process: no "the script says", no state-versus-correction columns, no mention of which heuristic decided what. Report the corrected state and, where you overrode the script, one short note in the row.

With consent only: `grant.status` corrected in `.grantstack/config.yaml`.

## Anti-patterns

- **Guessing the stage from the conversation.** The artifacts on disk are the record, and the script reads them.
- **Three next steps.** One; the lifecycle is ordered for a reason.
- **A stub counted as done.** The script strips template comments before deciding; trust its `stub` state, open anything it calls `thin`, and spot-check the artifact the stage rests on.
- **A report longer than the proposal's problems.** Bottom line, one table, then only what changes the next step.
