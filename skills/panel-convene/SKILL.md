---
name: panel-convene
description: Convenes a whole review panel — 4-8 reviewers from different disciplines and traditions, composed from the real published panel roster, who each read the proposal blind in their own subagent and then argue it out — and returns the ranking, where the panel split, and which objections you can answer by rewriting versus reframing. Use before submission when you want to know how a room full of different readers will disagree about your proposal, or run --step1 for the cheap screening pass.
argument-hint: "[SH2|PE6|committee] [--step1] [--size 4-8] [--dogmatism 0-10] [--named]"
allowed-tools:
  - Agent
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebSearch
  - WebFetch
  - Bash(date *)
---

# /grantstack:panel-convene

**Stage:** stress-test · **Voice:** panel secretary — records the room, never editorialises

`/grantstack:panel-mock` gives you one reviewer, fast. This convenes the whole panel: several reviewers from genuinely different traditions read the proposal **independently and blind**, then meet and argue. Use it when the single-reviewer pass has stopped surprising you, because what decides a real panel is not any one reader's verdict but where the readers disagree.

`$ARGUMENTS`: a panel code (`SH2`), a committee name, or nothing — then `panel.code` in `.grantstack/config.yaml`, then ask. Flags: `--step1` (screening mode: panellists read only the synopsis and track record, as a real step-1 panel does — much cheaper, and the stage where most proposals die), `--size 4-8` (default 8), `--dogmatism 0-10` (default 5, the panel's centre), `--named` (ground personas in named individuals from the roster rather than archetypes).

Read `${CLAUDE_PLUGIN_ROOT}/references/panel-composition.md` before composing anything. It carries the ethics this skill runs on — chief among them that **applicants must never contact a reviewer**, and that a simulated panellist's opinion is your inference from public work, never a real person's stated view.

## Procedure

1. **Load the proposal and the rules.** `.grantstack/config.yaml` (scheme, panel, acronym), `.grantstack/call-spec.md` (the evaluation criteria and weights the panel scores against — without these the panel scores on taste), and `${CLAUDE_PLUGIN_ROOT}/references/schemes.md` for how this scheme's panel works. Note the paths the panellists will read; do not read the sections yourself, because each panellist reads them independently.

2. **Reuse or compose the panel.** If `.grantstack/panel-roster.md` exists and its `code` matches, **reuse it unchanged** — the point of persistence is that a second run across a revised draft shows whether you moved anyone. Otherwise compose:

   a. **Get the roster.** Fetch the published panel-members list from the funder (the ERC publishes one document per call per scheme, chairs marked, released after the round closes). Walk this ladder and **name in the output which rung you used**: the published roster for the target year → the most recent published year, flagged as a proxy → ask the user to paste one → ask the user to describe the panel → compose generically from the scheme's criteria.

   b. **Sample, do not enumerate.** Look up five or six members' recent work with WebSearch — never all sixteen — and derive each one's discipline, method, and orientation. State the sample size.

   c. **Compose the distribution.** Build `--size` personas in the sampled proportions. Always seat the chair. Always seat at least one member whose orientation is furthest from the applicant's own: that reviewer is why this skill exists. Spread dogmatism around the `--dogmatism` centre rather than assigning it uniformly, and give any panel of five or more at least one member at 8 or above — a panel where everyone converges politely is not a panel.

   d. **Write `.grantstack/panel-roster.md`** — one block per persona, plus the composition provenance (roster rung, sample size, whether archetype or named):

   ```yaml
   - id: p3
     label: "critical-theoretic sociologist"
     discipline: "sociology"
     method: "interpretive, discourse-analytic"
     orientation: "critical"        # positivist | interpretive | critical | formal | historical | mixed
     seniority: "full professor"
     role: "member"                 # chair | rapporteur | member
     presses_on: "whose categories the project naturalises; who is absent from the data"
     moved_by: "reflexivity about the measurement's politics, not a citation to the critique"
     dogmatism: 8
     grounding: "archetype"         # archetype | described | named:<person>
   ```

   Under `--named`, `grounding` names the individual and every downstream sentence about them is phrased as inference from published work.

3. **Send each panellist in blind.** One `Agent` call per persona, `subagent_type: grantstack:panelist`, all dispatched together. Each prompt carries **only**: the persona's own block, the file paths to read (`--step1`: the synopsis and `cv/track-record.md` only; otherwise every section plus the budget and CV), the evaluation criteria from `call-spec.md`, and the assessment contract. It carries **nothing about any other panellist** — not their briefs, not their existence, not the panel's size. That is the whole design: a subagent starts with a fresh context and cannot see what the others are doing, so the disagreement you get back is real rather than staged.

   If the concurrent-subagent limit trips, spawn in batches of four; blindness is unaffected and only the wall-clock suffers. If the `Agent` tool is unavailable or denied, fall back to running the personas sequentially in this conversation — and **say in the output, plainly, that blind reading was not enforced**, because in a single context window it structurally cannot be.

4. **Table the assessments.** Once every panellist has returned, open the meeting with all of them in view. Reproduce each assessment **verbatim and unedited** in the output before any discussion: this is the pre-deliberation record and the most valuable thing the run produces. Do not summarise it away.

5. **Run the meeting**, holding every persona to its dogmatism band — 0–3 updates readily and may defer to the most forceful voice rather than the best argument; 4–6 updates on a good argument and concedes explicitly; 7–8 restates rather than concedes and moves only on evidence aimed at its own objection; 9–10 does not move and reinterprets counter-evidence to fit its prior.

   - **Round 0 — tabling.** The chair states the spread of standings and names the widest disagreement.
   - **Round 1 — positions.** Each member gives its standing and the one thing that would change its mind.
   - **Round 2 — cross-examination.** Each member answers the strongest point against it, and either moves or holds, in character.
   - **Round 3 — convergence.** The chair tests for consensus. Members who do not move say why.
   - **Close.** A ranking, and an explicit record of any split that survived.

6. **Classify every surviving objection** — this is what converts an argument into a work list, and it is the reason to run this rather than read four separate mock reviews:
   - **Rewrite** — the substance is in the proposal; it fails to show it.
   - **Rework** — it needs content that does not exist yet: a fallback, a test, a costed activity.
   - **Reframe** — the objection reaches the core; only a different framing answers it.
   - **Unanswerable** — a genuine disciplinary disagreement no revision resolves. Say who holds it and whether they are outnumbered.

7. **Save** to `.grantstack/review-cache/panel-convene-<YYYY-MM-DD>.md` (date from `date +%F`), opening with the **Recommendation** line. Set `grant.status: "review"` in `.grantstack/config.yaml` if it still says `writing`.

## Outputs

- `.grantstack/panel-roster.md` — the composed panel, reused by later runs.
- `.grantstack/review-cache/panel-convene-<date>.md` — recommendation, composition and its provenance, the verbatim blind assessments, the meeting, the surviving split, and the classified work list.
- Summary block: the standing, whether it was consensus or split, the single objection that most threatens funding, and how many of the panel hold it.

## Anti-patterns

- **A panel that agrees.** If eight reviewers from different traditions reach the same verdict, you have simulated one reviewer eight times. Check that the orientations actually differ and that the briefs were not homogenised.
- **Leaking the panel into the briefs.** A persona brief that mentions another panellist destroys the only thing that makes this better than `/grantstack:panel-mock`.
- **Summarising the blind assessments away.** They go in verbatim. The discussion is downstream of them and cannot replace them.
- **Presenting an inferred panel as the real one.** Name the rung of the roster ladder you used, every time.
- **Speaking for a named person.** "A panellist whose published work emphasises X would press on Y", never "Professor X thinks Y".
- **Treating the score as the output.** The score is the least transferable part. The split and the work list are the product.

## Next

`/grantstack:feasibility-audit` or `/grantstack:groundbreaking-test` for the objections classified rework or reframe; `/grantstack:draft-section` for the rewrites; `/grantstack:panel-mock` when you want one fast reader rather than a room. Before an interview, `/grantstack:interview-prep` — a surviving split is the question you will be asked.
