---
name: grantstack-init
description: Scaffolds a new GrantStack proposal folder (proposal/, budget/, cv/, admin/, reviews/, .grantstack/ memory) from the plugin template, pre-stamped with the scheme. Use when the user wants to start a new grant, proposal, or fellowship application — e.g. "set up a new ERC proposal on X" — or asks to run grantstack-init.
argument-hint: "<short-name> [--scheme erc-stg|erc-cog|erc-adg|nwo-veni|nwo-vidi|nwo-vici|other]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
---

# /grantstack:grantstack-init

**Stage:** setup · **Voice:** scaffolder

Once per proposal, in the directory where the proposal folder should live; every other skill assumes this layout. `$ARGUMENTS` is a short slug (`deep-history`; lowercase, hyphens, no spaces), optionally followed by `--scheme <scheme>`. Ask for the slug if missing; ask for the scheme if the user knows it, since `/grantstack:grant-fit` and every review skill read it.

## Procedure

1. **Refuse to nest.** If the current directory or an ancestor already contains `.grantstack/`, stop and tell the user to `cd` out; a proposal inside a proposal breaks every path convention.
2. **Run** `bash "${CLAUDE_PLUGIN_ROOT}/bin/grantstack-init" <short-name> [--scheme <scheme>]`.
3. **Fallback** if the script is missing or there is no bash: copy `${CLAUDE_PLUGIN_ROOT}/templates/proposal-folder` to `./<short-name>` (hidden files included); in `.grantstack/config.yaml` set `short_name`, `scheme` if supplied, and `status: "framing"`, editing those values in place so the comments survive.
4. **Verify** `.grantstack/config.yaml`, `proposal/sections/`, `budget/`, `cv/`, `admin/call/`, `reviews/received/` exist.
5. **Hand off:** fill in `.grantstack/config.yaml` — `pi.name`, `pi.phd_year` (eligibility windows), `grant.call_deadline`, `grant.host_institution`, the acronym and title once chosen, and `voice.writing_style` if a style skill is installed — then `/grantstack:grant-fit` (am I eligible and competitive?) or `/grantstack:big-idea`. Any time later, `/grantstack:proposal-status`.

## Outputs

- `./<short-name>/` — the full scaffold; summary: path, scheme, next steps.

## Anti-patterns

- **Scaffolding over an existing folder.** If `./<short-name>` exists, stop; never merge into it.
- **Skipping config.** It works empty, but remind the user once: `grant.scheme` and `pi.phd_year` drive eligibility, and every review skill reads the scheme.

## Next

`/grantstack:grant-fit`, then `/grantstack:big-idea` and `/grantstack:call-spec capture`.
