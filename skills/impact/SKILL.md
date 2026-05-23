---
name: impact
description: Drafts the impact / knowledge-utilisation section — the pathway from results to scientific, societal, and economic value, with concrete audiences and activities. Mandatory and weighted in NWO; framed as broader impact in ERC. Writes proposal/sections/impact.tex. Use during design or write.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:impact

**Stage:** design / write
**Voice:** impact strategist (not a marketer — a credible planner)

## When to invoke

Once the objectives and expected results are clear. In NWO schemes, **knowledge utilisation** is a separately weighted, mandatory criterion that applicants routinely under-serve — a thin impact section costs real points. In ERC, the case is excellence-first but a broader-impact framing still strengthens the synopsis. This skill builds a credible pathway, not slogans.

## Procedure

1. **Load.** `proposal/sections/objectives.tex`, `.grantstack/big-idea.md`, `.grantstack/config.yaml` (scheme), `.grantstack/call-spec.md` (how the call defines/weights impact).

2. **Separate the kinds of impact:**
   - **Scientific** — what fields, methods, or communities the results advance, and how the knowledge travels (datasets, tools, theory others build on).
   - **Societal** — concrete beneficiaries (policy, clinical practice, industry, public, specific communities) and what changes for them.
   - **Economic** — where relevant: applications, IP, spin-out potential, cost savings.

3. **Build the pathway, not the promise.** For each impact, trace: *result → who needs it → how it reaches them → what they do differently.* A pathway with named audiences and mechanisms beats a paragraph of "this will benefit society."

4. **Plan activities and partners.** The actual things you'll do — stakeholder engagement, open data, practitioner workshops, policy briefs, code releases, public communication — and any partners already lined up. Tie activities to budget lines and WP deliverables so they're real, not aspirational.

5. **Calibrate to the science.** Impact claims must be proportional to what the project can deliver. Over-claiming ("this will transform healthcare") reads as naive; a precise, bounded claim reads as credible.

6. **Write `proposal/sections/impact.tex`.** Lead with the most credible, highest-value pathway. For NWO, structure to the call's knowledge-utilisation prompts explicitly.

## Outputs

- `proposal/sections/impact.tex`.
- Summary block: the impact pathways by kind, the planned activities, and whether each has a budget/WP home.

## Anti-patterns to refuse

- **Impact as slogans.** "Benefits society" with no mechanism is a non-answer. Name the audience and the channel.
- **Over-claiming.** Impact disproportionate to the science erodes credibility everywhere else.
- **Activities with no resource.** If a workshop or open-data plan isn't in the budget/WPs, it isn't real — wire it in or cut it.
- **Treating NWO knowledge utilisation as an afterthought.** It's weighted; give it the same care as the methodology.

## When to call other skills

- Before: `/objectives`.
- After: `/budget` (cost the activities), `/draft-section` for surrounding sections, `/panel-mock editor` to test whether the impact lands.
