---
name: lay-summary
description: Writes the non-specialist summary a generalist panel, a funder's board, or the public reads — plain language, the stakes made vivid, the claim kept accurate — to the call's word cap. Use once the synopsis framing is locked, or when the user needs the public or lay abstract a submission form asks for.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:lay-summary

**Stage:** write · **Voice:** translator — a scientist who can explain it to a curious outsider

Most schemes require a summary for non-specialists, and it is usually published if you win. A jargon-dense lay summary signals you cannot communicate beyond your subfield, which these schemes penalize.

## Procedure

1. **Load** `proposal/sections/synopsis.tex`, `.grantstack/big-idea.md`, `.grantstack/config.yaml`, `.grantstack/call-spec.md` (the length and the audience the call specifies), and the lay-summary bar in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`.
2. **Draft in plain language**, in an order a non-expert can follow: the problem or question in terms anyone can grasp; why it matters, concretely; what you will do, by analogy or in everyday terms; what success would mean. No undefined jargon, no acronyms beyond the project's own, short sentences. One vivid, accurate image beats a paragraph of abstraction.
3. **Keep it true.** Plain is not the same as wrong: simplify the language, not the science, and do not promise more than the project delivers to make it sound exciting.
4. **Respect the limit.** Lay summaries usually carry tight word caps; hit it.
5. **Write to `proposal/sections/lay-summary.tex`** (or `.md` when `grant.format` is `markdown`). The file is not `\input` by `main.tex` — the lay summary is a submission-portal field — but it is versioned with the proposal so it stays in step.

## Outputs

- `proposal/sections/lay-summary.tex`.
- Summary block: the draft, its word count against the limit, and any jargon that slipped in.

## Anti-patterns

- **Jargon laundering.** Replacing one technical term with three is not plain language.
- **Dumbing down the science.** Simplify the words; keep the claim accurate.
- **Hype.** The lay summary is the version most likely to be quoted back at you.
- **A shrunk synopsis.** It is rewritten for a different reader, not compressed for the same one.

## Next

`/grantstack:panel-mock generalist` to check a non-expert actually follows it.
