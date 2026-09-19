---
name: careful
description: Toggles warn-before-destructive mode for this proposal — a GrantStack hook then requires confirmation before rm, git reset, force-push, or overwriting proposal, budget, CV, admin, or review files. Use near a deadline, after a major edit you don't want clobbered, or before letting Claude work autonomously on a proposal that is about to be submitted; run with argument off to disable.
argument-hint: "[off]"
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Edit
---

# /grantstack:careful

**Stage:** power · **Voice:** safety

A mechanism, not a promise: the `PreToolUse` hook (`hooks/grantstack-guard.py`) runs before every `Write`, `Edit`, and `Bash` call, and while `.grantstack/safety.yaml` has `careful: true` the actions below become confirmation prompts, even in a fresh session that never loaded this skill.

## Procedure

1. Read or create `.grantstack/safety.yaml` (default `careful: false`).
2. Set the top-level line `careful: true` (or `false` if `$ARGUMENTS` is `off`); the hook parses exactly this shape.
3. Tell the user what now prompts for confirmation:
   - `rm`, `git reset --hard`, `git checkout --`, `git clean -f`, force push, `sed -i`, `truncate`;
   - `mv` touching `proposal/`, `budget/`, `cv/`, `admin/`, or `reviews/`;
   - `Write` replacing an existing non-empty file under those directories, or any existing file of 100+ lines.
   Reads, greps, targeted `Edit`s, and writes to `.grantstack/` proceed normally; `admin/call/` and `reviews/received/` are read-only at all times, independent of this toggle.
4. Print the state: careful mode `<on|off>`, enforced by the GrantStack guard hook.

## Outputs

- `.grantstack/safety.yaml` updated; summary of the current state.

## Anti-patterns

- **Bypassing while on.** A confirmed prompt covers that command only; never flip the flag off to avoid future prompts unless the user runs `/grantstack:careful off`.

## Next

Pair with `/grantstack:freeze`; both together is `/grantstack:guard`.
