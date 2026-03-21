#!/usr/bin/env bash
# Meta Loop Protocol — Stop Hook (Windows compatible)
# Reminds agent to checkpoint progress at iteration end

MSYS_NO_PATHCONV=1
PROJECT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
META_DIR="$PROJECT_ROOT/.meta-loop"

[ ! -d "$META_DIR" ] && exit 0

cat <<'EOF'
{
  "additionalContext": "[Meta Loop Checkpoint] Iteration ending. Before finishing, verify:\n1. PROGRESS.md updated with this iteration's results\n2. Decisions recorded in DECISIONS.md\n3. Next iteration's task specified in PROGRESS.md\n4. Consider /compact if context is long"
}
EOF
exit 0
