#!/usr/bin/env bash
# Meta Loop Protocol — PreToolUse Hook (Windows compatible)
# Checks PROGRESS.md status before Edit/Write/MultiEdit
# Injects warning to stderr if progress tracking is stale or missing

# Windows Git Bash path handling
MSYS_NO_PATHCONV=1
PROJECT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
META_DIR="$PROJECT_ROOT/.meta-loop"
PROGRESS="$META_DIR/PROGRESS.md"

# Skip silently if meta-loop not initialized
[ ! -d "$META_DIR" ] && exit 0

# Check PROGRESS.md exists
if [ ! -f "$PROGRESS" ]; then
  echo "[Meta Loop] PROGRESS.md not found. Record iteration objective in PROGRESS.md before modifying code." >&2
  exit 0
fi

# Check for current iteration objective marker
# Requires explicit objective markers — generic terms excluded to avoid false positives
if ! grep -qE "(## Current Iteration Objective|## Iteration [0-9]|현재 이터레이션 목적)" "$PROGRESS" 2>/dev/null; then
  echo "[Meta Loop] PROGRESS.md has no iteration objective. Record what this iteration will accomplish before modifying code." >&2
  exit 0
fi

# Check staleness (30 min threshold) — GNU find via Git Bash
if command -v find >/dev/null 2>&1; then
  STALE=$(find "$PROGRESS" -mmin +30 2>/dev/null)
  if [ -n "$STALE" ]; then
    echo "[Meta Loop] PROGRESS.md has not been updated in 30+ minutes. Update it if starting a new iteration." >&2
  fi
fi

exit 0
