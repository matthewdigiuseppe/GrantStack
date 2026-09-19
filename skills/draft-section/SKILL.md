---
name: draft-section
description: Drafts a proposal section it owns — synopsis, feasibility, data-management or ethics — in the configured writing voice, to the substantive bar each section owes the two readers, within the call's page budget, citing only proposal/refs.bib. Use when the user asks to write or revise one of those sections; other sections belong to their own skill, which this one names.
argument-hint: "synopsis|feasibility|data-management|ethics"
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash(date *)
---

# /grantstack:draft-section

**Stage:** write · **Voice:** writer, anchored to `voice.writing_style` in `.grantstack/config.yaml`

`$ARGUMENTS` is the section to draft. This skill owns four:

| Section | Composed from |
|---|---|
| `synopsis` | `.grantstack/big-idea.md`, the newest `groundbreaking-test-*.md`, `proposal/sections/objectives.tex` |
| `feasibility` | `.grantstack/risk-register.md`, `.grantstack/team-plan.md`, `.grantstack/wp-plan.md` |
| `data-management` | `admin/data-management.md`, the DMP rules in `.grantstack/call-spec.md` |
| `ethics` | `admin/ethics.md`, the ethics rules in `.grantstack/call-spec.md` |

Every other section has a skill that owns it — `state-of-art`, `objectives`, `methodology`, `workpackages` (`/grantstack:workpackage`), `pi-track-record` (`/grantstack:track-record`), `impact`, `lay-summary`. If `$ARGUMENTS` names one of those, say which skill owns it and stop; if it names nothing recognized, list the four above and stop. One writer per file, or two skills overwrite each other's work.

Drafting ahead of the thinking produces prose you will rewrite: `synopsis` needs the objectives and the ground-breaking claim settled, `feasibility` needs the risk register and the team plan on disk.

## Procedure

1. **Load** `.grantstack/config.yaml` (scheme, acronym, title), `.grantstack/call-spec.md` (the page or word budget and formatting rules for this section — a hard gate), `.grantstack/learnings.jsonl` (proposal conventions), the section's source memos from the table above, and the sibling sections in `proposal/sections/` so voice, acronym, and cross-references stay consistent. List the citable keys of `proposal/refs.bib` with `grep -o '^@[A-Za-z]*{[^,]*' proposal/refs.bib` rather than reading the whole bibliography. Read the bar for this section in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`.
2. **Invoke the writing voice.** If `voice.writing_style` names an installed skill, use it for tone, rhythm, and vocabulary. If unset, write clean, vivid scholarly grant prose — confident, concrete, active, no hedge-stuffing, no thesaurus reaches — and tell the user once that they can set a style skill in `.grantstack/config.yaml`.
3. **Draft to the section's bar:**

   | Section | Quality bar |
   |---|---|
   | `synopsis` | The most-read page. Breakthrough → why now → why you → the plan in brief → why it is feasible. Legible to a generalist panel in one read, with the high-risk element stated as a bet rather than hidden. |
   | `feasibility` | Risk → mitigation → decision point → fallback, per bold objective; then team and resources; then the timeline closing. Bold but not reckless. Composed from the memos, not re-derived. |
   | `data-management` | FAIR-aligned: what data, where stored and archived, access and licensing, standards and repositories, who is responsible, what it costs — and the cost appears in the budget. |
   | `ethics` | Every applicable category addressed explicitly, approvals held or needed and from whom, and an explicit "not applicable" per category rather than a blank. |

4. **Citations.** Cite only keys that exist in `refs.bib`. For a needed-but-missing citation insert `\cite{TODO-author-year-keyword}` and append `% TODO: add ref — <description>`; in markdown format use `[@TODO-author-year-keyword]`. Never fabricate.
5. **Self-check before saving:** the section fits its page or word budget in `call-spec.md`; every number in it matches the memo or table it came from (budget total, duration, headcount, objective count); every cross-reference points at a section that exists; no citation key is invented; for `synopsis`, a generalist could state the breakthrough after one read.
6. **Write to disk** — `proposal/sections/<name>.tex`, or `.md` when `grant.format` is `markdown`. Overwrite only if the file is empty or still the template stub; otherwise produce a candidate and ask whether to overwrite, append, or save to `proposal/sections/<name>.candidate.tex`. On the first substantive section, set `grant.status: "writing"` in `.grantstack/config.yaml` if it still says `designing`.

## Outputs

- `proposal/sections/<name>.tex` (or `.candidate.tex` pending your decision).
- Summary block: word count against the budget, outstanding `TODO` citations, and anything cut to fit.

## Anti-patterns

- **Fabricating citations.** TODO them.
- **Blowing the page budget.** Draft to fit; if the content cannot compress without cutting scope, say so rather than silently overrunning.
- **Drafting a section another skill owns.** Name the skill and stop.
- **A synopsis only the subfield understands.** The whole panel reads it; if a generalist cannot follow it, it fails.
- **Generic voice when a `writing_style` is configured.** Defer to it; do not paper over it with hedge phrases.

## Next

After `synopsis`: `/grantstack:synopsis-shotgun` for variants. Once the sections exist: `/grantstack:call-spec audit`, `/grantstack:feasibility-audit`, then `/grantstack:panel-mock`.
