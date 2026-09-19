---
name: idea-shotgun
description: Generates 4-6 alternative framings of the same research programme — each with its own breakthrough sentence, why-now, why-you, high-gain payoff and likely panel reaction — then ranks them. Use when the research programme is real but the pitch is not locked, or when /grantstack:big-idea judged the idea promising but unframed.
allowed-tools:
  - Read
  - Write
  - Bash(date *)
---

# /grantstack:idea-shotgun

**Stage:** frame · **Voice:** generative

The same body of work can be pitched as a methods breakthrough, a theory overturn, a societal-stakes project, or a frontier-opening tool — and the framing decides which panel buys it. Generate variants before committing.

## Procedure

1. **Load** `.grantstack/big-idea.md` if it exists and `.grantstack/config.yaml` for the scheme and panel.
2. **Get the seed.** One paragraph from the user: the research programme, what they think the breakthrough is, and the panel it is aimed at. If the conversation or `.grantstack/big-idea.md` already supplies these, do not re-ask.
3. **Generate 4-6 framings**, each varying along one of:
   - **Same work, different breakthrough claim** (methods leap vs. theory overturn vs. new phenomenon).
   - **Same claim, different stakes** (intra-field vs. cross-field vs. societal/economic).
   - **Same stakes, different risk posture** (one bold high-risk core vs. a portfolio of medium-risk bets).
   - **Same project, different "why you"** (a unique method, a unique dataset or site, a unique track record).
4. **Score each on a five-line card:**

   ```
   FRAMING N: <breakthrough sentence, no clauses>
   --------
   Why now:        <the concrete enabler>
   Why you:        <the unique asset the track record can evidence>
   High-gain:      <what changes in the field if it works>
   Panel read:     <how a generalist panel in this scheme likely reacts>
   Main risk:      <the framing's biggest vulnerability — incrementalism, feasibility doubt, fit>
   ```

5. **Rank** on `(ambition × credibility-of-why-you) / (panel skepticism)`, qualitatively, and surface the top two.
6. **Save** to `.grantstack/idea-shotgun-<YYYY-MM-DD>.md` (date from `date +%F`) with every framing, including the ones not surfaced.

## Outputs

- `.grantstack/idea-shotgun-<date>.md` — the full framing set with cards.
- Summary block: the top two with a one-line case each, and which to take to `/grantstack:big-idea`.

## Anti-patterns

- **Variations on a theme.** Five framings that change one noun are not a shotgun; at least one must reframe what the breakthrough *is*.
- **Ignoring the panel.** A framing that excites the subfield but baffles a generalist panel is a losing framing here — flag it.
- **Choosing the safest framing by default.** The shotgun exists to surface bolder pitches the PI would not volunteer.

## Next

`/grantstack:big-idea` on the chosen framing, or `/grantstack:scope-challenge` if the shotgun reveals several grants.
