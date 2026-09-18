---
name: synopsis-shotgun
description: Generates 4-6 variants of the extended synopsis or project summary — the single most-read, most-decisive page — each leading with a different hook, tagged by the reader it serves and its main risk, and writes them into the section file with one recommended. Use once a synopsis draft exists and the framing is worth testing before it is locked.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:synopsis-shotgun

**Stage:** write · **Voice:** writer, anchored to `voice.writing_style` in `.grantstack/config.yaml`

The ERC extended synopsis and the NWO summary are read by every panel member, often first and sometimes only; the page decides whether the rest gets a fair read. The opening move matters enormously, so generate variants instead of converging on the first.

## Procedure

1. **Load** `proposal/sections/synopsis.tex`, `objectives.tex`, `state-of-art.tex`, `.grantstack/big-idea.md`, `.grantstack/config.yaml` (scheme, panel), `.grantstack/call-spec.md` (the length limit), `.grantstack/learnings.jsonl`, and the synopsis bar in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`.
2. **Apply the configured voice** across all variants; clean vivid grant prose if `voice.writing_style` is unset.
3. **Generate 4-6 variants**, each leading with a different hook:

   | Variant | Opens with |
   |---|---|
   | **Breakthrough-first** | The transformative claim. "This project establishes X, overturning the assumption that Y." |
   | **Puzzle-first** | The anomaly the field cannot explain. "The field assumes X, yet Y — no framework reconciles them." |
   | **Stakes-first** | What is at stake. "Whether X is possible determines Y." |
   | **Barrier-first** | The wall everyone is stuck behind. "Progress on X has stalled because no method can Z. This project builds that method." |
   | **Why-now-first** | The new enabler. "A new [method/dataset/instrument] makes it possible, for the first time, to X." |
   | **Vision-first** | The after-state. "Imagine a field in which X is settled. This project gets there." |

4. **Each variant respects the length limit** and contains, in some order, the breakthrough, why now, why you, the plan in brief, and the feasibility reassurance. What varies is order and emphasis.
5. **Tag each variant** with its hook style, the reader it serves best (generalist panel vs. in-field referee), and its main risk — "vision-first risks sounding like hype to a hard-nosed panel".
6. **Write to `proposal/sections/synopsis.tex`**: every variant as a comment, the recommended one uncommented.

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

   When `grant.format` is `markdown`, wrap the variants in `<!-- ... -->` instead; `%` is not a comment there and the variants would print.
7. **Recommend** the variant that best fits this scheme and panel, in one sentence. Generalist panels often reward puzzle- or barrier-first over vision-first.

## Outputs

- `proposal/sections/synopsis.tex` — variants as comments plus one recommended.
- Summary block: the variants with one-line tags, and the recommendation.

## Anti-patterns

- **Variants that all open the same way.** Not a shotgun.
- **Going over the page or word limit.** Every variant fits the gate.
- **Hype the panel will distrust.** Bold is good, breathless is a risk — flag it on the variant rather than writing it out.

## Next

`/grantstack:title-shotgun` to pair an acronym with the chosen hook; `/grantstack:lay-summary` for the non-specialist version; `/grantstack:panel-mock generalist` to test whether the hook lands.
