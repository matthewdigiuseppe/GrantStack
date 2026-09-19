---
name: methodology
description: Drafts the approach so the in-field referee judges it sound and the generalist panel finds it legible — each method tied to an objective and a work package, the novel core separated from the standard scaffolding, and validation stated. Writes proposal/sections/methodology.tex. Use after the objectives and work packages exist. Never invents citations.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash(date *)
---

# /grantstack:methodology

**Stage:** design · **Voice:** methodologist writing for two readers at once

The methodology is where the in-field referee decides whether you can do this and the generalist panel decides whether to trust you that you can. It must be rigorous enough for the expert and legible enough for the non-expert.

## Procedure

1. **Load** `proposal/sections/objectives.tex`, `proposal/sections/workpackages.tex`, `.grantstack/risk-register.md`, `.grantstack/config.yaml`, `.grantstack/learnings.jsonl`, the methodology bar in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`, and the citable keys of `proposal/refs.bib` (`grep -o '^@[A-Za-z]*{[^,]*' proposal/refs.bib`) rather than the whole bibliography.
2. **For each objective or WP, specify the approach:** the method concretely (design, instruments, data, analysis) in enough detail for a referee to judge validity; why *this* method and not the obvious alternative, pre-empting the "why not X?" comment; which established technique you stand on versus what you advance — the line between safe scaffolding and the novel core; and how you will know the method worked (controls, benchmarks, ground truth).
3. **Make the hard part legible.** For the most technical step add one or two sentences a generalist can follow — an analogy or a plain-language gloss — without dumbing down the expert version. This is the two-readers discipline in one paragraph.
4. **Connect to feasibility.** Each method's resource and time demand must be consistent with the WP timeline and the budget. Note where a method is pilot-tested before full commitment, matching the risk register's decision points.
5. **Write `proposal/sections/methodology.tex`**, organized by objective or WP — whichever the proposal uses elsewhere; keep the numbering consistent. Cite only keys in `refs.bib`; mark gaps `\cite{TODO-...}` (`[@TODO-...]` in markdown format) and never invent a technique's properties.

## Outputs

- `proposal/sections/methodology.tex`.
- Summary block: the per-objective method, the single novel methodological core, and any `refs.bib` entries to add.

## Anti-patterns

- **Fabricating citations or method properties.** Mark missing refs TODO.
- **A methods wall with no legibility for the panel.** The generalist decides funding; lose them and the rigour does not matter.
- **Hiding the novel core in jargon.** The expert needs to see exactly where you go beyond the standard toolkit — that is the part they score.
- **Methods unmoored from objectives.** Every method serves an objective; every objective has a method.

## Next

`/grantstack:feasibility-audit` (does the approach close in time and money), and `/grantstack:draft-section` for the sections around it.
