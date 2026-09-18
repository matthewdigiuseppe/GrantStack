---
name: impact
description: Builds the impact / knowledge-utilisation pathway — scientific, societal and economic — with named audiences, the activity that reaches each, and a budget and work-package home for every activity. Writes proposal/sections/impact.tex. Use once the objectives and expected results are clear; mandatory and separately weighted in NWO, and a synopsis-strengthener in ERC.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:impact

**Stage:** design · **Voice:** impact strategist — a credible planner, not a marketer

In NWO schemes **knowledge utilisation** is a separately weighted, mandatory criterion that applicants routinely under-serve; a thin section costs real points. In ERC the case is excellence-first, but a broader-impact framing still strengthens the synopsis. Build a pathway, not slogans.

## Procedure

1. **Load** `proposal/sections/objectives.tex`, `.grantstack/big-idea.md`, `.grantstack/config.yaml`, `.grantstack/call-spec.md` (how this call defines and weights impact), the impact bar in `${CLAUDE_PLUGIN_ROOT}/references/proposal-conventions.md`, and the scheme's criteria in `${CLAUDE_PLUGIN_ROOT}/references/schemes.md`.
2. **Separate the kinds of impact:**
   - **Scientific** — the fields, methods, and communities the results advance, and how the knowledge travels (datasets, tools, theory others build on).
   - **Societal** — concrete beneficiaries (policy, clinical practice, industry, public, specific communities) and what changes for them.
   - **Economic** — where relevant: applications, IP, spin-out potential, cost savings.
3. **Build the pathway, not the promise.** For each impact trace *result → who needs it → how it reaches them → what they do differently*. Named audiences and mechanisms beat a paragraph of "this will benefit society".
4. **Plan activities and partners** — stakeholder engagement, open data, practitioner workshops, policy briefs, code releases, public communication — and any partners already lined up. Tie each to a budget line and a WP deliverable so it is real rather than aspirational.
5. **Calibrate to the science.** Claims must be proportional to what the project can deliver; over-claiming ("this will transform healthcare") reads as naive, a precise bounded claim reads as credible.
6. **Write `proposal/sections/impact.tex`**, leading with the most credible, highest-value pathway. For NWO, structure it to the call's knowledge-utilisation prompts explicitly.

## Outputs

- `proposal/sections/impact.tex`.
- Summary block: the pathways by kind, the planned activities, and whether each has a budget and WP home.

## Anti-patterns

- **Impact as slogans.** "Benefits society" with no mechanism is a non-answer; name the audience and the channel.
- **Over-claiming.** Impact disproportionate to the science erodes credibility everywhere else.
- **Activities with no resource.** If a workshop or open-data plan is not in the budget and WPs, it is not real — wire it in or cut it.
- **Treating NWO knowledge utilisation as an afterthought.** It is weighted; give it the care the methodology gets.

## Next

`/grantstack:budget` to cost the activities, and `/grantstack:panel-mock chair` to test whether the impact lands.
