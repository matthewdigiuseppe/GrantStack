# GrantStack philosophy

## Why this exists

A big research grant — an ERC Starting/Consolidator/Advanced Grant, an NWO Veni/Vidi/Vici — is not a long paper. It is a different artifact with a different reader, a different bar, and a different failure mode. A "help me write my grant" prompt collapses the whole thing into one stage, and an undirected AI does the stage it knows best: prose. You get a fluent methodology when what you needed was someone to tell you the idea isn't ground-breaking yet, or that the budget contradicts the work packages, or that the synopsis loses a generalist panel by paragraph two.

[gstack](https://github.com/garrytan/gstack) by Garry Tan noticed this pattern in product engineering: a single AI is a worse collaborator than a small team of role-defined ones. [MStack](https://github.com/matthewdigiuseppe/MStack) applied the fix to academic papers. GrantStack applies it to big grants — the same wager, a different lifecycle.

## The wager

Three claims:

1. **Grant-writing has stages, and the questions don't transfer between them.** Frame → position → design → write → stress-test → submit/defend → reflect. "Is this actually ground-breaking?" matters at positioning; it's too late to ask at the interview. "Does the budget close against the work packages?" matters at design; it's noise at framing.
2. **Role-based prompting beats free-form prompting.** A skill that says "you are the incremental-skeptic reviewer; argue this is not ground-breaking and make the applicant defeat you" produces different — and more useful — output than "give me feedback on my proposal."
3. **Per-proposal memory beats per-conversation memory.** A `.grantstack/` folder carries the breakthrough sentence, the panel assumptions, the risk register, and every prior mock review across sessions. The proposal is the unit; the chat is not.

## What is different about grants (the two readers)

Everything in a big-grant proposal is read by **two people at once**, and they want different things:

- **The generalist panel member** is not in your subfield, reads the whole proposal, and *decides whether you are funded*. They read the synopsis and lay summary hardest. If the breakthrough isn't legible to them, the rigour underneath never gets a fair hearing.
- **The in-field remote referee** reads the methodology and state-of-the-art deeply and prosecutes feasibility and genuine novelty. Their report feeds the panel.

GrantStack skills are built to serve both at once: `/synopsis-shotgun` and `/lay-summary` for the generalist; `/methodology`, `/state-of-art`, and `/feasibility-audit` for the expert; `/panel-mock` simulates each separately so neither is neglected.

## The two things every big grant must be at once

**Ground-breaking and feasible.** These pull against each other, and most rejections live in the gap:

- Too safe → "excellent but not ground-breaking" → below the line.
- Too bold with no plan → "exciting but not feasible / reckless" → below the line.

So GrantStack has a skill that enforces each, and refuses to let one paper over the other: `/groundbreaking-test` prosecutes the ambition; `/risk-register` and `/feasibility-audit` prosecute the deliverability. The bold core is defended with fallbacks, not sanded down.

## The person is half the score

ERC and NWO judge the **applicant and the project together**. A brilliant project with a weak case for *why you* loses. `/track-record` treats the CV as an argument — curated to evidence ground-breaking capacity — not a list. `/big-idea` forces the "why you" answer up front, and `/interview-prep` rehearses defending it in the room.

## The decision is often made after the proposal

For ERC Consolidator (step-2 interview) and NWO Vici (rebuttal + committee interview), the written proposal gets you *invited*; the **defense decides it**. GrantStack treats rebuttal and interview as first-class stages (`/rebuttal`, `/interview-prep`), because a strong proposal lost at interview is the most expensive way to fail.

## Rejection is a stage, not a verdict

Most funded big grants are resubmissions. `/retro` mines the reviews for signal; `/resubmit` plans the next attempt without gutting the ambition. The learning loop is part of the system, not an afterthought.

## How to read the skill set

Every skill carries a **stage** and a **voice**. Stage tells you when to use it; voice tells you whose ear it's in.

- **Advisor / adversarial-advisor** voices own framing (`/grant-fit`, `/big-idea`, `/scope-challenge`) — their job is to talk you out of unfundable ideas before you spend months.
- **Methodologist / architect / finance** voices own design — making the project deliverable.
- **Writer** voice owns the writing stage and defers to your configured `voice.writing_style`.
- **Reviewer** voice (`/panel-mock`) defers to `grant-reviewer-style` and front-runs the real panel.
- **Compliance** voice (`/call-spec`, `/admin-pack`) guards the gates that get proposals desk-rejected.
- **Coach / strategist** voices close the loop (`/interview-prep`, `/retro`, `/resubmit`).

## Defaults you should know

- **Schemes:** built around ERC (StG/CoG/AdG) and NWO Talent (Veni/Vidi/Vici); the spine generalizes to most large individual-investigator schemes (ANR JCJC, DFG, UKRI fellowships, etc.). Set `grant.scheme` in `.grantstack/config.yaml`.
- **The call is the contract.** `/call-spec` ingests the *actual* call document; GrantStack never asserts page limits or eligibility rules from memory, because they change yearly and per panel.
- **Manuscript format:** LaTeX by default; `markdown` if you set `grant.format: markdown`.
- **Writing voice:** user-configurable. Set `voice.writing_style`; GrantStack ships none. Reviewer voice: `grant-reviewer-style`.
- **Citations are never invented.** Drafting skills cite only `proposal/refs.bib` and mark gaps as `\cite{TODO-...}`.

## Failure modes GrantStack is built to prevent

| Failure | Skill that catches it |
|---|---|
| Spending a year on a scheme you're not eligible/competitive for | `/grant-fit` |
| An idea that's very good but not ground-breaking | `/big-idea`, `/groundbreaking-test` |
| A sprawling proposal that's really three grants | `/scope-challenge` |
| A synopsis a generalist panel can't follow | `/synopsis-shotgun`, `/lay-summary`, `/panel-mock generalist` |
| "Exciting but not feasible / reckless" | `/risk-register`, `/feasibility-audit` |
| Budget that contradicts the work packages | `/feasibility-audit` |
| Desk-reject on page limit / font / missing annex | `/call-spec`, `/admin-pack` |
| Under-served, unweighted impact / knowledge-utilisation section | `/impact` |
| A CV dump instead of a case for *you* | `/track-record` |
| A strong proposal lost at the interview | `/interview-prep` |
| A rebuttal that concedes the ambition to placate a referee | `/rebuttal` |
| Resubmitting unchanged, or gutting the bold core | `/retro`, `/resubmit` |
