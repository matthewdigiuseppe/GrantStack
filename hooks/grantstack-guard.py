#!/usr/bin/env python3
"""GrantStack PreToolUse guard.

Enforces, inside any GrantStack proposal folder (a directory tree containing
.grantstack/):

  1. Received documents are read-only once they exist: the call as published
     (admin/call/) and the referee reports, panel letters, and evaluation
     summaries as received (reviews/received/) are never edited, overwritten,
     or removed. New files may still be added (that is how
     /grantstack:call-spec and /grantstack:rebuttal take delivery of them).
     Always on; no toggle.
  2. /grantstack:freeze — while .grantstack/safety.yaml sets freeze.path,
     writes are denied outside that directory (.grantstack/ itself stays
     writable so /grantstack:unfreeze can clear the lock).
  3. /grantstack:careful — while careful: true, destructive commands and
     whole-file overwrites of proposal/budget/CV/admin/review files require
     explicit user confirmation (surfaced as a permission prompt).

Outside a GrantStack proposal folder the hook is a no-op. Denials exit 2
(stderr is fed back to Claude); confirmations emit the PreToolUse "ask"
decision. The hook is a backstop, not a sandbox — Bash analysis is
best-effort pattern matching, and the skills carry the same rules as
instructions.
"""
import json
import re
import sys
from pathlib import Path

FILE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
CAREFUL_DIRS = ("proposal", "budget", "cv", "admin", "reviews")

# Received documents: additions are fine, mutation of an existing file is not.
# Each entry is (path prefix, where the response actually belongs).
READ_ONLY_DIRS = (
    ("reviews/received/", "Answer it in reviews/rebuttal/; the report as received is the record."),
    ("admin/call/", "Re-capture with /grantstack:call-spec recapture; the call as published is the contract."),
)

DESTRUCTIVE_BASH = [
    (re.compile(r"(^|[;&|]\s*|\s)rm\s"), "rm"),
    (re.compile(r"git\s+reset\s+--hard"), "git reset --hard"),
    (re.compile(r"git\s+checkout\s+--\s"), "git checkout --"),
    (re.compile(r"git\s+clean\s+-\w*f"), "git clean -f"),
    (re.compile(r"push\s+(\S+\s+)*(--force\b|--force-with-lease\b|-f\b)"), "force push"),
    (re.compile(r"sed\s+(-\w+\s+)*-i"), "sed -i"),
    (re.compile(r"\btruncate\s"), "truncate"),
]
MUTATING_BASH = DESTRUCTIVE_BASH + [
    (re.compile(r"(^|[;&|]\s*|\s)mv\s"), "mv"),
    (re.compile(r"(^|[;&|]\s*|\s)cp\s"), "cp"),
    (re.compile(r"\btee\s"), "tee"),
    (re.compile(r">>?\s*\S"), "shell redirection"),
]


def allow():
    sys.exit(0)


def deny(reason):
    print(f"GrantStack guard: {reason}", file=sys.stderr)
    sys.exit(2)


def ask(reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": f"GrantStack careful mode: {reason}",
        }
    }))
    sys.exit(0)


def find_project(start):
    """Walk up from `start` to the nearest directory containing .grantstack/."""
    try:
        p = Path(start).resolve()
    except OSError:
        return None
    for candidate in [p, *p.parents]:
        if (candidate / ".grantstack").is_dir():
            return candidate
    return None


def read_safety(project):
    """Parse .grantstack/safety.yaml without a YAML dependency.

    Understands the flat and two-level forms the safety skills write:
      careful: true
      freeze:
        path: "reviews/rebuttal"
      freeze.path: reviews/rebuttal
    """
    cfg = {"careful": False, "freeze_path": ""}
    f = project / ".grantstack" / "safety.yaml"
    try:
        text = f.read_text()
    except OSError:
        return cfg
    section = None
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indented = raw[:1] in (" ", "\t")
        line = raw.strip()
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip().strip("\"'")
        if not indented:
            section = key if not value else None
            if key == "careful":
                cfg["careful"] = value.lower() == "true"
            elif key == "freeze.path":
                cfg["freeze_path"] = value
        elif section == "freeze" and key == "path":
            cfg["freeze_path"] = value
    return cfg


