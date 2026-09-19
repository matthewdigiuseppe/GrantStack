# GrantStack skill reference

Each skill is invoked as `/grantstack:<name>` once the plugin is installed. The bare `/<name>` also works when nothing else in your setup claims that name, but the namespaced form is the one that always resolves. Stages match the workflow in [philosophy.md](philosophy.md).

## Stage 0 — Setup

| Skill | Voice | Use when |
|---|---|---|
| `/grantstack:grantstack-init <name> [--scheme …]` | scaffolder | Once per proposal. Creates the folder every other skill assumes. |

## Stage 1 — Frame

| Skill | Voice | Use when |
|---|---|---|
| `/grantstack:grant-fit` | advisor | First. Are you eligible and genuinely competitive for this scheme? |
| `/grantstack:big-idea` | advisor | After grant-fit. Forcing questions on the breakthrough — what, why now, why you. |
| `/grantstack:scope-challenge` | adversarial-advisor | Proposal sprawling or ambition mis-calibrated. One grant or three? Too big or too small? |
| `/grantstack:idea-shotgun` | generative | The idea is real but the framing isn't locked. 4-6 ways to pitch the same programme. |
| `/grantstack:call-spec capture` | compliance | Early: ingest the call's hard requirements from the document itself. |

## Stage 2 — Position

| Skill | Voice | Use when |
|---|---|---|
| `/grantstack:state-of-art` | systematic-reviewer | After big-idea. Field landscape + the specific gap your breakthrough opens. |
| `/grantstack:groundbreaking-test` | incremental-skeptic | After state-of-art. Prosecutes "is this actually ground-breaking?" |
| `/grantstack:objectives` | methodologist | Turn the breakthrough into 3-4 falsifiable objectives with success criteria. |
| `/grantstack:risk-register` | risk officer | After objectives. High-risk/high-gain: risk → mitigation → decision point → fallback. |

## Stage 3 — Design

| Skill | Voice | Use when |
|---|---|---|
| `/grantstack:workpackage` | project architect | After objectives + risk-register. WPs, milestones, deliverables, dependencies, Gantt. |
| `/grantstack:methodology` | methodologist | The approach, rigorous for the referee and legible for the panel. |
| `/grantstack:team-resources` | group leader | Who you hire and the infrastructure, mapped to WPs. |
| `/grantstack:budget` | finance officer | Cost the WPs and team within the ceiling; every euro maps to science. |
| `/grantstack:impact` | impact strategist | The pathway to scientific/societal/economic value. Mandatory and weighted in NWO. |

## Stage 4 — Write

| Skill | Voice | Use when |
|---|---|---|
| `/grantstack:draft-section <name>` | writer | Draft synopsis, feasibility, data-management or ethics. Anchors to `voice.writing_style`. |
| `/grantstack:synopsis-shotgun` | writer | After a synopsis draft. 4-6 hooks for the most-read page. |
| `/grantstack:title-shotgun` | writer | Late. Acronym + title options ranked, with a collision check. |
| `/grantstack:lay-summary` | translator | The non-specialist summary, plain language without dumbing down. |
| `/grantstack:track-record` | advocate | The case for *you* — curated achievements, not a CV dump. |

Other sections are written by the skill that owns them: `state-of-art`, `objectives`, `methodology`, `workpackages` (`/grantstack:workpackage`), `impact`, `pi-track-record` (`/grantstack:track-record`), `lay-summary`. One writer per file.

## Stage 5 — Stress-test

| Skill | Voice | Use when |
|---|---|---|
| `/grantstack:feasibility-audit` | staff auditor | Internal consistency: objectives ↔ WPs ↔ timeline ↔ team ↔ budget. |
| `/grantstack:panel-mock [persona]` | reviewer | Submission-ready. Mock review as generalist / expert / skeptic / chair, scored to the call. |
| `/grantstack:mentor-review [persona]` | mentor | The honest read from an ally — senior-pi / grants-officer / field-elder. |
| `/grantstack:call-spec audit` | compliance | Before submission. Page limits, format, missing annexes, leftover placeholders. |

## Stage 6 — Submit

| Skill | Voice | Use when |
|---|---|---|
| `/grantstack:admin-pack` | grants coordinator | Assemble + check the admin package: declarations, host letter, forms, annexes. |

## Stage 7 — Defend

| Skill | Voice | Use when |
|---|---|---|
| `/grantstack:rebuttal [round]` | applicant | Reports arrived and a written reply is due (NWO). ERC grants no rebuttal. |
| `/grantstack:interview-prep` | interview coach | Invited to interview. Pitch, slide skeleton, drilled question bank. |

## Stage 8 — Reflect

| Skill | Voice | Use when |
|---|---|---|
| `/grantstack:retro` | coach | After the outcome. What worked, what the reviews really said, what to systematize. |
| `/grantstack:resubmit` | strategist | After a rejection you'll fight. Diff against reviews; plan the rework without gutting ambition. |

## Power tools

| Skill | Use when |
|---|---|
| `/grantstack:proposal-status` | Where does this stand, and what is the one next step? |
| `/grantstack:careful` | Near a deadline. Warn before destructive commands. |
| `/grantstack:freeze <dir>` | Lock writes to one directory. |
| `/grantstack:guard [dir]` | `/grantstack:careful` + `/grantstack:freeze`. |
| `/grantstack:unfreeze` | Remove the lock. |
| `/grantstack:learn <fact>` | Per-proposal conventions Claude should remember. |
| `/grantstack:grantstack-upgrade` | Update GrantStack (git pull, or the marketplace command). |

