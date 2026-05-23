---
name: learn
description: Append a per-proposal convention or fact to .grantstack/learnings.jsonl. Use to teach Claude the acronym, the panel assumptions, framing decisions, scheme-specific preferences. One JSON object per line — append-only.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(date *)
---

# /grantstack:learn

**Stage:** power
**Voice:** memory

## When to invoke

Whenever you find yourself telling Claude the same proposal-specific fact twice. The convention belongs in the proposal's memory, not in your head.

## Argument

`$ARGUMENTS` — the fact to remember. Free-form text; this skill will normalize it.

## Procedure

1. **Classify the fact** into one of:
   - `convention` — naming or usage convention (e.g., always use the acronym, not the long title).
   - `decision` — a framing or design decision (with rationale).
   - `panel` — an assumption about the panel/committee (e.g., generalist social scientists, not your subfield).
   - `preference` — output / formatting / style preference.
   - `reference` — pointer to an external resource specific to this proposal (the call, a template, a host policy).
   - `other` — free-form.

2. **Normalize.** Strip whitespace; trim trailing punctuation; capitalize the sentence.

3. **Append a JSON line** to `.grantstack/learnings.jsonl`:

   ```json
   {"date":"YYYY-MM-DD","kind":"<class>","fact":"<normalized fact>"}
   ```

4. **Echo back** what was written so the user can confirm.

5. **Hint at scope.** If the fact looks like it generalizes across proposals (a writing habit, a scheme-wide rule, a tooling preference), tell the user to consider also writing it to global memory rather than only here.

## Outputs

- `.grantstack/learnings.jsonl` — one new line.
- Summary: the new line + scope hint if applicable.

## Anti-patterns to refuse

- **Storing transient state.** "Currently editing the synopsis" is conversation context, not memory. Don't write it.
- **Storing what's already in config.** If it's a config field (scheme, deadline, acronym), set it there, not in learnings.

## When to call other skills

- If the fact crosses proposals, suggest writing to global memory rather than just here.
