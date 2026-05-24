---
name: freeze
description: Lock edits to one directory. Refuses all writes outside that directory until /unfreeze. Useful during rebuttal/interview to keep Claude out of the frozen proposal, or always to keep it out of submitted/ annexes. Lifted from gstack's /freeze via MStack.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
---

# /grantstack:freeze

**Stage:** power
**Voice:** safety

## Argument

`$ARGUMENTS` — the directory to allow writes within. All writes outside this directory will be refused until `/unfreeze` is called.

If no argument is given, default to the current proposal-folder root (everything writeable as today).

## Procedure

1. **Read or create `.grantstack/safety.yaml`.**

2. **Set the lock.**
   - `freeze.path: <relative-or-absolute-path>`.
   - `freeze.set_at: <YYYY-MM-DD HH:MM>`.

3. **Behavior change while `freeze.path` is set:**
   - Before any `Write`, `Edit`, or `Bash` that mutates files outside `freeze.path`, refuse and tell the user to run `/unfreeze` first.
   - Reads, greps, finds, and `Bash` commands that don't mutate outside the path are fine.

4. **Print the lock state** to the user with the absolute path of the lock target.

## Outputs

- `.grantstack/safety.yaml` updated.
- Summary: lock target.

## Anti-patterns to refuse

- **Quietly working around the lock.** If a step requires a write outside, surface it and ask.

## When to call other skills

- Pair with `/careful` to make `/guard`.
- Use `/unfreeze` to clear.
