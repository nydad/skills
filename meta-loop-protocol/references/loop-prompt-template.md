# Meta Loop Protocol — Loop Prompt Template

Copy the content between BEGIN TEMPLATE and END TEMPLATE into `.meta-loop/loop-prompt.md`.
Leave the placeholder at the end for the user to add project-specific work instructions.

---

BEGIN TEMPLATE

---

Follow this project's Meta Loop Protocol for all work.

## Iteration Start Procedure (mandatory — cannot be skipped)

Follow this exact sequence. Do not reorder or skip any step.

1. Read `.meta-loop/WHY.md` → confirm the purpose and principles of this work
2. Read `.meta-loop/PROGRESS.md` → understand what was done and what's next
3. Read `.meta-loop/DECISIONS.md` → review prior judgments (prevent repetition/reversal)
4. Compare `.meta-loop/BASELINE.md` against current state → compute delta from origin
5. Record this iteration's objective in PROGRESS.md → then begin work

## Work Principles

- When changing any numeric value, record "why this value?" in DECISIONS.md
- If monotonic escalation (inflation) is detected, stop and recalibrate against BASELINE
- At every decision point, record the rationale in DECISIONS.md
- Do not make changes that deviate from WHY.md's intent
- On direction drift: self-verify and re-establish direction autonomously (do NOT wait for user)
- For complex changes, use subagents for Writer/Reviewer separation
- Run /compact autonomously if context is growing long
- Full project re-analysis every iteration is acceptable (resources are unlimited)
- Web searches for consistency/correctness verification are permitted

## Iteration Wrap-up (mandatory)

After completing work:

1. Update PROGRESS.md with this iteration's results
2. Specify what must be done next iteration (clear and actionable)
3. Record any decisions made in DECISIONS.md
4. Run /compact or /simplify if needed

## Specific Work Instructions

<!-- Add project-specific work instructions below -->


---

END TEMPLATE
