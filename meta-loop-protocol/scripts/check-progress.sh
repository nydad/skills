#!/usr/bin/env bash
# Meta Loop Protocol — PreToolUse Hook (Windows compatible)
# Checks PROGRESS.md status before Edit/Write/MultiEdit

MSYS_NO_PATHCONV=1

# Find project root by walking up looking for .meta-loop/
ROOT="$PWD"
while [ "$ROOT" != "/" ] && [ "$ROOT" != "" ] && [ ! -d "$ROOT/.meta-loop" ]; do
  ROOT="$(dirname "$ROOT")"
done
META_DIR="$ROOT/.meta-loop"
PROGRESS="$META_DIR/PROGRESS.md"

[ ! -d "$META_DIR" ] && exit 0

if [ ! -f "$PROGRESS" ]; then
  echo "[Meta Loop] PROGRESS.md not found. Record iteration objective before modifying code." >&2
  exit 0
fi

if ! grep -qE "(## Current Iteration Objective|## Iteration [0-9]|현재 이터레이션 목적)" "$PROGRESS" 2>/dev/null; then
  echo "[Meta Loop] PROGRESS.md has no iteration objective. Record what this iteration will accomplish." >&2
  exit 0
fi

if command -v find >/dev/null 2>&1; then
  STALE=$(find "$PROGRESS" -mmin +30 2>/dev/null)
  if [ -n "$STALE" ]; then
    echo "[Meta Loop] PROGRESS.md not updated in 30+ min. Update if starting new iteration." >&2
  fi
fi

exit 0
