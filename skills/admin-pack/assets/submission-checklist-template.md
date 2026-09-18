# Submission checklist — {ACRONYM}, {SCHEME}, deadline {YYYY-MM-DD}

Every row is PASS, FAIL, or WAIVED, and every row carries **evidence**: the
command run, the count, the file checked. A row with a verdict and no evidence
has not been checked. The proposal is not ready while any row is FAIL without
a waiver the user has explicitly acknowledged.

Requirements come from `.grantstack/call-spec.md`, captured from the actual
call. Rows the call does not require are deleted, not marked N/A, except where
noting the absence is itself useful.

## Eligibility

| Item | Verdict | Evidence |
|---|---|---|
| PhD date within the scheme window (incl. extensions claimed) | | date, window, extension grounds |
| Extension evidence held for every extension claimed | | documents on file |
| Prior/current grants compatible with this scheme | | |
| Host institution eligible and willing to host | | |

## Documents

| Item | Verdict | Evidence |
|---|---|---|
| Every mandatory part present | | file list |
| Page limit per part | | pages counted per part |
| Font, size, margins, line spacing per the call | | settings in `proposal/main.tex` |
| CV in the call's exact format | | |
| No metrics the call bars (JIF, h-index) in the CV | | grep result |
| Budget table complete and within the ceiling | | total vs ceiling |
| Data management plan / ethics self-assessment present | | |
| Ethics categories answered explicitly, including the "no" ones | | |
| AI-use disclosure as the call requires | | the call's rule, quoted |
| Host support / commitment letter signed | | date, signatory |
| Declarations and annexes the call lists | | |

## Cleanliness

| Item | Verdict | Evidence |
|---|---|---|
| No `TODO`, `UNCONFIRMED`, `[ACTION:` left in any submitted file | | grep count (must be 0) |
| No `\cite{TODO-` left | | grep count (must be 0) |
| No template placeholders (`ACRONYM --- TITLE`, `PI NAME`, `HOST INSTITUTION`) | | grep count (must be 0) |
| Acronym, title, duration, and budget total agree across all documents | | values compared |
| All figures and tables referenced in the text and legible in print | | |
| The PDF compiles from a clean checkout | | build command and result |

## Portal

| Item | Verdict | Evidence |
|---|---|---|
| Portal account and host authorisation in place | | |
| Fields that duplicate the proposal (abstract, lay summary, keywords) prepared | | |
| File formats and size limits met | | |
| Internal deadline (host research office) noted and met | | date |

## Verdict

**Verdict:** Ready / Not ready — N blocking items.
