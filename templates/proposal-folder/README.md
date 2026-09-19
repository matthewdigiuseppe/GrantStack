# {ACRONYM} — {PROJECT TITLE}

Scaffolded by [GrantStack](https://github.com/matthewdigiuseppe/GrantStack).

## Layout

```
.grantstack/      # GrantStack config + learnings + caches (do not delete)
  config.yaml     # scheme, deadline, acronym, budget, status — every skill reads it
  audits/         # dated feasibility audits
  review-cache/   # dated panel-mock and mentor-review reports
proposal/         # the proposal: main.tex + sections/
  sections/       # synopsis, state-of-art, objectives, methodology,
                  # workpackages, feasibility, pi-track-record, impact,
                  # data-management, ethics, and lay-summary (a portal field,
                  # not \input by main.tex)
  refs.bib        # cited works — never auto-invented
budget/           # budget table + justification, aligned to work packages
cv/               # PI track record / CV narrative
admin/            # DMP and ethics annexes; eligibility and host-support letters
  call/           # the call / work programme as published — read-only once here
reviews/
  received/       # referee reports, panel letters, evaluation summaries as
                  # received — read-only once here; the record of what was said
  rebuttal/       # your replies (NWO grants a written rebuttal; ERC does not)
  interview/      # pitch, slide outline, question bank
```

`admin/call/` and `reviews/received/` are enforced read-only by GrantStack's
guard hook: new files can be added, existing ones are never edited. Corrections
belong in the spec, the rebuttal, or the retro — never in the document as
received.

## Workflow

Start with `/grantstack:grant-fit` (am I eligible and competitive for this
scheme?) then `/grantstack:big-idea`. Walk the stages: frame → position →
design → write → stress-test → submit → defend → reflect. Lost the thread?
`/grantstack:proposal-status` reads this folder and names the one next step.
See the GrantStack README for the full command map.

## The two readers

Everything in `proposal/` is written for two people at once: the **generalist
panel member** who is not in your subfield and decides your fate, and the
**in-field referee** who reads the methodology deeply. The synopsis and lay
summary serve the first; the methodology and work packages serve the second.
