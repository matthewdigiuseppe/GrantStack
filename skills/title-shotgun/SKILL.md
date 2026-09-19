---
name: title-shotgun
description: Generates 5-8 acronym-and-title pairs ranked on memorability, precision, pronounceability and fit, checks each for collisions with known projects or unfortunate readings, and can stamp the chosen pair into config. Use late, once the framing is locked — the acronym is how a panel refers to the proposal in the room.
allowed-tools:
  - Read
  - Write
  - Edit
  - WebSearch
  - WebFetch
  - Bash(date *)
---

# /grantstack:title-shotgun

**Stage:** write · **Voice:** writer

"The QUANTA proposal" is an asset; an unmemorable acronym makes you the proposal the panel cannot quite place. The title must be precise enough for the record and vivid enough to stick.

## Procedure

1. **Load** `.grantstack/big-idea.md`, `proposal/sections/synopsis.tex`, `.grantstack/config.yaml` (current acronym and title, scheme).
2. **Generate 5-8 candidate pairs**, each an acronym plus a full title, varying across: **derivation** (initials of the core concepts vs. an evocative word that encodes the mission), **register** (sober and scientific vs. vivid and metaphorical — calibrate to the panel, since some domains reward restraint), and **emphasis** (the phenomenon, the method, or the ambition).
3. **Score each pair** qualitatively on four axes: **memorable** (will a panellist recall it a day later?), **precise** (does the title say what the project does without overclaiming?), **pronounceable and clean**, and **fit** with the scheme's tone and the field's norms.
4. **Run the collision check.** Search for each shortlisted acronym: an existing well-known project, a gene, a product, a company, or an unfortunate word or reading in any language the panel speaks. Report what you find; an acronym that collides with a famous project is one a panel will misattribute.
5. **Rank** and surface the top two or three with a one-line case each.
6. **Save** to `.grantstack/title-shotgun-<YYYY-MM-DD>.md` (date from `date +%F`). If the user picks one, write it into `grant.acronym` and `grant.title` in `.grantstack/config.yaml`, editing in place and asking before overwriting non-empty values, and append the choice to `decisions:`. Config is where every section reads the acronym from — do not park it in `learnings.jsonl`.

## Outputs

- `.grantstack/title-shotgun-<date>.md` — every pair with its scores and collision findings.
- `grant.acronym` and `grant.title` in `.grantstack/config.yaml`, on the user's say-so.
- Summary block: the top two or three pairs and the recommendation.

## Anti-patterns

- **A forced acronym** where the title is tortured to fit the letters. The title reads naturally; the acronym serves it.
- **Overclaiming titles.** "Solving X" invites the skeptic; "A new route to X" sounds bolder and is safer.
- **Skipping the collision check.** Flag any clash with a famous project, gene, product, or unfortunate word.

## Next

Use the acronym consistently everywhere; `/grantstack:call-spec audit` checks that the proposal, budget, CV and annexes agree.
