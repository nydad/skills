---
name: meta-loop-protocol
description: "Meta Loop Protocol — Judgment framework for long-running autonomous /loop tasks. Installs hook scripts and external memory files to prevent Context Drift, Monotonic Escalation, Literal Execution, and Session Amnesia in AI coding agents. Windows (Git Bash) compatible."
user-invocable: true
disable-model-invocation: true
---

# Meta Loop Protocol

A framework that transforms the agent from an **executor into a judge** during long-running autonomous /loop tasks.

## The Problem

When an agent iterates through loop-based autonomous work, it falls into four structural failure modes:

| Failure Mode | Symptom | Solution |
|-------------|---------|----------|
| Context Drift | Modified code becomes the new baseline; agent forgets original state | BASELINE.md — immutable snapshot, always compare against origin |
| Monotonic Escalation | "Improve" = "increase numbers"; values only go up, never down | Self-Audit — detect inflation patterns, self-verify and recalibrate |
| Literal Execution | Agent does exactly what's asked, fails to internalize design intent | WHY.md — anchor purpose and philosophy, referenced every iteration |
| Session Amnesia | Session reset loses judgment context, not just text | PROGRESS.md + DECISIONS.md — relay baton between sessions |

## How It Works

- **Phase 1 (Setup)**: First invocation → install hook scripts + initialize external memory
- **Phase 2 (Runtime)**: Every loop iteration → follow the protocol

If `.meta-loop/` directory already exists, skip Setup and go directly to Runtime.

---

## Phase 1: Setup

### Step 1 — Install Hook Scripts

Read the 3 hook scripts from this skill's `scripts/` directory and copy them to the project's `.claude/hooks/`.

| File | Event | Purpose |
|------|-------|---------|
| check-progress.sh | PreToolUse (Edit\|Write\|MultiEdit) | Warn if PROGRESS.md not updated before code changes |
| checkpoint.sh | Stop | Remind to checkpoint progress at iteration end |
| audit-trigger.sh | PostToolUse (Edit\|Write\|MultiEdit) | Trigger self-audit every N file edits |

Steps:
1. Create `.claude/hooks/` directory if it doesn't exist
2. Read all 3 files from this skill's `scripts/` directory
3. Write them to the project's `.claude/hooks/`

> **Note**: Windows environment — `chmod` is not required. Git Bash executes .sh files directly.

### Step 2 — Register Hooks in settings.json

Read the project's `.claude/settings.json` (or start with `{}` if absent).
**Merge** the following hooks config — append to existing arrays, never overwrite existing hooks.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [{"type": "command", "command": "bash .claude/hooks/check-progress.sh"}]
      }
    ],
    "Stop": [
      {
        "hooks": [{"type": "command", "command": "bash .claude/hooks/checkpoint.sh"}]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [{"type": "command", "command": "bash .claude/hooks/audit-trigger.sh"}]
      }
    ]
  }
}
```

### Step 3 — Initialize External Memory

Create `.meta-loop/` directory at project root with these files:

#### WHY.md (North Star — immutable)

**Do NOT fill this in autonomously.** Interview the user to co-create it:

- "What is the fundamental reason for this work?"
- "What does success look like?"
- "What principles are non-negotiable?"
- "What are the boundaries of scope?"

This file is the agent's north star. Once written, never modify it.

#### BASELINE.md (Origin Snapshot — immutable)

Perform a full survey of the current project state and record:

- Directory/file structure
- Key numeric values and settings (balance values, performance metrics, etc.)
- Core architecture and patterns
- Known issues

This is the "original state" reference. Once written, never modify it.

#### PROGRESS.md (Relay Baton)

```markdown
# Progress Log

## Plan
(Priorities agreed with user)

## Current Status
Setup complete. Work not yet started.

## Next Iteration
(First work item)
```

#### DECISIONS.md (Decision Log)

Records "chose A over B because..." — prevents repeating or reversing decisions across sessions.

#### AUDIT.md (Audit Log)

Records delta analysis against BASELINE, inflation detection, and direction correction history.

#### .meta-loop/.gitignore

Add `.edit-counter` to gitignore (ephemeral counter file).

### Step 4 — Loop Prompt Template

Read `references/loop-prompt-template.md` from this skill and copy it to `.meta-loop/loop-prompt.md`.
Leave a placeholder at the end for the user to add project-specific work instructions.

### Step 5 — User Instructions

After setup, inform the user:

1. **Session restart required** — Hooks load at session start. Exit and restart for hooks to activate.
2. **Usage**: Add specific tasks to `.meta-loop/loop-prompt.md`, then run `/loop 5m cat .meta-loop/loop-prompt.md`
3. **Audit frequency**: Adjustable via `META_LOOP_AUDIT_THRESHOLD` env var (default: every 10 file edits)

---

## Phase 2: Runtime

If `.meta-loop/` exists, skip Setup and start here.

For detailed protocol see `references/runtime-protocol.md`. For self-audit procedure see `references/self-audit.md`.

### Iteration Protocol Summary

1. **Read WHY.md** → confirm purpose
2. **Read PROGRESS.md** → understand where things stand and what's next
3. **Read DECISIONS.md** → review prior judgments to avoid repetition/reversal
4. **Compare BASELINE.md vs current state** → compute delta
5. **Record this iteration's objective in PROGRESS.md** → then begin work
6. **Record judgments in DECISIONS.md** at every decision point
7. **Update PROGRESS.md** on completion → specify next task
8. **Run /compact autonomously** if context is growing long

### Core Judgment Principles

At every decision point, evaluate:

- "Does this change align with WHY.md's intent?"
- "Is this direction correct relative to BASELINE?"
- "Are values only going up (inflation pattern)?"
- "Should work continue, or stop for self-verification?"

Do not make changes that deviate from WHY.md's intent.
If monotonic escalation is detected, stop and recalibrate against BASELINE.
For complex changes, use subagents to separate Writer and Reviewer roles.
Use /compact, /simplify, and other slash commands autonomously.
Resources are unlimited — full project re-analysis every iteration is acceptable if it serves accuracy.

### Self-Audit

Hooks auto-trigger every N file edits. Details in `references/self-audit.md`.

---

## Deactivation / Cleanup

To remove the protocol from a project:

1. Delete hook entries from `.claude/settings.json` (the 3 PreToolUse/Stop/PostToolUse entries added in Step 2)
2. Delete `.claude/hooks/check-progress.sh`, `checkpoint.sh`, `audit-trigger.sh`
3. Optionally delete `.meta-loop/` directory (or keep as historical record)
4. Restart the session for hook changes to take effect
