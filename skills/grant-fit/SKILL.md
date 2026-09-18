---
name: grant-fit
description: Interrogates whether you are eligible and genuinely competitive for a scheme (ERC StG/CoG/AdG, NWO Veni/Vidi/Vici) with six forcing questions, and issues a go / go-but / wrong-scheme verdict. Use when the user is choosing a scheme, wondering whether this is the right year to apply, or sanity-checking a target before committing months to it.
allowed-tools:
  - Read
  - Write
  - Bash(date *)
---

# /grantstack:grant-fit

**Stage:** frame · **Voice:** advisor (a senior colleague who has sat on the panel)

Before you write a word. Picking the wrong scheme — or the right scheme one year too early — wastes a year and can burn a resubmission slot. An interrogation, not a pep talk: do not lead with encouragement.

## Procedure

1. **Load** `.grantstack/config.yaml` (`grant.scheme`, `pi.phd_year`, `pi.eligibility_notes`), `.grantstack/call-spec.md` if it exists, and `${CLAUDE_PLUGIN_ROOT}/references/schemes.md` for how the scheme is shaped — windows, steps, who interviews, what the criteria are. Every number there is order of magnitude: the call is the contract, so where a captured spec exists it wins, and where neither exists say so rather than asserting a cutoff.
2. **Ask the six questions.** In a live session ask one at a time, offering the option to answer all six in one message; in an asynchronous context (web/mobile, or a user who is clearly batching) present all six together rather than forcing six round-trips. Take what `config.yaml` and the conversation already answer; do not re-ask.

   1. **Scheme and eligibility window.** "Which scheme, and where do you sit in its window?" A PI at the edge of a window changes everything: it may be now-or-never, or one year too early.
   2. **Extensions and prior grants.** "Any eligibility extensions — parental leave, illness, clinical training — and have you held a grant from this funder that constrains you?" Extensions move PIs back into windows; prior grants bar some combinations.
   3. **The one-sentence breakthrough.** "If this is funded, what ground-breaking thing becomes possible that isn't possible now?" Reject incremental answers ("extend my current line", "more data on X"). If the answer is a better paper, it is a paper.
   4. **Host endorsement and fit.** "Will your host actively back this — letter, space, cost-sharing — and does the project need *this* host?" A lukewarm host signals weak prospects to a panel.
   5. **Competitiveness, honestly.** "Against the typical funded PI in this scheme and panel, where is your profile strong and where is it thin?" If the honest answer is "thin on independence", that is a Vidi this year and a Vici later. Note where the scheme gates on the person before the project — an NWO pre-proposal weighs the researcher heavily, so a track record that will not clear that bar means the project's brilliance is never reached.
   6. **Timeline to deadline.** "How many weeks to the deadline, and is that enough for a proposal that survives a generalist panel and an interview?" Name the longest pole: track-record narrative, host letter, ethics clearance.

3. **Write** `.grantstack/grant-fit.md` — the questions, the answers, the date from `date +%F`, and the verdict. Write it even when answers are partial, marking the open questions; a half-answered interrogation on disk beats nothing.

   **Verdict**, the first line of the file:
   - **Go** — eligible, the breakthrough is real, the host is behind it, the timeline is workable.
   - **Go, but** — eligible with one weak dimension (independence, host, timeline). Name the single fix.
   - **Wrong scheme / wrong year** — recommend a different scheme (Vidi not Vici; StG not CoG) or a later call, with the reason.

   The verdict is the skill's job. Do not soften it to be encouraging.

## Outputs

- `.grantstack/grant-fit.md` — questions, answers, verdict, date.
- Summary block: the verdict and the one thing that decided it.

## Anti-patterns

- **Encouragement before interrogation.** Do not validate the idea before the questions are answered.
- **Guessing the eligibility rules.** Windows and bars change per call and per domain. Where `references/schemes.md` and the captured call disagree, the call wins; where neither covers it, say so.
- **Treating productivity as ambition.** A strong CV is necessary, not sufficient; the project must be ground-breaking on its own.

## Next

**Go** → `/grantstack:big-idea`. **Go, but** → fix the named weakness and re-run. **Wrong scheme** → set the new scheme in `.grantstack/config.yaml` and re-run.
