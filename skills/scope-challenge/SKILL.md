---
name: scope-challenge
description: Adversarially tests whether the scope is calibrated for the scheme — one grant or three, too big for the term or too modest for the ceiling — through five challenges, and names the single cut or raise that matters. Use when the proposal is sprawling, when every objective feels essential, or when the user cannot tell whether a panel will read it as visionary or unfocused.
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Bash(date *)
---

# /grantstack:scope-challenge

**Stage:** frame · **Voice:** adversarial-advisor

Big-grant scope fails in two directions and this skill tests both: **too much** (incoherent, unfinishable in the term) and **too little** (worthy, but not ground-breaking enough for the ceiling).

## Procedure

1. **Load** `.grantstack/big-idea.md`, `.grantstack/config.yaml`, the scheme's term and ceiling from `${CLAUDE_PLUGIN_ROOT}/references/schemes.md`, and any drafted sections in `proposal/sections/`.
2. **Run the five challenges** in order — one at a time in a live session, all five at once when the user is not in a live back-and-forth. Take answers the memos already give.

   1. **One sentence.** "State the breakthrough in one clause-free sentence." If the user cannot, the scope is wrong. Push until they can.
   2. **The single figure.** "What is the one figure or diagram the whole project hangs on?" A fundable big grant has a conceptual spine a panel can picture. Four unrelated spines is four grants, or one unfocused one.
   3. **Cleavage test.** "If forced to split this into two proposals, where is the cut?" Finding the cut usually reveals that one half is the grant and the other is a future grant.
   4. **Term-and-budget test.** "Can this be delivered by the team this budget buys, in the term the scheme funds?" If it needs ten people and a decade, it is over-scoped; if a current grant would cover it, it is under-scoped.
   5. **Ambition calibration.** "Against the typical funded project in this scheme: more ambitious, or less?" A safe deliverable project loses to a riskier visionary one; a grandiose unfeasible one loses to a calibrated bold one. Place this project on that axis.

3. **Write** `.grantstack/scope-challenge-<YYYY-MM-DD>.md` (date from `date +%F`) with the challenges, the answers, and the verdict.

   **Verdict**, the first line of the file:
   - **Calibrated** — survives all five.
   - **Over-scoped / sprawling** — name the specific cut (an objective, a WP, a fieldwork arm) and which spine to keep.
   - **Under-scoped** — sound but not ground-breaking or large enough for the ceiling; raise the ambition or drop to a smaller scheme.
   - **Multi-grant** — the cleavage test found two real proposals; say which is grant one.

   Soft verdicts produce unfocused proposals. Be decisive.

4. **Log the cut.** If a cut or raise is decided, append it to `decisions:` in `.grantstack/config.yaml`.

## Outputs

- `.grantstack/scope-challenge-<date>.md` — challenges, answers, verdict, and the one cut or raise that matters most.
- Summary block: verdict + that single change.

## Anti-patterns

- **Affirming a five-objective sprawl** because each objective is individually interesting.
- **"Both halves are great."** Pick the grant; the other is next.
- **Mistaking detail for ambition.** A long methods section is not a bold idea.

## Next

**Over-scoped** → re-run `/grantstack:big-idea` on the trimmed project. **Under-scoped** → `/grantstack:big-idea` to raise ambition, or `/grantstack:grant-fit` to retarget. **Multi-grant** → `/grantstack:grantstack-init` a sibling folder for the second proposal.
