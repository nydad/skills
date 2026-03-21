#!/usr/bin/env bash
# Meta Loop Protocol — Stop Hook (Windows compatible)

MSYS_NO_PATHCONV=1

ROOT="$PWD"
while [ "$ROOT" != "/" ] && [ "$ROOT" != "" ] && [ ! -d "$ROOT/.meta-loop" ]; do
  ROOT="$(dirname "$ROOT")"
done

[ ! -d "$ROOT/.meta-loop" ] && exit 0

cat <<'EOF'
{
  "additionalContext": "[Meta Loop Checkpoint] Iteration ending. Before finishing, verify:\n1. PROGRESS.md updated with this iteration's results\n2. Decisions recorded in DECISIONS.md\n3. Next iteration's task specified in PROGRESS.md\n4. Consider /compact if context is long"
}
EOF
exit 0
