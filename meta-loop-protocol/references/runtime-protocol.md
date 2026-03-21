# Runtime Protocol — Detailed

This document describes the detailed per-iteration protocol for Meta Loop Protocol.

## Iteration Start Procedure

Every iteration must follow this exact sequence. It cannot be skipped or reordered.

### 1. Context Restoration

```
Read: .meta-loop/WHY.md
Read: .meta-loop/PROGRESS.md
Read: .meta-loop/DECISIONS.md (recent entries)
Read: .meta-loop/AUDIT.md (latest audit result)
```

- WHY.md: Clarify "why am I doing this work?"
- PROGRESS.md: Understand "what was done so far, and what's next?"
- DECISIONS.md: Review "what judgments were made before?" to prevent repetition/reversal.

### 2. Delta Computation

Read BASELINE.md and compare against the current project state.
Calculate how much key values and structures have changed.
Use this comparison to establish "where am I now relative to the origin?"

### 3. Iteration Planning

Based on PROGRESS.md's "Next Iteration" section, decide what to do this iteration.
Record the decided objective in PROGRESS.md as "Current Iteration Objective."
**Code modification cannot begin until this record is complete** (enforced by PreToolUse hook).

### 4. Work Execution

Execute the planned work. During execution:

- **Decision points**: When two or more options exist, record the choice and reasoning in DECISIONS.md
- **Value changes**: When modifying any numeric value, record "why this value?" in DECISIONS.md
- **Scope drift detection**: If work feels like it's deviating from WHY.md intent, stop immediately and self-verify
- **Inflation detection**: If values keep going up, stop and review against BASELINE

### 5. Iteration Wrap-up

When work is complete, always:

1. Update PROGRESS.md:
   - What was done this iteration (specific)
   - Results and outcomes
   - What must be done next iteration (clear and actionable)
   - Quantitative metric changes (if applicable)

2. Add decision records to DECISIONS.md if any judgments were made

3. Context management:
   - If context is long, run /compact
   - If code quality is questionable, run /simplify
   - Both can be used autonomously without user instruction

---

## Judgment Framework

At every decision point, the agent must pass through these gates:

```
"Does this change serve WHY.md's purpose?"
  ├─ YES → proceed
  └─ NO  → self-verify. Analyze why you drifted and re-establish direction.

"Is the magnitude of this change appropriate relative to BASELINE?"
  ├─ appropriate → proceed
  └─ excessive   → self-verify. Is this change truly necessary?

"Does this contradict prior DECISIONS?"
  ├─ consistent → proceed
  └─ contradicts → Is there a clear reason to reverse the prior decision?
      ├─ yes → record reversal reason in DECISIONS.md, then proceed
      └─ no  → follow the prior decision

"Are values showing a monotonic increase pattern?"
  ├─ no  → proceed
  └─ yes → inflation warning. Review what should be decreased.
```

---

## Multi-Agent Utilization

In loop work, resources are unlimited. Accuracy is the top priority.

### Writer/Reviewer Separation

For complex changes, use subagents:
- Writer agent: handles code creation/modification
- Reviewer agent: independently reviews the written code
- Self-reviewing introduces bias, so separation is essential

### Subagent for Self-Audit

During Self-Audit routines, always use a separate subagent:
- The current agent's judgment may be biased toward its own work
- An independent perspective provides more reliable BASELINE comparison

### Full Project Re-analysis

Re-analyzing the entire project every iteration is explicitly permitted:
- Resources are unlimited, so efficiency is not a concern
- Being thorough and intent-aligned matters more than being fast
- Web searches for consistency/correctness checks are also permitted

---

## Autonomous Slash Command Usage

The following commands can be used autonomously without user instruction:

| Command | When to Use |
|---------|-------------|
| /compact | Context is growing long and important information is getting diluted |
| /simplify | Code quality has degraded |
| /clear | Irrelevant context needs full cleanup |

These should be used proactively whenever the agent judges them necessary.

---

## Autonomous Direction Correction Protocol

When direction drift is detected, **do NOT alert the user and wait**. Instead:

1. Pause current work
2. Re-read WHY.md to reconfirm original intent
3. Analyze current state against BASELINE.md
4. Record drift cause in AUDIT.md
5. Establish corrected direction and update PROGRESS.md with revised plan
6. Resume work on the corrected course

The agent bears full responsibility for detecting problems and resolving them autonomously.
The user is away — discover issues yourself and fix them yourself.
