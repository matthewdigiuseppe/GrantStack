---
name: objectives
description: Turns the breakthrough into 3-4 falsifiable objectives, each with a success criterion, a link to the central claim, and a risk tag, then writes proposal/sections/objectives.tex and populates project.objectives in config. Use once the gap and the ground-breaking claim are settled, or when the current objectives read as "explore" and "investigate".
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Bash(date *)
---

# /grantstack:objectives

**Stage:** position · **Voice:** methodologist

The breakthrough is a vision; objectives are how a panel checks it is a *project*. Vague objectives are the commonest feasibility red flag. This skill operationalizes the ambition without shrinking it.

## Procedure

1. **Load** `.grantstack/big-idea.md`, the newest `.grantstack/groundbreaking-test-*.md`, `proposal/sections/state-of-art.tex`, `.grantstack/config.yaml`, and the objectives bar in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`.
2. **Derive 3-4 objectives.** Not more. Each one:
   - Is something the project will *establish, build, demonstrate, or measure* — a verb with a checkable outcome, never "explore X".
   - Maps to the breakthrough: together they add up to the one-sentence claim, with nothing off-mission and no part of the claim uncovered.
   - Has a **success criterion**: the result that counts as achieving it, and the result that would falsify the hypothesis behind it.
   - Carries a **risk tag** (`safe` / `bold` / `high-risk`) so the portfolio is visibly high-gain but not reckless — typically one anchor objective that de-risks the others, plus the bold core.
3. **Check the set.** *Coverage:* they jointly deliver the breakthrough. *Independence:* failure of the boldest does not sink the rest (the partial-success floor from `/grantstack:big-idea`). *Sequence:* note which must precede which — this seeds `/grantstack:workpackage`.
4. **Check before saving:** every objective has a success criterion and a falsifying result; every objective maps to a clause of the breakthrough sentence and no clause is unclaimed; at least one is tagged bold or high-risk and at least one is not; no objective is really a task (that is a work package); there are no more than four.
5. **Write `proposal/sections/objectives.tex`** — a framing sentence linking to the breakthrough, then numbered objectives (O1-O4), each: statement → why it matters to the ambition → success criterion. The panel should grasp the architecture in one read.
6. **Update config.** Write the statements into `project.objectives` in `.grantstack/config.yaml`, editing in place; ask before overwriting a non-empty list.

## Outputs

- `proposal/sections/objectives.tex`.
- `project.objectives` populated in `.grantstack/config.yaml`.
- Summary block: the objective set with risk tags, and the partial-success floor.

## Anti-patterns

- **"Explore / investigate / understand" objectives.** Unfalsifiable; replace with checkable outcomes.
- **More than four.** A fifth is usually a work package or scope creep — flag for `/grantstack:scope-challenge`.
- **All-safe or all-reckless portfolios.** High-gain needs a bold core; fundable needs a floor. Demand both.
- **Objectives that do not sum to the breakthrough.** If they fall short, the vision was hot air; if they overshoot, the scope is wrong.

## Next

`/grantstack:risk-register` (every bold objective needs a fallback), then `/grantstack:workpackage`.
