---
name: title-shotgun
description: Generates project acronym + title options, ranked on memorability, precision, and panel-appeal. Grants live and die on a memorable acronym a panel repeats in the room. Use late, once the framing is locked. Writes to .grantstack/title-shotgun-<date>.md and can stamp the chosen pair into config. Analog to MStack's /title-shotgun.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:title-shotgun

**Stage:** write
**Voice:** writer

## When to invoke

Once the breakthrough framing is settled. A grant's acronym is how the panel refers to it during deliberation — "the QUANTA proposal" is an asset; an unmemorable one makes you the proposal they can't quite place. The title must be precise enough for the record and vivid enough to stick.

## Procedure

1. **Load.** `.grantstack/big-idea.md`, `proposal/sections/synopsis.tex`, `.grantstack/config.yaml` (current acronym/title, scheme).

2. **Generate 5-8 candidate pairs.** Each is an acronym + a full title. Vary across:
   - **Acronym derivation** — initials of the core concepts vs. an evocative word that encodes the mission.
   - **Register** — sober/scientific vs. vivid/metaphorical (calibrate to the panel; some domains reward restraint).
   - **Emphasis** — the phenomenon, the method, or the ambition.

3. **Score each pair on four axes (qualitatively):**
   - **Memorable** — will a panellist recall it a day later?
   - **Precise** — does the full title say what the project does without overclaiming?
   - **Pronounceable / clean** — no awkward or unfortunate readings; check it's not an existing well-known project or product.
   - **Fit** — matches the scheme's tone and the field's norms.

4. **Rank** and surface the top 2-3 with a one-line case each.

5. **Save** to `.grantstack/title-shotgun-<YYYY-MM-DD>.md`. If the user picks one, offer to write it into `.grantstack/config.yaml` → `grant.acronym` / `grant.title` (ask before overwriting non-empty).

## Outputs

- `.grantstack/title-shotgun-<date>.md` — all pairs with scores.
- Optionally update `config.yaml` acronym/title.
- Summary block: top 2-3 pairs + recommendation.

## Anti-patterns to refuse

- **A forced acronym** where the title is tortured to fit the letters. The title must read naturally; the acronym serves it, not the reverse.
- **Overclaiming titles.** "Solving X" invites the skeptic; "A new route to X" is bolder-sounding and safer.
- **Skipping the collision check.** Flag if a candidate clashes with a famous project, gene, product, or an unfortunate word.

## When to call other skills

- Before: `/synopsis-shotgun` (the title should pair with the chosen hook).
- After: stamp into config; reuse consistently via a `/learn` entry so every section uses the same acronym.
