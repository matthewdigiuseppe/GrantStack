---
name: state-of-art
description: Maps the field landscape and locates the gap your project breaks open — the must-engage works, the prevailing consensus you'll move, and the competitors who might scoop you. Writes proposal/sections/state-of-art.tex. Never invents citations. Analog to MStack's /lit-map, framed for a funding panel.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash(date *)
---

# /grantstack:state-of-art

**Stage:** position
**Voice:** systematic-reviewer who also thinks like a panel chair

## When to invoke

After `/big-idea` lands a breakthrough. Before you can claim you go "beyond the state of the art," you must show you command it — for two readers: the in-field referee who knows the literature cold, and the generalist panel who needs the gap made legible.

## Procedure

1. **Load.** `.grantstack/big-idea.md`, `.grantstack/config.yaml`, `proposal/refs.bib`.

2. **Build the landscape.** Organize the field into 3-5 strands. For each strand: what is established, who owns it (the canonical works), and where it stops. Cite only entries in `refs.bib`; mark anything missing as `\cite{TODO-author-year-keyword}` with a `% TODO: add ref` comment. Never fabricate a citation.

3. **Locate the gap precisely.** The gap is not "no one has studied X." It is a specific limit — a method that can't reach, an assumption no one has tested, a phenomenon no framework explains. State the gap as the thing your breakthrough sentence resolves.

4. **Name the must-engage works.** The 3-7 papers/books a referee will expect you to engage. Omitting any of these reads as not knowing the field. Flag any that aren't yet in `refs.bib`.

5. **Scoop / competitor scan.** Who else is visibly near this (recent grants, preprints, conference programmes, lab pages)? For each, state how your approach differs. A panel may include or consult these people.

6. **Write `proposal/sections/state-of-art.tex`.** Structure: brief landscape → the specific gap → why existing approaches can't close it → one-paragraph bridge to your objectives. End on the sentence that hands off to `/objectives`. Make the gap visible to a non-specialist in the first two sentences.

## Outputs

- `proposal/sections/state-of-art.tex`.
- `.grantstack/state-of-art-notes.md` — the strand map, must-engage list, and competitor scan (working notes, not for the proposal).
- Summary block: the gap in one sentence, the must-engage list, and any missing `refs.bib` entries to add.

## Anti-patterns to refuse

- **Fabricating citations.** Mark missing refs as TODO; never invent author-year-title.
- **A gap of the form "X is understudied."** Understudied is not a breakthrough opening. Name the specific limit.
- **A literature wall.** A generalist panel skims a dense review. Lead with the gap, support with the strands.
- **Ignoring competitors.** Pretending no one is near it reads as naive; the referee knows who is.

## When to call other skills

- Before: `/big-idea` if no breakthrough is on file.
- After: `/groundbreaking-test` to prove the gap is a leap, then `/objectives`.