def is_under(path, root):
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def bash_paths(command, cwd, project):
    """Best-effort: tokens of a Bash command that resolve inside the project."""
    hits = []
    for token in re.findall(r"[\w~$./-]+", command):
        if "/" not in token and token not in CAREFUL_DIRS:
            continue
        if token.startswith("-") or token.startswith("$"):
            continue
        candidate = Path(token).expanduser()
        if not candidate.is_absolute():
            candidate = Path(cwd) / candidate
        try:
            resolved = candidate.resolve()
        except OSError:
            continue
        if is_under(resolved, project):
            hits.append(resolved)
    return hits


def main():
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        allow()

    tool = event.get("tool_name", "")
    tool_input = event.get("tool_input") or {}
    cwd = event.get("cwd") or "."

    if tool in FILE_TOOLS:
        target = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
        if not target:
            allow()
        target = Path(target)
        if not target.is_absolute():
            target = Path(cwd) / target
        project = find_project(target.parent)
        if project is None:
            allow()
        rel = target.resolve().relative_to(project.resolve()) if is_under(target, project) else None
        if rel is None:
            allow()

        # Rule 1: received documents are immutable once they exist.
        if target.exists():
            for prefix, remedy in READ_ONLY_DIRS:
                if str(rel).startswith(prefix):
                    deny(f"{rel} is under {prefix}, which is read-only once the file "
                         f"exists. {remedy}")

        safety = read_safety(project)

        # Rule 2: freeze lock (exempting .grantstack/ so /grantstack:unfreeze works).
        fp = safety["freeze_path"]
        if fp and not str(rel).startswith(".grantstack"):
            freeze_root = Path(fp) if Path(fp).is_absolute() else project / fp
            if not is_under(target, freeze_root):
                deny(
                    f"freeze is active: writes are locked to {fp} (plus .grantstack/). "
                    f"{rel} is outside it. Run /grantstack:unfreeze to lift the lock."
                )

        # Rule 3: careful mode — confirm whole-file overwrites that hurt.
        if safety["careful"] and tool == "Write" and target.exists():
            top = rel.parts[0] if rel.parts else ""
            try:
                n_lines = sum(1 for _ in target.open(errors="ignore"))
                size = target.stat().st_size
            except OSError:
                n_lines, size = 0, 0
            if (top in CAREFUL_DIRS and size > 0) or n_lines >= 100:
                ask(f"overwriting existing {rel} ({n_lines} lines). Confirm before replacing it.")
        allow()

    if tool == "Bash":
        command = tool_input.get("command") or ""
        if not command:
            allow()
        project = find_project(cwd)
        if project is None:
            allow()
        safety = read_safety(project)

        # Rule 1: destructive commands touching a read-only directory.
        for prefix, remedy in READ_ONLY_DIRS:
            if prefix.rstrip("/") not in command:
                continue
            for pattern, label in DESTRUCTIVE_BASH:
                if pattern.search(command):
                    deny(f"'{label}' targets {prefix}, which is read-only once the "
                         f"files exist. {remedy}")

        # Rule 2: freeze lock for mutating commands.
        fp = safety["freeze_path"]
        if fp:
            freeze_root = Path(fp) if Path(fp).is_absolute() else project / fp
            mutates = next((label for pattern, label in MUTATING_BASH if pattern.search(command)), None)
            if mutates:
                targets = bash_paths(command, cwd, project)
                outside = [
                    t for t in targets
                    if not is_under(t, freeze_root) and not is_under(t, project / ".grantstack")
                ]
                if outside:
                    deny(
                        f"freeze is active (writes locked to {fp}) and this '{mutates}' touches "
                        f"{outside[0]}. Run /grantstack:unfreeze first."
                    )
                if not targets:
                    ask(f"freeze is active (locked to {fp}) and this '{mutates}' command's targets "
                        "could not be verified. Confirm it does not write outside the lock.")

        # Rule 3: careful mode — confirm destructive commands.
        if safety["careful"]:
            for pattern, label in DESTRUCTIVE_BASH:
                if pattern.search(command):
                    ask(f"'{label}' detected near a deadline-protected proposal. Confirm before running.")
            if re.search(r"(^|[;&|]\s*|\s)mv\s", command) and any(
                f"{d}/" in command for d in CAREFUL_DIRS
            ):
                ask("'mv' touches proposal/budget/CV/admin/review directories. Confirm before running.")
        allow()

    allow()


if __name__ == "__main__":
    main()
