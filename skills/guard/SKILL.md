---
name: guard
description: Maximum-safety mode — /grantstack:careful plus /grantstack:freeze in one toggle, enforced by the GrantStack hook. Use in the last days before a deadline.
argument-hint: "[directory]"
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Edit
---

# /grantstack:guard

**Stage:** power · **Voice:** safety

`$ARGUMENTS` is the directory to freeze writes to (as in `/grantstack:freeze`); if omitted, ask which.

## Procedure

1. Set `careful: true` in `.grantstack/safety.yaml` (as `/grantstack:careful` does).
2. Set `freeze.path` to the supplied directory (as `/grantstack:freeze` does).
3. Print the combined state. Both are enforced by the `PreToolUse` hook (`hooks/grantstack-guard.py`): destructive commands prompt for confirmation, writes outside the freeze path are denied.

## Outputs

- `.grantstack/safety.yaml` with both `careful: true` and `freeze.path`; summary of both flags + the freeze target.

## Next

`/grantstack:unfreeze` removes just the freeze (careful stays on); `/grantstack:careful off` removes just careful (freeze stays on).
