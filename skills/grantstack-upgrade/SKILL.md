---
name: grantstack-upgrade
description: Pulls the latest GrantStack from GitHub and re-runs setup. Wraps the bin/grantstack-upgrade shell script.
user-invocable: true
allowed-tools:
  - Bash
---

# /grantstack:grantstack-upgrade

**Stage:** power
**Voice:** maintenance

## Procedure

1. Run `grantstack-upgrade` (the shell script at `bin/grantstack-upgrade` in the GrantStack checkout) via Bash.
2. Capture stdout/stderr.
3. Summarize what changed: skills added, skills removed, version delta.

## Outputs

- Summary block: previous version → new version, list of new/changed skills, instruction to restart Claude Code if changes affect skill loading.

## Anti-patterns to refuse

- **Upgrading mid-proposal without warning.** If a proposal folder is in active use, surface the changeset *before* the upgrade so the user can opt in.
