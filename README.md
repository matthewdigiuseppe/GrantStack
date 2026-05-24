# GrantStack

**A Claude Code plugin for big research-grant writing.** Sibling to [MStack](https://github.com/matthewdigiuseppe/MStack); inspired by [gstack](https://github.com/garrytan/gstack).

gstack's wager is that role-based slash commands beat free-form prompting because they force the right questions at the right stage. MStack applied it to journal papers. GrantStack applies it to **big individual research grants** — ERC Starting / Consolidator / Advanced, NWO Veni / Vidi / Vici — where the artifact, the reader, and the bar are all different from a paper. A grant has clear stages — frame, position, design, write, stress-test, submit/defend, reflect — each with its own forcing questions, failure modes, and quality bar. GrantStack ships 33 skills that walk a proposal across all of them.

Think ERC Consolidator and NWO Vici, but the spine generalizes to most large investigator-driven schemes (ANR, DFG, UKRI fellowships).

## Why GrantStack exists

A big research grant is not a long paper, and treating it like one is why strong scientists write losing proposals. Three things make it a different beast, and GrantStack is built around them:

- **You write for two readers at once.** A **generalist panel member** — not in your subfield — reads the whole proposal and *decides whether you are funded*; they read the synopsis and lay summary hardest. An **in-field referee** reads the methodology deeply and prosecutes feasibility and novelty. A proposal that satisfies one and loses the other fails. Skills like `/synopsis-shotgun` and `/lay-summary` serve the panel; `/methodology` and `/feasibility-audit` serve the referee; `/panel-mock` simulates each separately so neither is neglected.
- **It must be ground-breaking *and* feasible.** These pull against each other, and most rejections live in the gap: too safe earns "excellent but not ground-breaking"; too bold with no plan earns "exciting but not feasible." So one skill enforces each — `/groundbreaking-test` prosecutes the ambition, `/risk-register` and `/feasibility-audit` prosecute the deliverability — and the bold core is defended with fallbacks, never sanded down.
- **The person is half the score.** ERC and NWO judge the applicant and the project *together*; a brilliant project with a weak case for "why you" loses. `/track-record` treats the CV as an argument, and `/interview-prep` rehearses defending it in the room — because for ERC Consolidator and NWO Vici, the written proposal gets you *invited* and the **interview decides it**.

A "help me write my grant" prompt collapses all of this into one stage, and an undirected assistant defaults to the stage it knows best — prose. GrantStack forces the right question at the right stage instead.

## How it relates to MStack and gstack

[gstack](https://github.com/garrytan/gstack) (Garry Tan) made the original bet for product engineering: a single AI is a worse collaborator than a small team of role-defined ones, each speaking in a defined voice with defined questions. [MStack](https://github.com/matthewdigiuseppe/MStack) ported that bet to academic **papers** — idea → lit → design → analysis → writing → submission. GrantStack is its **sibling for grants** — frame → position → design → write → stress-test → submit/defend → reflect.

The architecture is shared: role-based skills, per-project memory, shotgun-for-divergence / review-for-convergence, edit-safety power tools. What differs is everything domain-specific — the lifecycle, the two-readers discipline, the ground-breaking/feasible tension, the panel-and-interview defense, and the resubmission loop. Use **MStack** when the deliverable is a paper for a journal; use **GrantStack** when it's a proposal for a funder. They're independent plugins; install either or both.

## Install

GrantStack works in every flavor of Claude Code: the **terminal CLI**, the **Mac and Windows desktop apps**, **Claude Code on the web** (claude.ai/code), and the **VS Code and JetBrains extensions**. The steps are the same in all of them.

### Step 1 — Add GrantStack to Claude Code

Open Claude Code and type these two lines, one at a time, into the chat box:

```
/plugin marketplace add matthewdigiuseppe/GrantStack
/plugin install grantstack@grantstack
```

The first line tells Claude Code where to find GrantStack. The second installs it. When both are done, all GrantStack commands — `/grant-fit`, `/big-idea`, `/panel-mock`, and so on — are ready. Type `/plugin` to see what's installed.

### Step 2 — Start a new proposal

In Claude Code, just ask in plain English:

> Please run `grantstack-init quantum-aid --scheme erc-cog` to set up a new GrantStack proposal folder here.

(Replace `quantum-aid` with a short name and `erc-cog` with your scheme.) Claude creates the folder with everything in the right place. Then open `.grantstack/config.yaml` and fill in your name, PhD year, the acronym/title, the call deadline, and the host.

You're done. From here you'd typically start with `/grant-fit` then `/big-idea`.

### Power-user alternative (optional, terminal users only)

If you live in a Mac or Linux terminal and would rather run `grantstack-init` directly:

```bash
git clone https://github.com/matthewdigiuseppe/GrantStack.git ~/.claude/plugins/grantstack
cd ~/.claude/plugins/grantstack
./setup
```

`./setup` registers GrantStack with Claude Code and prints one line to paste into your shell config so `grantstack-init my-grant` works in any folder. Skip this if you installed via `/plugin install` above — it does the same job.

## Workflow

| Stage | What you type | What happens |
|---|---|---|
| **Frame** | `/grant-fit` | Eligibility + competitiveness interrogation before you commit |
| | `/big-idea` | Forcing questions: the breakthrough, why now, why you |
| | `/scope-challenge` | "One grant or three? Too big, or not ground-breaking enough?" |
| | `/idea-shotgun` | 4-6 framings of the same research programme |
| | `/call-spec` | Ingests the call's hard rules; later audits the proposal against them |
| **Position** | `/state-of-art` | Field landscape + the specific gap your breakthrough opens |
| | `/groundbreaking-test` | Skeptic prosecutes "is this actually ground-breaking?" |
| | `/objectives` | 3-4 falsifiable objectives with success criteria |
| | `/risk-register` | High-risk/high-gain: risk → mitigation → fallback |
| **Design** | `/workpackage` | WPs, milestones, deliverables, dependencies, Gantt |
| | `/methodology` | Approach: rigorous for the referee, legible for the panel |
| | `/team-resources` | Who you hire + infrastructure, mapped to WPs |
| | `/budget` | Cost the WPs within the ceiling; every euro maps to science |
| | `/impact` | Knowledge-utilisation / impact pathway (weighted in NWO) |
| **Write** | `/draft-section <name>` | Drafts a section in voice, within the page budget |
| | `/synopsis-shotgun` | 4-6 hooks for the single most-read page |
| | `/title-shotgun` | Acronym + title options, ranked |
| | `/lay-summary` | Plain-language summary for the generalist reader |
| | `/track-record` | The case for *you* — curated, not a CV dump |
| **Stress-test** | `/panel-mock [persona]` | Mock review: generalist / expert / skeptic / chair, scored to the call |
| | `/feasibility-audit` | Internal consistency: objectives ↔ WPs ↔ timeline ↔ team ↔ budget |
| | `/mentor-review [persona]` | The honest read from an ally |
| **Submit/Defend** | `/rebuttal` | Response to referee reports without conceding the ambition |
| | `/interview-prep` | Pitch, slides, and a drilled question bank for the interview |
| | `/admin-pack` | Declarations, host letter, forms, annexes — checked against the call |
| **Reflect** | `/retro` | Proposal retrospective; mine the reviews for signal |
| | `/resubmit` | Plan the next attempt without gutting the bold core |
| **Power** | `/careful`, `/freeze`, `/guard`, `/unfreeze` | Edit-safety controls |
| | `/learn` | Per-proposal conventions Claude should remember |
| | `/grantstack-upgrade` | Self-update |

## Per-proposal scaffold

`grantstack-init` creates this layout, and every skill assumes it:

```
my-grant/
  .grantstack/{config.yaml, learnings.jsonl, review-cache/, audits/}
  proposal/{main.tex, refs.bib, sections/}
  budget/budget.md
  cv/track-record.md
  admin/{data-management.md, ethics.md, submission-checklist.md}
  reviews/{rebuttal/, interview/}
  README.md
```

## How it works

Four moving parts do the work:

- **Skills are role-based slash commands.** Each `/command` is a skill that loads a specific voice and a specific procedure — `/groundbreaking-test` *is* the incremental-skeptic reviewer; `/panel-mock generalist` *is* the non-expert panellist. You're not prompting a general assistant; you're calling in the right specialist for the stage you're at. Type `/` in Claude Code to see them, or browse [`docs/skills.md`](docs/skills.md).
- **`.grantstack/` is the proposal's memory.** Everything durable lives in this folder, not in the chat: `config.yaml` (scheme, deadline, acronym, budget, status), `learnings.jsonl` (conventions Claude should remember — added via `/learn`), and caches of every mock review and audit. Close the session, reopen next week, and the proposal still knows its own breakthrough sentence and what the last panel-mock said. The proposal is the unit; the conversation is disposable.
- **`config.yaml` steers the skills.** Skills read it to stay scheme-aware (an ERC CoG and an NWO Vici get different framing), to anchor your prose voice (`voice.writing_style`), and to keep the acronym, budget, and status consistent across every section.
- **`/call-spec` makes the actual call the contract.** Rather than hardcode page limits or eligibility rules that change yearly, you paste the real call document into `/call-spec`; it extracts the hard requirements into a checklist and later audits the proposal against them. This is why the skills can say "confirm against the current call" instead of asserting rules that drift.

Outputs land in predictable files (`proposal/sections/*.tex`, `budget/budget.md`, `reviews/…`), so the proposal folder is a real working tree you can edit by hand, put under git, and hand to a co-applicant — not a chat transcript.

## A worked example

A typical ERC Consolidator run, start to interview:

```
grantstack-init deep-history --scheme erc-cog     # scaffold the folder
# fill in .grantstack/config.yaml (PhD year, acronym, deadline, host)

/grant-fit            # eligible (7–12y post-PhD) and competitive? honest verdict
/call-spec capture    # paste the ERC 2026 call → requirements checklist
/big-idea             # interrogate the breakthrough: what, why now, why you
/scope-challenge      # one grant or three? bold enough for CoG?

/state-of-art         # the field, and the specific gap you break open
/groundbreaking-test  # skeptic argues it's incremental — you defeat the argument
/objectives           # 3–4 falsifiable objectives with success criteria
/risk-register        # per bold objective: risk → mitigation → fallback

/workpackage          # WPs, milestones, dependencies, Gantt
/methodology          # rigorous for the referee, legible for the panel
/team-resources  /budget  /impact

/draft-section synopsis      # then state-of-art, methodology, …
/synopsis-shotgun            # 4–6 hooks for the most-read page
/track-record  /lay-summary  /title-shotgun

/call-spec audit      # page limits, fonts, missing annexes — desk-reject check
/feasibility-audit    # does budget ↔ WPs ↔ timeline ↔ team close?
/panel-mock generalist   →   /panel-mock skeptic   →   /mentor-review
/admin-pack           # declarations, host letter, forms

# … submitted, invited to interview …
/interview-prep       # the pitch, slide skeleton, and a drilled question bank
```

For an NWO Vici the shape is the same, with `/rebuttal` slotting in before the interview (Vici grants a written rebuttal stage; ERC does not — there you reply in the interview). If it's rejected: `/retro` to mine the reviews, then `/resubmit` to plan the next attempt without gutting the ambition.

## Design principles

1. **Role > prompt.** Every skill speaks in a defined voice — advisor, incremental-skeptic, panel reviewer, mentor, interview coach, compliance officer.
2. **Forcing questions over generation.** Framing and positioning skills interrogate the ambition before they produce prose.
3. **Two readers, always.** Every section serves the generalist panel who decides funding *and* the in-field referee who reads deeply.
4. **Ground-breaking and feasible at once.** `/groundbreaking-test` enforces the first; `/risk-register` and `/feasibility-audit` the second. Defend the bold core with fallbacks, never sand it down.
5. **The person is half the score.** `/track-record` makes the CV an argument; `/interview-prep` rehearses defending it.
6. **The call is the contract.** `/call-spec` ingests the actual call; GrantStack never asserts limits or eligibility from memory.
7. **Catch it before the panel does.** Internal `/panel-mock`, `/feasibility-audit`, `/mentor-review`, and `/call-spec audit` front-run the real review.
8. **Rejection is a stage, not a verdict.** `/retro` + `/resubmit` close the loop — most funded grants are resubmissions.
9. **Per-proposal memory.** A `.grantstack/` folder stores the breakthrough, panel assumptions, decisions, and prior reviews.

## Defaults

- **Schemes.** ERC (StG/CoG/AdG) and NWO Talent (Veni/Vidi/Vici). Set `grant.scheme` in `.grantstack/config.yaml`. The spine generalizes to other large fellowships.
- **Format.** LaTeX by default; set `grant.format: markdown` for Markdown.
- **Voice.** `/draft-section`, `/synopsis-shotgun`, and `/lay-summary` anchor tone to whatever skill name you put in `voice.writing_style`. GrantStack ships none; leave it empty for a generic vivid grant voice. Reviewer voice: `grant-reviewer-style`.
- **Citations.** Never invented — drafting skills cite only `proposal/refs.bib` and mark gaps as `\cite{TODO-...}`.

## License

MIT.
