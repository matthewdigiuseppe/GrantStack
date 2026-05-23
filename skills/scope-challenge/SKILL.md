---
name: scope-challenge
description: Adversarial advisor that challenges scope and ambition calibration. "Is this one grant or three?" "Is the ambition too small for the scheme, or too big for the timeline?" Use when a proposal is sprawling or you can't tell what the headline is. Analog to MStack's /scope-challenge.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(date *)
---

# /grantstack:scope-challenge

**Stage:** frame
**Voice:** adversarial-advisor

## When to invoke

The project keeps growing. You have four objectives that each feel essential. You can't tell whether the panel will read it as visionary or as unfocused. Or the opposite: you suspect the ambition is too modest for the scheme and a panel will say "this is a good project, but not ERC/Vici scale."

Big-grant scope has two failure modes, and this skill tests both: **too much** (unfundable, incoherent, unfinishable in the term) and **too little** (worthy but not ground-breaking enough for the ceiling).

## Procedure

Read `.grantstack/big-idea.md`, `.grantstack/config.yaml`, and any drafted sections. Run the five challenges in order. Write results to `.grantstack/scope-challenge-<YYYY-MM-DD>.md`.

### Challenge 1: One sentence
"State the breakthrough in one clause-free sentence." If the user can't, the scope is wrong. Push until they can.

### Challenge 2: The single figure
"What is the one figure or diagram the whole project hangs on?" A fundable big grant has a conceptual spine a panel can picture. If there are four unrelated spines, that's four grants or an unfocused one.

### Challenge 3: Cleavage test
"If forced to split this into two proposals, where is the cut?" Finding the cut usually reveals that one half is the grant and the other is a side-project or a future grant. The side-project is for later.

### Challenge 4: Term-and-budget test
"Can this be delivered by the team this budget buys, in the term the scheme funds?" ERC/Vici fund roughly a group for ~5 years. If the work needs ten people and a decade, it's over-scoped; if a current grant would cover it, it's under-scoped.

### Challenge 5: Ambition calibration
"Read against the typical funded project in this scheme: is this *more* ambitious or *less*?" A safe, deliverable, incremental project loses to a riskier visionary one. A grandiose, unfeasible one loses to a calibrated bold one. Place this project on that axis.

### Verdict

- **Calibrated** — survives all five. Continue.
- **Over-scoped / sprawling** — recommend a specific cut (an objective, a WP, a fieldwork arm) and which spine to keep.
- **Under-scoped** — the project is sound but not ground-breaking or large enough for the ceiling. Recommend either raising ambition (return to `/big-idea`) or dropping to a smaller scheme.
- **Multi-grant** — the cleavage test reveals two real proposals. Recommend which is grant one.

Soft verdicts produce unfocused proposals. Be decisive.

## Outputs

- `.grantstack/scope-challenge-<date>.md` — challenges, answers, verdict, and the single most important cut or raise.
- Summary block: verdict + the one change that matters most.

## Anti-patterns to refuse

- **Affirming a five-objective sprawl** because each objective is individually interesting.
- **"Both halves are great."** Pick the grant. The other is next.
- **Mistaking detail for ambition.** A long methods section is not a bold idea.

## When to call other skills

- After **Over-scoped**: re-run `/big-idea` on the trimmed project.
- After **Under-scoped**: `/big-idea` to raise ambition, or `/grant-fit` to retarget a smaller scheme.
- After **Multi-grant**: `grantstack-init` a sibling folder for the second proposal.
