# Claude Code Skills

A collection of reusable [Claude Code](https://claude.com/claude-code) skills.

## Available Skills

### html-slides

Professional HTML presentation generator with rich dark theme design system.

- 13 color themes (section + in-section content themes)
- 25+ components (cards, grids, stats, pipelines, architecture layers, etc.)
- Glass-morphism design with responsive layout
- Keyboard, touch, and fullscreen navigation
- Print and accessibility support
- Single-file HTML output

**Usage**: Install as a Claude Code skill, then ask Claude to create a presentation.

```
html-slides/
  SKILL.md                        # Main skill definition
  references/
    template.html                 # Canonical CSS + JS template
    slide-patterns.md             # 20 HTML slide patterns
    design-tokens.md              # Color, typography, spacing reference
    creative-guidelines.md        # Custom composition rules
```

## Installation

Copy any skill directory into `~/.claude/skills/` to make it available in Claude Code.
