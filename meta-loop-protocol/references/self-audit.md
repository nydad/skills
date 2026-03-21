# Self-Audit Routine

This document describes the detailed self-audit procedure for Meta Loop Protocol.

## Trigger Conditions

Self-audit is triggered by:

1. **Automatic**: PostToolUse hook fires when file edit count reaches threshold (default: 10)
2. **Autonomous**: Agent judges it necessary on its own (actively encouraged)

## Procedure

### 1. Re-read BASELINE

Read `.meta-loop/BASELINE.md`. This is the immutable snapshot of the original state.

### 2. Delta Analysis

Compare current project state against BASELINE:

- Number of changed files and magnitude of changes
- Numeric value / setting changes (if any)
- Newly added code/files
- Deleted code/files
- Structural changes

### 3. Inflation Check

Read DECISIONS.md and PROGRESS.md to trace the history of value changes:

- Are values consistently moving in one direction (increasing)?
- Is "making it better" actually destroying balance?
- Is raising one value triggering cascading increases in others?

When inflation is detected:
1. Stop changes immediately
2. Re-evaluate against BASELINE's original values
3. Ask fundamentally: "Does this value truly need to be higher?"
4. If not, revert toward BASELINE values
5. Record findings in AUDIT.md

### 4. Direction Check

Compare current work direction against WHY.md's purpose/philosophy:

- Has any change deviated from the original intent?
- Am I rationalizing with "it wasn't asked for, but it's a good change"?
- Have I crossed boundaries the user explicitly set?

### 5. Independent Review (subagent)

Use a separate subagent whenever possible:

- Have it independently review the current agent's work
- Judge "does this change align with WHY.md intent?" from an external perspective
- Writer/Reviewer separation minimizes bias
- Resources are unlimited — do not hesitate to use subagents

### 6. Record Results

Record in AUDIT.md using this format:

```markdown
## Audit [date/time] — Iteration N

### Delta Analysis
- Files changed from BASELINE: X
- Key value changes: (specifics)

### Inflation Check
- Monotonic increase pattern: detected / not detected
- (If detected) affected values, analysis, corrective action

### Direction Check
- WHY.md alignment: aligned / drifted
- (If drifted) drift details, analysis, corrected direction

### Verdict
- Continue as-is / Direction re-established after correction
- (If corrected) new direction and rationale
```

### 7. On Drift Detection — Autonomous Correction

If any of the following conditions are met, self-verify and re-establish direction:

- Values have shifted 50%+ from BASELINE
- Changes contradict WHY.md's core principles
- Inflation pattern detected 3+ consecutive times
- Subagent review reports serious issues

**Do NOT alert the user and wait.** Instead:

1. Record in AUDIT.md with "[DIRECTION RESET]" tag
2. Re-read WHY.md to reconfirm original intent
3. Analyze the cause of drift
4. Establish corrected direction
5. Update PROGRESS.md with revised plan
6. Resume work on corrected course

The agent is fully responsible for detecting and resolving problems autonomously.
