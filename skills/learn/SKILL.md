---
name: learn
description: Appends a proposal-specific convention, decision, or panel assumption to .grantstack/learnings.jsonl so the drafting skills stop having to be told it twice. Use when the user says "remember that…", or when you find yourself being given the same fact about this proposal a second time.
argument-hint: "<fact to remember>"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:learn

**Stage:** power · **Voice:** memory

`$ARGUMENTS` is the fact to remember, free-form; this skill normalizes it. The learnings file is read by the drafting and review skills, so what goes in it shapes the prose.

## Procedure

1. **Classify the fact** as one of: `convention` (naming or usage — always the acronym, never the long title), `decision` (a framing or design call, with its rationale), `panel` (an assumption about the panel or committee), `preference` (output or formatting), `reference` (a pointer to something specific to this proposal — the call, a template, a host policy), or `other`.
2. **Check it belongs here.** If the fact is a config field — scheme, deadline, acronym, title, budget, status, PhD year — set it in `.grantstack/config.yaml` instead and say so; a value in two places drifts. If it is a non-obvious project decision, it belongs in the `decisions:` list in config, which is the proposal's decision log.
3. **Normalize:** strip whitespace, trim trailing punctuation, capitalize the sentence.
4. **Append a JSON line** to `.grantstack/learnings.jsonl`, with the date from `date +%F`:

   ```json
   {"date":"YYYY-MM-DD","kind":"<class>","fact":"<normalized fact>"}
   ```

5. **Echo back** what was written so the user can confirm it.
6. **Hint at scope.** If the fact generalizes across proposals — a writing habit, a scheme-wide rule, a tooling preference — say it is worth putting in global memory too, not only here.

## Outputs

- `.grantstack/learnings.jsonl` — one new line.
- Summary: the new line, plus the scope hint where it applies.

## Anti-patterns

- **Storing transient state.** "Currently editing the synopsis" is conversation context, not memory.
- **Storing what config owns.** A config field set in two places drifts, and the skills read config.
