---
name: idea-shotgun
description: Generates 4-6 alternative framings of the same research programme, each with a breakthrough sentence, why-now, why-you, and the panel's likely reaction. Use when the core idea is real but you're not sure how to pitch it. Analog to MStack's /idea-shotgun, aimed at fundability not publishability.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(date *)
---

# /grantstack:idea-shotgun

**Stage:** frame
**Voice:** generative

## When to invoke

You have a research programme you believe in, but the framing isn't locked. The same body of work can be pitched as a methods breakthrough, a theory overturn, a societal-stakes project, or a frontier-opening tool — and the framing decides which panel buys it. Generate variants before committing.

## Procedure

1. **Load context.** Read `.grantstack/big-idea.md` (if it exists), `.grantstack/config.yaml` for the scheme and panel.

2. **Ask for the seed.** One paragraph: the research programme, what the user thinks the breakthrough is, and which panel/scheme it's aimed at.

3. **Generate 4-6 framings.** Each must vary along one of:
   - **Same work, different breakthrough claim** (methods leap vs. theory overturn vs. new-phenomenon).
   - **Same claim, different stakes** (intra-field significance vs. cross-field vs. societal/economic).
   - **Same stakes, different risk posture** (one bold high-risk core vs. a portfolio of medium-risk bets).
   - **Same project, different "why you"** (leaning on a unique method, a unique dataset/site, or a unique track record).

4. **Score each framing on a 5-line card:**

   ```
   FRAMING N: <breakthrough sentence, no clauses>
   --------
   Why now:        <the concrete enabler>
   Why you:        <the unique asset the track record can evidence>
   High-gain:      <what changes in the field if it works>
   Panel read:     <how a generalist panel in this scheme likely reacts>
   Main risk:      <the framing's biggest vulnerability — incrementalism, feasibility doubt, fit>
   ```

5. **Rank** on `(ambition × credibility-of-why-you) / (panel skepticism)` qualitatively. Surface the top 2.

6. **Save** to `.grantstack/idea-shotgun-<YYYY-MM-DD>.md` with all framings, including the ones not surfaced.

## Outputs

- `.grantstack/idea-shotgun-<date>.md` — full framing set with cards.
- Summary block: top 2 framings with a one-line case each, and a recommendation on which to take to `/big-idea` (or back to it).

## Anti-patterns to refuse

- **Variations on a theme.** Five framings that change one noun are not a shotgun. At least one must reframe what the breakthrough *is*.
- **Ignoring the panel.** A framing that excites the PI's subfield but baffles a generalist panel is a losing framing for these schemes — flag it.
- **Choosing the safest framing by default.** The shotgun exists to surface bolder pitches the PI wouldn't volunteer.

## When to call other skills

- After: `/big-idea` on the chosen framing (or `/scope-challenge` if the shotgun reveals it's really several grants).
