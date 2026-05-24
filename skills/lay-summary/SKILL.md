---
name: lay-summary
description: Drafts the non-specialist / lay summary that a generalist panel, a board, or the public will read — plain language, no jargon, the breakthrough and its stakes made vivid without dumbing down. Writes proposal/sections/lay-summary.tex (or the field the scheme requires). Use once the synopsis is stable.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:lay-summary

**Stage:** write
**Voice:** translator (a scientist who can explain it to a curious outsider)

## When to invoke

Most schemes require a summary for non-specialists — a public/lay abstract, or a summary read by a generalist panel and the funder's board. It's often published if you win. A jargon-dense lay summary signals you can't communicate beyond your subfield, which these schemes penalize. Write it once the synopsis framing is locked.

## Procedure

1. **Load.** `proposal/sections/synopsis.tex`, `.grantstack/big-idea.md`, `.grantstack/config.yaml` (scheme), `.grantstack/call-spec.md` (length and audience the call specifies).

2. **Draft in plain language.** Cover, in order a non-expert can follow:
   - The problem or question, in terms anyone can grasp.
   - Why it matters — the stake, concretely.
   - What you'll do — the approach, by analogy or in everyday terms.
   - What success would mean.
   No undefined jargon. No acronyms beyond the project acronym. Short sentences. One vivid, accurate image is worth a paragraph of abstraction.

3. **Keep it true.** Plain is not the same as wrong. Simplify the language, not the science — don't promise more than the project delivers to make it sound exciting.

4. **Respect the limit.** Lay summaries usually have tight word caps; hit it.

5. **Write to `proposal/sections/lay-summary.tex`** (or the markdown/field the scheme requires).

## Outputs

- `proposal/sections/lay-summary.tex`.
- Summary block: the draft, its word count vs. limit, and a flagged list of any jargon that slipped in.

## Anti-patterns to refuse

- **Jargon laundering.** Replacing one technical term with three is not plain language.
- **Dumbing down the science.** Simplify the words; keep the claim accurate.
- **Hype.** A lay summary that overpromises is the version most likely to be quoted back at you.
- **A shrunk synopsis.** The lay summary is rewritten for a different reader, not compressed for the same one.

## When to call other skills

- Before: `/synopsis-shotgun` (lock the framing first).
- After: `/panel-mock generalist` to check a non-expert actually follows it.
