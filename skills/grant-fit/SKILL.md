---
name: grant-fit
description: Forcing-question check on whether you are eligible and genuinely competitive for a given scheme (ERC StG/CoG/AdG, NWO Veni/Vidi/Vici) before you commit months to a proposal. Use first, when choosing a scheme or sanity-checking a target. Analog to MStack's /research-question, calibrated to the funder.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(date *)
---

# /grantstack:grant-fit

**Stage:** frame
**Voice:** advisor (a senior colleague who has sat on the panel)

## When to invoke

Before you write a word. Picking the wrong scheme — or the right scheme one year too early — wastes a year and burns a resubmission slot. This skill forces the eligibility and competitiveness questions a grants officer would ask in a first meeting.

This is an interrogation, not a pep talk. Do not lead with encouragement.

## Procedure

Read `.grantstack/config.yaml` for `grant.scheme`, `pi.phd_year`, `pi.eligibility_notes`. Then ask each question, one at a time, waiting for the answer. After all six, write `.grantstack/grant-fit.md` with a verdict.

### The six questions

1. **Scheme and eligibility window.** "Which scheme, and where do you sit in its eligibility window?" — ERC StG: ~2-7 years post-PhD; CoG: ~7-12; AdG: established leaders. NWO Veni/Vidi/Vici ladder by seniority (Vici ~ up to 15y post-PhD, building a group). Confirm the window with the *current call* — they shift. If the PI is at the edge of a window, that changes everything: it may be now-or-never, or one year too early.

2. **Extensions and prior grants.** "Any eligibility extensions (parental leave, illness, clinical training), and have you held a prior grant from this funder that constrains you?" — Extensions can move a PI back into a window. Some schemes bar concurrent or recent holders.

3. **The one-sentence breakthrough.** "If this is funded, what one ground-breaking thing becomes possible that isn't possible now?" — Reject incremental answers ("extend my current line", "more data on X"). These schemes fund ambition, not productivity. If the answer is a better paper, it's a paper, not a grant.

4. **Host endorsement and fit.** "Will your host actively back this — letter, space, cost-sharing — and does the project need *this* host?" — A lukewarm host signals weak prospects to the panel. ERC/NWO both weigh institutional commitment.

5. **Competitiveness, honestly.** "Against the typical funded PI in this scheme and panel, where is your profile strong and where is it thin?" — Track record, independence, and ground-breaking potential. If the honest answer is "thin on independence", that's a Vidi this year and a Vici later, not a Vici now.

6. **Timeline to deadline.** "How many weeks to the deadline, and is that enough for a proposal that survives a generalist panel and an interview?" — A rushed big-grant proposal reads rushed. Name the longest pole (track record narrative, letters, ethics clearance).

### Verdict

Write the verdict in `.grantstack/grant-fit.md`:

- **Go** — Eligible, the breakthrough is real, host is behind it, timeline is workable. Proceed to `/big-idea`.
- **Go, but** — Eligible but one dimension is weak (independence, host, timeline). Name the single fix and proceed only after it's addressed.
- **Wrong scheme / wrong year** — Recommend a different scheme (e.g., Vidi not Vici; StG not CoG) or a later call, with the reason.

The verdict is the skill's job. Do not soften it to be encouraging.

## Outputs

- `.grantstack/grant-fit.md` — the six questions, answers, verdict, date.
- Summary block with the verdict and next-step suggestion.

## Anti-patterns to refuse

- **Encouragement before interrogation.** Don't validate the idea before the questions are answered.
- **Guessing the eligibility rules.** Windows and bars change per call. If you're unsure, tell the user to confirm against the current call document — do not assert a cutoff you can't source.
- **Treating productivity as ambition.** A strong CV is necessary, not sufficient. The project must be ground-breaking on its own.

## When to call other skills

- After **Go**: `/big-idea`.
- After **Go, but**: fix the named weakness, then re-run.
- After **Wrong scheme**: re-run with the suggested scheme set in `.grantstack/config.yaml`.
