---
name: synopsis-shotgun
description: Generates 4-6 variants of the extended synopsis / project summary — the single most-read, most-decisive page — each leading with a different hook. Use after a synopsis draft exists. Writes variants into proposal/sections/synopsis.tex as commented options plus one recommended. Analog to MStack's /abstract-shotgun.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:synopsis-shotgun

**Stage:** write
**Voice:** writer (anchored to `.grantstack/config.yaml` → `voice.writing_style`)

## When to invoke

A synopsis draft exists. This page (ERC extended synopsis, NWO summary/abstract) is read by every panel member, often first and sometimes only — it decides whether the rest gets a fair read. The opening move matters enormously, so generate variants instead of converging on the first.

## Procedure

1. **Load.** `proposal/sections/synopsis.tex`, `objectives.tex`, `state-of-art.tex`, `.grantstack/big-idea.md`, `.grantstack/config.yaml` (scheme, panel), `.grantstack/call-spec.md` (length limit).

2. **Apply the configured voice** across all variants; generic vivid grant voice if unset.

3. **Generate 4-6 variants**, each leading with a different hook:

   | Variant | Opens with |
   |---|---|
   | **Breakthrough-first** | The transformative claim. "This project establishes X, overturning the assumption that Y." |
   | **Puzzle-first** | The anomaly the field can't explain. "The field assumes X, yet Y — no framework reconciles them." |
   | **Stakes-first** | What's at stake scientifically or societally. "Whether X is possible determines Y." |
   | **Barrier-first** | The wall everyone's stuck behind. "Progress on X has stalled because no method can Z. This project builds that method." |
   | **Why-now-first** | The new enabler. "A new [method/dataset/instrument] makes it possible, for the first time, to X." |
   | **Vision-first** | The after-state. "Imagine a field in which X is settled. This project gets there." |

4. **Each variant respects the length limit** and contains, in some order: the breakthrough, why now, why you, the plan in brief, and the feasibility reassurance. The *order and emphasis* is what varies.

5. **Tag each variant** with: hook style, the reader it serves best (generalist panel vs. in-field), and its main risk (e.g., "vision-first risks sounding like hype to a hard-nosed panel").

6. **Write to `proposal/sections/synopsis.tex`**: all variants as comments, one recommended variant uncommented. Format:

   ```
   % VARIANT 1 (breakthrough-first):
   % <text>
   %
   % VARIANT 2 (puzzle-first):
   % <text>
   ...
   % --- RECOMMENDED ---
   <recommended variant, uncommented>
   ```

7. **Recommend.** Which variant best fits this scheme and panel, in one sentence. (Generalist panels often reward puzzle- or barrier-first over vision-first.)

## Outputs

- `proposal/sections/synopsis.tex` — variants as comments + one recommended.
- Summary block: 4-6 variants with one-line tags + recommendation.

## Anti-patterns to refuse

- **Variants that all open the same way.** Not a shotgun.
- **Going over the page/word limit.** Every variant fits the gate.
- **Hype the panel will distrust.** Bold is good; breathless is a risk — flag it on the variant.

## When to call other skills

- Before: `/draft-section synopsis` for a baseline.
- After: `/title-shotgun` to pair an acronym/title with the chosen hook; `/lay-summary` if the scheme wants a separate non-specialist summary.
