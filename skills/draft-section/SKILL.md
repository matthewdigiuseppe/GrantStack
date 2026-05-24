---
name: draft-section
description: Drafts a proposal section (synopsis, state-of-art, objectives, methodology, workpackages, feasibility, pi-track-record, impact, data-management, ethics) in voice, scheme-aware, within the call's page budget. Anchors tone to the writing-style skill in .grantstack/config.yaml. Section name passed as argument. Writes to proposal/sections/<name>.tex. Never fabricates citations.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash(date *)
---

# /grantstack:draft-section

**Stage:** write
**Voice:** writer (anchored to the skill named in `.grantstack/config.yaml` → `voice.writing_style`)

## When to invoke

After the upstream stage for that section is settled (e.g., draft `methodology` only after `/methodology` has specified the approach; draft `synopsis` only once objectives and the ground-breaking claim are stable). Drafting ahead of the thinking produces prose you'll rewrite.

## Argument

`$ARGUMENTS` is the section name. One of: `synopsis`, `state-of-art`, `objectives`, `methodology`, `workpackages`, `feasibility`, `pi-track-record`, `impact`, `data-management`, `ethics`.

If not supplied or unrecognized, list the recognized names and stop.

## Procedure

1. **Load context.**
   - `.grantstack/config.yaml` — scheme, acronym, title, status.
   - `.grantstack/call-spec.md` — the page/word budget and formatting rules for this section. Respect the limit as a hard gate.
   - `.grantstack/learnings.jsonl` — proposal-specific conventions (acronym usage, panel assumptions, framing decisions).
   - `proposal/refs.bib` — available citations; never invent entries.
   - Sibling sections in `proposal/sections/` so voice, acronym, and cross-references stay consistent.
   - The relevant upstream artifact (e.g., `.grantstack/risk-register.md` for feasibility, `cv/track-record.md` for pi-track-record).

2. **Invoke the writing voice.** Read `voice.writing_style`; if set, use that skill. If unset, write in a clean, vivid scholarly grant voice: confident, concrete, active, no hedge-stuffing, no thesaurus reaches. Tell the user once that no `voice.writing_style` is configured.

3. **Draft to the section's bar:**

   | Section | Quality bar |
   |---|---|
   | `synopsis` | The most-read page. Breakthrough → why now → why you → what you'll do → why it's feasible. Legible to a generalist panel in one read. |
   | `state-of-art` | Command the field, then name the specific gap your breakthrough opens. Gap visible in the first two sentences. |
   | `objectives` | 3-4 falsifiable objectives with success criteria; together they sum to the breakthrough. |
   | `methodology` | Rigorous for the referee, legible for the panel. Each method tied to an objective; the novel core marked. |
   | `workpackages` | WPs, milestones, deliverables, dependencies, Gantt. Verifiable milestones only. |
   | `feasibility` | Risk → mitigation → fallback; team and resources; timeline closes. Bold but not reckless. |
   | `pi-track-record` | The right person to do this. Achievements chosen to evidence ground-breaking capacity, not a CV dump. |
   | `impact` | Pathways with named audiences and mechanisms; proportional to the science. NWO: hit the knowledge-utilisation prompts. |
   | `data-management` | FAIR-aligned: what data, where stored/archived, access, standards, cost. |
   | `ethics` | Address each applicable category explicitly; state approvals held/needed. State "not applicable" per category rather than leaving blanks. |

4. **Citations.** Cite only `refs.bib` entries. For a needed-but-missing citation, insert `\cite{TODO-author-year-keyword}` and append `% TODO: add ref — <description>`. Never fabricate.

5. **Write to disk.** Output to `proposal/sections/<name>.tex` (`.md` if `config.format: markdown`). Overwrite only if the file is empty or a placeholder; otherwise produce a candidate and ask whether to overwrite, append, or save to `proposal/sections/<name>.candidate.tex`.

## Outputs

- `proposal/sections/<name>.tex`.
- Optional `.grantstack/draft-log.md` — one line per draft (date, section, word count, page-budget status, outstanding TODOs).

## Anti-patterns to refuse

- **Fabricating citations.** TODO them.
- **Blowing the page budget.** If `call-spec` says ≤5 pages, draft to fit; flag if the content can't compress without cutting scope.
- **Drafting `methodology`/`workpackages` before the design skills have run.** Stop and point to `/methodology` or `/workpackage`.
- **A synopsis only the subfield understands.** It's read by the whole panel; if a generalist can't follow it, it fails.
- **Generic voice when a `writing_style` is configured.** Defer to it.

## When to call other skills

- Before `synopsis`: `/objectives` and `/groundbreaking-test` should be on file.
- After `synopsis`: `/synopsis-shotgun` for variants.
- After all sections: `/call-spec audit`, then `/feasibility-audit`, then `/panel-mock`.
