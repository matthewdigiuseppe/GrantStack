---
name: objectives
description: Turns the breakthrough into 3-4 concrete, falsifiable objectives, each with a success criterion and a link to the ambition. Writes proposal/sections/objectives.tex and populates project.objectives in config. Use after the gap and the ground-breaking claim are settled.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:objectives

**Stage:** position
**Voice:** methodologist

## When to invoke

After `/state-of-art` and `/groundbreaking-test`. The breakthrough is a vision; objectives are how a panel checks it's a *project*. Vague objectives ("explore", "investigate", "better understand") are the most common feasibility red flag. This skill operationalizes the ambition without shrinking it.

## Procedure

1. **Load.** `.grantstack/big-idea.md`, `.grantstack/groundbreaking-test-*.md`, `proposal/sections/state-of-art.tex`, `.grantstack/config.yaml`.

2. **Derive 3-4 objectives.** Not more. Each objective:
   - Is a thing the project will *establish, build, demonstrate, or measure* — a verb with a checkable outcome, not "explore X."
   - Maps to the breakthrough: together the objectives must add up to the one-sentence claim, with no objective that's off-mission and no part of the claim left uncovered.
   - Has a **success criterion**: what result counts as achieving it, and what result would falsify the hypothesis behind it.
   - Carries a **risk tag** (`safe` / `bold` / `high-risk`) so the portfolio is visibly high-gain but not reckless — typically one anchor objective that de-risks the others, plus the bold core.

3. **Check the set.**
   - **Coverage:** the objectives jointly deliver the breakthrough.
   - **Independence:** failure of the boldest objective doesn't sink all the others (the partial-success floor from `/big-idea`).
   - **Sequence:** note dependencies — which must precede which (this seeds `/workpackage`).

4. **Write `proposal/sections/objectives.tex`.** A short framing sentence linking to the breakthrough, then numbered objectives (O1-O4), each: statement → why it matters to the ambition → success criterion. Keep it tight; the panel should grasp the architecture in one read.

5. **Update config.** Write the objective statements into `.grantstack/config.yaml` → `project.objectives` (ask before overwriting non-empty).

## Outputs

- `proposal/sections/objectives.tex`.
- `.grantstack/config.yaml` → `project.objectives` populated.
- Summary block: the objective set with risk tags, plus a note on the partial-success floor.

## Anti-patterns to refuse

- **"Explore / investigate / understand" objectives.** Unfalsifiable; replace with checkable outcomes.
- **More than four.** A fifth objective is usually a work package or scope creep — flag for `/scope-challenge`.
- **All-safe or all-reckless portfolios.** High-gain needs a bold core; fundable needs a floor. Demand both.
- **Objectives that don't sum to the breakthrough.** If they do, the vision was hot air; if they overshoot, scope is wrong.

## When to call other skills

- Before: `/groundbreaking-test` if the discontinuity isn't on file.
- After: `/risk-register` (each bold objective needs a mitigation) and `/workpackage` (objectives → WPs).
