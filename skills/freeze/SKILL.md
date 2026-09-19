---
name: freeze
description: Locks writes to a single directory — a GrantStack hook denies edits anywhere else in the proposal folder until /grantstack:unfreeze. Use during the rebuttal or interview prep to keep Claude out of the submitted proposal, or to fence it into one part of the folder.
argument-hint: "<directory>"
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Edit
---

# /grantstack:freeze

**Stage:** power · **Voice:** safety

`$ARGUMENTS` is the directory writes stay inside, relative to the proposal folder (`reviews/rebuttal`, `reviews/interview`, `proposal/sections`). Without an argument do **not** lock: print the current state from `.grantstack/safety.yaml` and ask which directory; a lock on the whole folder is a no-op that gives false comfort.

Enforcement is the `PreToolUse` hook (`hooks/grantstack-guard.py`): while `freeze.path` is set, writes outside it are denied by the hook itself, including in later sessions that never loaded this skill. `.grantstack/` stays writable so the lock can be cleared; `admin/call/` and `reviews/received/` stay read-only regardless.

## Procedure

1. Read or create `.grantstack/safety.yaml`.
2. Set the lock in exactly this shape:

   ```yaml
   freeze:
     path: "reviews/rebuttal"
     set_at: "YYYY-MM-DD HH:MM"
   ```

3. Tell the user what the hook now does: `Write` / `Edit` outside the path (and outside `.grantstack/`) denied; mutating Bash (`rm`, `mv`, `cp`, redirects, `sed -i`, `git reset/clean/checkout --`) with targets outside the lock denied, and asked about when the targets cannot be resolved; reads, greps, and non-mutating commands unaffected.
4. Print the lock state with the absolute path of the target.

## Outputs

- `.grantstack/safety.yaml` updated; summary with the lock target.

## Anti-patterns

- **Working around the lock.** If a step needs a write outside, surface it and ask; do not restructure the work to dodge the hook.

## Next

`/grantstack:unfreeze` clears it; with `/grantstack:careful` it is `/grantstack:guard`.
