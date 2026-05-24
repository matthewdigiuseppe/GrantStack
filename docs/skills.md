# GrantStack skill reference

Each skill is invokable as `/<name>` once the plugin is installed. Stages match the workflow in [philosophy.md](philosophy.md).

## Stage 1 — Frame

| Skill | Voice | Use when |
|---|---|---|
| `/grant-fit` | advisor | First. Are you eligible and genuinely competitive for this scheme? |
| `/big-idea` | advisor | After grant-fit. Forcing questions on the breakthrough — what, why now, why you. |
| `/scope-challenge` | adversarial-advisor | Proposal sprawling or ambition mis-calibrated. One grant or three? Too big or too small? |
| `/idea-shotgun` | generative | The idea is real but the framing isn't locked. 4-6 ways to pitch the same programme. |
| `/call-spec` | compliance | Early: ingest the call's hard requirements. Re-run before submission to audit alignment. |

## Stage 2 — Position

| Skill | Voice | Use when |
|---|---|---|
| `/state-of-art` | systematic-reviewer | After big-idea. Field landscape + the specific gap your breakthrough opens. |
| `/groundbreaking-test` | incremental-skeptic | After state-of-art. Prosecutes "is this actually ground-breaking?" |
| `/objectives` | methodologist | Turn the breakthrough into 3-4 falsifiable objectives with success criteria. |
| `/risk-register` | risk officer | After objectives. High-risk/high-gain: risk → mitigation → fallback per bold objective. |

## Stage 3 — Design

| Skill | Voice | Use when |
|---|---|---|
| `/workpackage` | project architect | After objectives + risk-register. WPs, milestones, deliverables, dependencies, Gantt. |
| `/methodology` | methodologist | The approach, rigorous for the referee and legible for the panel. |
| `/team-resources` | group leader | Who you hire and the infrastructure, mapped to WPs. |
| `/budget` | finance officer | Cost the WPs and team within the ceiling; every euro maps to science. |
| `/impact` | impact strategist | The pathway to scientific/societal/economic value. Mandatory + weighted in NWO. |

## Stage 4 — Write

| Skill | Voice | Use when |
|---|---|---|
| `/draft-section <name>` | writer | Draft any section, scheme-aware and within the page budget. Anchors to `voice.writing_style`. |
| `/synopsis-shotgun` | writer | After a synopsis draft. 4-6 hooks for the most-read page. |
| `/title-shotgun` | writer | Late. Acronym + title options ranked on memorability × precision. |
| `/lay-summary` | translator | The non-specialist summary, plain language without dumbing down. |
| `/track-record` | advocate | The case for *you* — curated achievements, not a CV dump. |

## Stage 5 — Stress-test

| Skill | Voice | Use when |
|---|---|---|
| `/panel-mock [persona]` | reviewer | Submission-ready. Mock review as generalist / expert / skeptic / chair. Scored to the call's criteria. |
| `/feasibility-audit` | staff auditor | Internal consistency: objectives ↔ WPs ↔ timeline ↔ team ↔ budget. |
| `/mentor-review [persona]` | mentor | The honest read from an ally — senior-pi / grants-officer / field-elder. |

## Stage 6 — Submit / Defend

| Skill | Voice | Use when |
|---|---|---|
| `/rebuttal [round]` | applicant | Responding to referee reports (NWO rebuttal, ERC step-2 / resubmission). |
| `/interview-prep` | interview coach | Invited to interview. Pitch, slide skeleton, drilled question bank. |
| `/admin-pack` | grants coordinator | Assemble + check the admin package: declarations, host letter, forms, annexes. |

## Stage 7 — Reflect

| Skill | Voice | Use when |
|---|---|---|
| `/retro` | coach | After the outcome. What worked, what the reviews really said, what to systematize. |
| `/resubmit` | strategist | After a rejection you'll fight. Diff against reviews; plan the rework without gutting ambition. |

## Power tools

| Skill | Use when |
|---|---|
| `/careful` | Near a deadline. Warn before destructive commands. |
| `/freeze` | Lock edits to one directory. |
| `/guard` | `/careful` + `/freeze`. |
| `/unfreeze` | Remove the lock. |
| `/learn` | Per-proposal conventions Claude should remember. Writes `.grantstack/learnings.jsonl`. |
| `/grantstack-upgrade` | Pull latest GrantStack from GitHub. |

## File output conventions

Every skill writes to predictable paths inside the proposal folder:

| Skill | Writes to |
|---|---|
| `/grant-fit` | `.grantstack/grant-fit.md` |
| `/big-idea` | `.grantstack/big-idea.md` + `config.yaml` breakthrough |
| `/idea-shotgun` | `.grantstack/idea-shotgun-<date>.md` |
| `/call-spec` | `.grantstack/call-spec.md`, `.grantstack/call-spec-audit-<date>.md` |
| `/state-of-art` | `proposal/sections/state-of-art.tex` |
| `/groundbreaking-test` | `.grantstack/groundbreaking-test-<date>.md` |
| `/objectives` | `proposal/sections/objectives.tex` + `config.yaml` objectives |
| `/risk-register` | `.grantstack/risk-register.md` + `proposal/sections/feasibility.tex` |
| `/workpackage` | `proposal/sections/workpackages.tex` + `.grantstack/wp-plan.md` |
| `/methodology` | `proposal/sections/methodology.tex` |
| `/team-resources` | `proposal/sections/feasibility.tex` + `.grantstack/team-plan.md` |
| `/budget` | `budget/budget.md` |
| `/impact` | `proposal/sections/impact.tex` |
| `/draft-section <name>` | `proposal/sections/<name>.tex` |
| `/synopsis-shotgun` | `proposal/sections/synopsis.tex` (variants in comments) |
| `/title-shotgun` | `.grantstack/title-shotgun-<date>.md` + `config.yaml` acronym/title |
| `/lay-summary` | `proposal/sections/lay-summary.tex` |
| `/track-record` | `proposal/sections/pi-track-record.tex` + `cv/track-record.md` |
| `/panel-mock` | `.grantstack/review-cache/panel-mock-<persona>-<date>.md` |
| `/feasibility-audit` | `.grantstack/audits/<date>-feasibility.md` |
| `/mentor-review` | `.grantstack/review-cache/mentor-<persona>-<date>.md` |
| `/rebuttal` | `reviews/rebuttal/<round>-rebuttal.md` |
| `/interview-prep` | `reviews/interview/{pitch,slides-outline,qbank}.md` |
| `/admin-pack` | `admin/submission-checklist.md` + drafted annexes |
| `/retro` | `.grantstack/retro.md` |
| `/resubmit` | `.grantstack/resubmit-plan.md` |
