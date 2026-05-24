---
name: methodology
description: Drafts the methodology/approach section so it convinces the in-field referee it's sound and the generalist panel it's feasible. Ties each method to an objective and a work package. Writes proposal/sections/methodology.tex. Never invents citations.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash(date *)
---

# /grantstack:methodology

**Stage:** design
**Voice:** methodologist writing for two readers at once

## When to invoke

After objectives and work packages exist. The methodology is where the in-field referee decides whether you can actually do this, and where the generalist panel decides whether to trust you that you can. It must satisfy both: rigorous enough for the expert, legible enough for the non-expert.

## Procedure

1. **Load.** `proposal/sections/objectives.tex`, `proposal/sections/workpackages.tex`, `.grantstack/risk-register.md`, `.grantstack/config.yaml`, `proposal/refs.bib`.

2. **For each objective/WP, specify the approach:**
   - The method, concretely — design, instruments, data, analysis. Enough that a referee can judge validity.
   - Why *this* method and not the obvious alternative (pre-empt the "why not X?" comment).
   - What established technique you stand on (cite `refs.bib`; mark gaps as `\cite{TODO-...}`) versus what you advance — the line between safe scaffolding and the novel core.
   - Validation: how you'll know the method worked (controls, benchmarks, ground truth).

3. **Make the hard part legible.** For the most technical step, add one or two sentences a generalist can follow — an analogy or a plain-language gloss — without dumbing down the expert version. This is the two-readers discipline.

4. **Connect to feasibility.** Each method's resource and time demand should be consistent with the WP timeline and the budget. Note where a method is pilot-tested before full commitment (links to risk-register decision points).

5. **Write `proposal/sections/methodology.tex`.** Organized by objective or WP (match whichever the proposal uses elsewhere — keep numbering consistent). Tight, specific, citation-grounded.

## Outputs

- `proposal/sections/methodology.tex`.
- Summary block: per-objective method, the single novel methodological core, and any `refs.bib` entries to add.

## Anti-patterns to refuse

- **Fabricating citations or methods.** Mark missing refs as TODO; never invent a technique's properties.
- **A methods wall with no legibility for the panel.** The generalist decides funding; lost them and the rigour doesn't matter.
- **Hiding the novel core in jargon.** The expert needs to see exactly where you go beyond the standard toolkit — that's the part they score.
- **Methods unmoored from objectives.** Every method serves an objective; every objective has a method.

## When to call other skills

- Before: `/objectives`, `/workpackage`.
- After: `/feasibility-audit` (does the approach close in time and money), `/draft-section` for surrounding sections.
