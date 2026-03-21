#!/usr/bin/env bash
# Meta Loop Protocol — PostToolUse Hook (Windows compatible)

MSYS_NO_PATHCONV=1

ROOT="$PWD"
while [ "$ROOT" != "/" ] && [ "$ROOT" != "" ] && [ ! -d "$ROOT/.meta-loop" ]; do
  ROOT="$(dirname "$ROOT")"
done
META_DIR="$ROOT/.meta-loop"
COUNTER_FILE="$META_DIR/.edit-counter"
THRESHOLD=${META_LOOP_AUDIT_THRESHOLD:-10}

[ ! -d "$META_DIR" ] && exit 0

[ ! -f "$COUNTER_FILE" ] && echo "0" > "$COUNTER_FILE"
COUNT=$(cat "$COUNTER_FILE" 2>/dev/null || echo "0")
COUNT=$((COUNT + 1))
echo "$COUNT" > "$COUNTER_FILE"

if [ "$COUNT" -ge "$THRESHOLD" ]; then
  echo "0" > "$COUNTER_FILE"
  cat <<'EOF'
{
  "additionalContext": "[Meta Loop Self-Audit Trigger] File edit count reached threshold. Perform Self-Audit now:\n1. Re-read BASELINE.md and compute delta against current state\n2. Check for monotonic escalation (inflation) in numeric values\n3. Verify alignment with WHY.md intent\n4. Use a subagent for independent Writer/Reviewer review if possible\n5. Record results in AUDIT.md\n6. If direction has drifted: self-verify and re-establish direction autonomously (do NOT wait for user)"
}
EOF
fi

exit 0
