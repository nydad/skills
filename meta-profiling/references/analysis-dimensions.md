# Analysis Dimensions — Detailed Rubric

7 dimensions for profiling AI collaboration style. Each dimension has 5 levels with specific indicators.

## Table of Contents
1. [Delegation Architecture](#1-delegation-architecture)
2. [Communication Style](#2-communication-style)
3. [Quality Standards](#3-quality-standards)
4. [Autonomy Spectrum](#4-autonomy-spectrum)
5. [Knowledge Management](#5-knowledge-management)
6. [Meta-cognitive Depth](#6-meta-cognitive-depth)
7. [Failure Architecture](#7-failure-architecture)

---

## 1. Delegation Architecture

**Core Question:** How does the user distribute cognitive work to AI?

| Level | Label | Indicators | Evidence Sources |
|-------|-------|-----------|-----------------|
| 1 | Default | Uses AI as single Q&A tool, no role differentiation | No agents, no CLAUDE.md delegation rules |
| 2 | Aware | Occasionally specifies AI role ("act as reviewer") | Simple role prompts in conversation |
| 3 | Deliberate | Assigns distinct roles to different interactions, uses subagents | Custom agents (2-3), some role definitions |
| 4 | Systematic | Multi-agent architecture with defined cognitive roles, model selection per task | 4+ agents, model-per-task strategy, agent-teams config |
| 5 | Generative | Designs delegation systems others can use, creates reusable orchestration patterns | Agent definitions as sharable templates, multi-model architecture docs, teaching materials |

**What to look for:**
- `~/.claude/agents/*.md` — count, role diversity, model assignments
- `settings.json` — `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` flag
- CLAUDE.md — delegation rules, role division sections
- Memory files — feedback about delegation patterns
- Custom skills that invoke subagents

**Scoring notes:**
- Multi-model usage (e.g., Claude for judgment + GPT for exploration) = Level 4+
- Parallel agent execution patterns = Level 4+
- "Council Pattern" or equivalent multi-perspective design = Level 5

---

## 2. Communication Style

**Core Question:** How does the user instruct, correct, and confirm AI work?

| Level | Label | Indicators | Evidence Sources |
|-------|-------|-----------|-----------------|
| 1 | Default | Generic prompts, no feedback loops, accepts outputs as-is | No feedback memories, no CLAUDE.md rules |
| 2 | Aware | Gives corrections, but ad-hoc ("no, not that") | Occasional feedback memories |
| 3 | Deliberate | Explains WHY behind corrections, sets expectations upfront | Feedback memories with "Why" sections, CLAUDE.md with communication rules |
| 4 | Systematic | Communication rules codified, correction patterns are systematic | Rules files with communication standards, feedback memories with "How to apply" |
| 5 | Generative | Communication style is itself a designed system, teaches others how to communicate with AI | Teaching materials, shared prompt patterns, organizational AI communication guides |

**What to look for:**
- Memory files of type `feedback` — look for "Why:" and "How to apply:" structure
- CLAUDE.md — language preferences, response style rules
- Tone of feedback: direct vs indirect, specific vs vague
- Whether corrections address root cause or just symptoms
- Whether user explains reasoning behind preferences

**Scoring notes:**
- "Don't do X" without explanation = Level 2
- "Don't do X because Y, apply when Z" = Level 4
- Korean default + English for code = deliberate language architecture = Level 3+

---

## 3. Quality Standards

**Core Question:** What does "done" mean to this user?

| Level | Label | Indicators | Evidence Sources |
|-------|-------|-----------|-----------------|
| 1 | Default | Accepts first output, no verification | No quality rules, no test commands |
| 2 | Aware | Eyeballs output, occasionally asks for changes | Ad-hoc revision requests |
| 3 | Deliberate | Has explicit quality criteria, runs tests | CLAUDE.md verification checklist, test commands |
| 4 | Systematic | Quality gates in workflow, automated checks, quantitative standards | Hook-based validation, CI integration, coverage metrics |
| 5 | Generative | Quality systems are reusable frameworks, creates tools for quality assurance | Quality frameworks as skills/scripts, shared testing strategies |

**What to look for:**
- CLAUDE.md — verification checklist presence
- Settings — hook configurations for pre/post tool use
- Memory — feedback about quality ("20점", "아마추어적")
- Git patterns — test-before-commit habits
- Quantitative metrics in memory (test counts, coverage %)

**Scoring notes:**
- Explicit numeric quality scores in feedback = Level 4+
- "원본 정합성 최우선" type rules = Level 4+
- Reusable test frameworks = Level 5

---

## 4. Autonomy Spectrum

**Core Question:** How much freedom does the user grant AI?

| Level | Label | Indicators | Evidence Sources |
|-------|-------|-----------|-----------------|
| 1 | Restrictive | Approves every action, tight control | Permission mode: default or plan, no loop usage |
| 2 | Cautious | Allows some tools, reviews frequently | Selective permission allow-lists |
| 3 | Balanced | Grants autonomy for routine, reviews critical decisions | Mixed permission mode, occasional /loop |
| 4 | Delegating | Broad autonomy with guardrails, extended /loop sessions | dontAsk mode, 1h+ loop sessions, hook-based guardrails |
| 5 | Orchestrating | AI runs autonomously for hours/days with self-correction mechanisms | 10h+ loops, meta-loop-protocol or equivalent, cron-based automation |

**What to look for:**
- `settings.json` — `defaultMode` (dontAsk = high autonomy)
- `skipDangerousModePermissionPrompt` — extreme trust signal
- Loop usage patterns in memory
- Cron or scheduled task configurations
- Self-correction mechanisms (hooks, audit triggers)
- Duration of autonomous sessions mentioned in memory

**Scoring notes:**
- `dontAsk` mode = Level 4 minimum
- 10h+ autonomous sessions = Level 5
- Self-audit hooks = Level 5
- cron-based AI execution = Level 5

---

## 5. Knowledge Management

**Core Question:** How does the user preserve context across sessions?

| Level | Label | Indicators | Evidence Sources |
|-------|-------|-----------|-----------------|
| 1 | Default | No persistence, each session starts fresh | No memory files, no CLAUDE.md |
| 2 | Aware | Uses CLAUDE.md for basic project info | Simple CLAUDE.md, no memory files |
| 3 | Deliberate | Maintains memory files, organizes by type | Memory files with frontmatter, MEMORY.md index |
| 4 | Systematic | Multi-project memory, cross-session continuity design, compaction strategy | Memory across 3+ projects, /compact rules, BASELINE snapshots |
| 5 | Generative | Knowledge management is itself a designed system, external memory architecture | Meta-loop external memory (.meta-loop/), Zettelkasten-like linking, memory skills |

**What to look for:**
- `~/.claude/projects/*/memory/` — file count, type distribution, freshness
- MEMORY.md — organization quality, link density
- CLAUDE.md — compaction instructions, context preservation rules
- External memory systems (.meta-loop/, custom knowledge bases)
- Memory type distribution (user vs feedback vs project vs reference)

**Scoring notes:**
- 10+ memory files across 3+ projects = Level 4
- Immutable snapshot + dynamic tracking pattern = Level 5
- Memory files that reference each other = Level 5

---

## 6. Meta-cognitive Depth

**Core Question:** Does the user think about HOW they work with AI, or just WHAT they work on?

| Level | Label | Indicators | Evidence Sources |
|-------|-------|-----------|-----------------|
| 1 | Default | Uses AI for tasks, no reflection on process | No process-related configuration |
| 2 | Aware | Notices when AI works well/poorly, adjusts prompts | Occasional feedback about AI behavior |
| 3 | Deliberate | Designs workflows around AI strengths/weaknesses | CLAUDE.md with workflow rules, agent role design |
| 4 | Systematic | Creates reusable AI collaboration systems | Custom skills, agent definitions, rules files |
| 5 | Generative | Builds meta-systems (tools that build tools), teaches others, designs failure prevention frameworks | Skills that generate skills, meta-loop protocols, AI collaboration education |

**What to look for:**
- Custom skills — especially meta-level ones (meta-loop-protocol, profiling)
- Agent definitions — do they encode cognitive theory?
- Rules files — do they address "how to use AI" not just "what to do"?
- Teaching/education activities
- Tool-making vs tool-using ratio
- Second-order thinking (designing systems that design systems)

**Scoring notes:**
- Building skills = Level 4
- Building skills that control how AI thinks = Level 5
- Teaching AI collaboration to others = Level 5
- Explicit failure mode taxonomy = Level 5

---

## 7. Failure Architecture

**Core Question:** How does the user handle and prevent AI mistakes?

| Level | Label | Indicators | Evidence Sources |
|-------|-------|-----------|-----------------|
| 1 | Default | Deals with errors as they come, no prevention | No error-handling rules |
| 2 | Reactive | Corrects mistakes after they happen, saves feedback | Feedback memories about past errors |
| 3 | Preventive | Sets up rules to prevent known errors | CLAUDE.md rules ("never do X"), safety rules |
| 4 | Systematic | Failure modes classified, automated prevention (hooks, guardrails) | Hook-based prevention, classified failure types, UND_ERR_SOCKET rules |
| 5 | Generative | Failure prevention is itself a framework, predicts novel failure modes | Meta-loop-protocol, FMEA-style analysis, failure mode taxonomy as a skill |

**What to look for:**
- CLAUDE.md — "NEVER" rules, error handling sections
- Feedback memories — patterns of corrections (same error multiple times?)
- Hook configurations — PreToolUse/PostToolUse checks
- Meta-loop or equivalent — self-audit mechanisms
- Failure classification (Context Drift, Monotonic Escalation, etc.)

**Scoring notes:**
- "UND_ERR_SOCKET → STOP, different strategy" = Level 4
- Named failure modes (Context Drift, etc.) = Level 5
- Self-audit hooks = Level 5
- Failure prevention framework as a shareable skill = Level 5

---

## Overall Profile Calculation

The 7 scores produce a profile shape, not a single number. Different shapes represent different collaboration archetypes.

**Common shapes:**
- **Flat high** (all 4-5): Power user / AI methodology designer
- **Delegation spike** (dim 1 high, others moderate): Team orchestrator
- **Quality spike** (dim 3 high): Precision-focused developer
- **Autonomy spike** (dim 4 high): Automation maximizer
- **Meta spike** (dim 6 high): Tool-maker / framework designer

**Important:** The shape matters more than individual scores. A "3,3,3,3,3,3,3" user is fundamentally different from a "5,1,5,1,5,1,5" user even though both average 3.
