# GrantStack

**A Claude Code plugin for big research-grant writing.** Sibling to [MStack](https://github.com/matthewdigiuseppe/MStack); inspired by [gstack](https://github.com/garrytan/gstack).

gstack's wager is that role-based slash commands beat free-form prompting because they force the right questions at the right stage. MStack applied it to journal papers. GrantStack applies it to **big individual research grants** — ERC Starting / Consolidator / Advanced, NWO Veni / Vidi / Vici — where the artifact, the reader, and the bar are all different from a paper. A grant has clear stages — frame, position, design, write, stress-test, submit/defend, reflect — each with its own forcing questions, failure modes, and quality bar. GrantStack ships 33 skills that walk a proposal across all of them.

Think ERC Consolidator and NWO Vici, but the spine generalizes to most large investigator-driven schemes (ANR, DFG, UKRI fellowships).

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