The four safety toggles are enforced by a `PreToolUse` hook, not by prompt text: they write `.grantstack/safety.yaml`, and `hooks/grantstack-guard.py` reads it before every `Write`, `Edit`, and `Bash` call — including in a session that never loaded the skill. `admin/call/` and `reviews/received/` are read-only at all times; new files can be added, existing ones are never edited.

## Reference library

The skills carry their procedures; the substance a strong grants adviser brings lives in `references/`, loaded by the skills that need it at the stage that needs it.

| Reference | What it holds | Loaded by |
|---|---|---|
| `schemes.md` | How ERC and NWO Talent are shaped: two-step evaluation, who interviews, who grants a right of reply, eligibility windows and extensions, pre-proposal rounds, resubmission bars, budget structure. Numbers are order-of-magnitude under a verify-against-the-call banner | grant-fit, call-spec, scope-challenge, budget, panel-mock, interview-prep, rebuttal, admin-pack, resubmit |
| `panel-report-conventions.md` | Report structure, tone, specificity, the idioms that decide grants, and how to read a report you must answer (fallback for `voice.reviewer_style`) | panel-mock, mentor-review, rebuttal, retro |
| `proposal-conventions.md` | What each section owes the generalist panel and the in-field referee; reporting rules; complaints panels make most, by section | draft-section, state-of-art, objectives, methodology, workpackage, impact, track-record, synopsis-shotgun, lay-summary, panel-mock, mentor-review |
| `feasibility-catalog.md` | The contradictions panels find between objectives, WPs, timeline, team and budget, as checks — including the three arithmetic ones | feasibility-audit, workpackage, budget, team-resources, risk-register, draft-section |

Assets: `skills/admin-pack/assets/submission-checklist-template.md` (every row a verdict plus evidence) and `skills/interview-prep/assets/qbank-template.md`.

## Status and memory

Stage-completing skills advance `grant.status` in `.grantstack/config.yaml` (`state-of-art` → positioning, `workpackage` → designing, `draft-section`/`track-record` → writing, the review skills → review, `rebuttal` → rebuttal, `interview-prep` → interview, `retro` → funded/rejected, `resubmit` → resubmitting). `/grantstack:admin-pack` deliberately does not set `submitted` — only the portal can confirm that. `/grantstack:proposal-status` reconciles the field against the artifacts on disk and never changes it unasked.

Non-obvious decisions go in one place: the `decisions:` list in `.grantstack/config.yaml`. Conventions Claude should remember go in `.grantstack/learnings.jsonl` via `/grantstack:learn`.

## File output conventions

Every skill writes to predictable paths inside the proposal folder:

| Skill | Writes to |
|---|---|
| `/grantstack:grantstack-init` | the whole scaffold |
| `/grantstack:grant-fit` | `.grantstack/grant-fit.md` |
| `/grantstack:big-idea` | `.grantstack/big-idea.md` + `config.yaml` breakthrough, decisions |
| `/grantstack:scope-challenge` | `.grantstack/scope-challenge-<date>.md` |
| `/grantstack:idea-shotgun` | `.grantstack/idea-shotgun-<date>.md` |
| `/grantstack:call-spec` | `admin/call/<scheme>-<year>-call.md`, `.grantstack/call-spec.md`, `.grantstack/call-spec-audit-<date>.md` |
| `/grantstack:state-of-art` | `proposal/sections/state-of-art.tex` + `.grantstack/state-of-art-notes.md` |
| `/grantstack:groundbreaking-test` | `.grantstack/groundbreaking-test-<date>.md` |
| `/grantstack:objectives` | `proposal/sections/objectives.tex` + `config.yaml` objectives |
| `/grantstack:risk-register` | `.grantstack/risk-register.md` |
| `/grantstack:workpackage` | `proposal/sections/workpackages.tex` + `.grantstack/wp-plan.md` |
| `/grantstack:methodology` | `proposal/sections/methodology.tex` |
| `/grantstack:team-resources` | `.grantstack/team-plan.md` |
| `/grantstack:budget` | `budget/budget.md` |
| `/grantstack:impact` | `proposal/sections/impact.tex` |
| `/grantstack:draft-section <name>` | `proposal/sections/<name>.tex` (synopsis, feasibility, data-management, ethics) |
| `/grantstack:synopsis-shotgun` | `proposal/sections/synopsis.tex` (variants in comments) |
| `/grantstack:title-shotgun` | `.grantstack/title-shotgun-<date>.md` + `config.yaml` acronym/title |
| `/grantstack:lay-summary` | `proposal/sections/lay-summary.tex` |
| `/grantstack:track-record` | `proposal/sections/pi-track-record.tex` + `cv/track-record.md` |
| `/grantstack:feasibility-audit` | `.grantstack/audits/<date>-feasibility.md` |
| `/grantstack:panel-mock` | `.grantstack/review-cache/panel-mock-<persona>-<date>.md` |
| `/grantstack:mentor-review` | `.grantstack/review-cache/mentor-<persona>-<date>.md` |
| `/grantstack:admin-pack` | `admin/submission-checklist.md`, `admin/eligibility.md`, `admin/host-support.md`, the DMP and ethics annexes |
| `/grantstack:rebuttal` | `reviews/rebuttal/<round>-rebuttal.md` (and `reviews/received/<round>-referees.md` when you paste the reports) |
| `/grantstack:interview-prep` | `reviews/interview/{pitch,slides-outline,qbank}.md` |
| `/grantstack:retro` | `.grantstack/retro.md` |
| `/grantstack:resubmit` | `.grantstack/resubmit-plan.md` |
| `/grantstack:learn` | `.grantstack/learnings.jsonl` |
| `/grantstack:careful`, `freeze`, `guard`, `unfreeze` | `.grantstack/safety.yaml` |
| `/grantstack:proposal-status`, `/grantstack:grantstack-upgrade` | nothing (status offers a `grant.status` correction) |
