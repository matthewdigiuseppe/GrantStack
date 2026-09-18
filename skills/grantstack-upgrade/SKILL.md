---
name: grantstack-upgrade
description: Updates GrantStack — git pull plus setup for clone installs, or points marketplace installs at /plugin marketplace update. User-invoked only.
disable-model-invocation: true
allowed-tools:
  - Bash
  - Read
---

# /grantstack:grantstack-upgrade

**Stage:** power · **Voice:** maintenance

## Procedure

1. **Detect the install:** does `${CLAUDE_PLUGIN_ROOT}/.git` exist?
2. **Git clone** (installed via `./setup`): run `bash "${CLAUDE_PLUGIN_ROOT}/bin/grantstack-upgrade"`, which fetches, refuses a dirty tree, pulls `--ff-only`, and re-runs setup. Summarize previous version → new version (from `.claude-plugin/plugin.json`) and skills added / removed / changed.
3. **Marketplace install** (no `.git`; the plugin cache is a managed copy, not a repo): do not `git pull`. Tell the user to run `/plugin marketplace update grantstack` and restart Claude Code so reloaded skills take effect.

## Outputs

- Summary: install mode, previous → new version, restart reminder if skills changed.

## Anti-patterns

- **Upgrading mid-proposal unannounced.** If a proposal folder is in active use near a deadline, surface the changeset first so the user can opt in.
- **`git pull` in the plugin cache.** A marketplace install is not a checkout; only `/plugin marketplace update` works there.
