---
name: state-of-art
description: Maps the field into strands, locates the specific limit your breakthrough resolves, names the must-engage works and the competitors who could scoop you, and writes proposal/sections/state-of-art.tex. Use after the breakthrough is settled, when the user needs to show they command the field before claiming to go beyond it. Never invents citations.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - WebSearch
  - WebFetch
  - Bash(date *)
---

# /grantstack:state-of-art

**Stage:** position · **Voice:** systematic-reviewer who also thinks like a panel chair

Before you can claim to go beyond the state of the art, you must show you command it — for two readers: the in-field referee who knows the literature cold, and the generalist panel who needs the gap made legible.

## Procedure

1. **Load** `.grantstack/big-idea.md`, `.grantstack/config.yaml`, `.grantstack/learnings.jsonl`, and the citable keys of `proposal/refs.bib` (`grep -o '^@[A-Za-z]*{[^,]*' proposal/refs.bib`) rather than the whole bibliography. Read the state-of-art bar in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`.
2. **Build the landscape.** Organize the field into 3-5 strands. For each: what is established, who owns it (the canonical works), and where it stops. Cite only keys that exist in `refs.bib`; mark anything missing as `\cite{TODO-author-year-keyword}` with a `% TODO: add ref` comment (`[@TODO-author-year-keyword]` when `grant.format` is markdown). Never fabricate a citation.
3. **Locate the gap precisely.** Not "no one has studied X" — a specific limit: a method that cannot reach, an assumption no one has tested, a phenomenon no framework explains. State the gap as the thing the breakthrough sentence resolves.
4. **Name the must-engage works** — the 3-7 papers or books a referee expects you to engage. Omitting any reads as not knowing the field. Flag those not yet in `refs.bib`.
5. **Scoop / competitor scan.** Who is visibly near this — recent grants, preprints, conference programmes, lab pages? Search for it rather than guessing; a panel may include or consult these people. For each, state how your approach differs.
6. **Write `proposal/sections/state-of-art.tex`**: brief landscape → the specific gap → why existing approaches cannot close it → a one-paragraph bridge to the objectives. The gap must be visible to a non-specialist within two sentences.
7. **Save the working notes** to `.grantstack/state-of-art-notes.md` — strand map, must-engage list, competitor scan — and set `grant.status: "positioning"` in `.grantstack/config.yaml` if it still says `framing`.

## Outputs

- `proposal/sections/state-of-art.tex`.
- `.grantstack/state-of-art-notes.md` — working notes, not for the proposal.
- Summary block: the gap in one sentence, the must-engage list, and the `refs.bib` entries to add.

## Anti-patterns

- **Fabricating citations.** Mark missing refs TODO; never invent an author-year-title.
- **A gap of the form "X is understudied".** Understudied is not a breakthrough opening; name the specific limit.
- **A literature wall.** A generalist panel skims a dense review. Lead with the gap, support with the strands.
- **Ignoring competitors.** Pretending no one is near it reads as naive; the referee knows who is.

## Next

`/grantstack:groundbreaking-test` to prove the gap is a leap, then `/grantstack:objectives`.
