# Claude Code Skills

A collection of reusable [Claude Code](https://claude.com/claude-code) skills — adaptive agents that generate context-aware output, not cookie-cutter templates.

## Available Skills

### html-slides

Professional HTML presentation generator with rich dark theme design system.

- Adaptive slide count (lightning 5-7, standard 15-25, deep-dive 30-40)
- 13 color themes (section + in-section content themes)
- 25+ components (cards, grids, stats, pipelines, architecture layers, etc.)
- Glass-morphism design with responsive layout
- Keyboard, touch, and fullscreen navigation
- Print and accessibility support
- Single-file HTML output

**Triggers**: `presentation`, `slides`, `ppt`, `deck`, `발표자료`

```
html-slides/
  SKILL.md                        # Main skill definition
  references/
    template.html                 # Canonical CSS + JS template
    slide-patterns.md             # 20 HTML slide patterns
    design-tokens.md              # Color, typography, spacing reference
    creative-guidelines.md        # Custom composition rules
```

### confluence-wiki

Confluence wiki document generator with optional draw.io diagrams.

- Wiki Markup (.wiki) and XHTML (.xhtml) output formats
- 7 color themes (Ocean Blue, Forest Green, Soft Purple, Warm Amber, Slate Gray, Soft Rose, Teal)
- ac:layout page layouts (single, two-column, three-column variants)
- 11 draw.io diagram types (architecture, flowchart, network, CI/CD, ERD, K8s, etc.)
- Diagrams generated only when architecture/structure visualization is needed (max 1-2)
- GCP icon support with full prIcon reference

**Triggers**: `/confluence`, `/wiki`, `/cwiki`, `confluence 문서`, `위키 작성`

```
confluence-wiki/
  SKILL.md                        # Main skill definition
  references/
    design-system.md              # 7 color palettes, ac:layout XHTML patterns
    drawio-diagram-templates.md   # 12 diagram type shape styles
    drawio-gcp-reference.md       # GCP icons, containers, arrows
```

## Installation

Copy any skill directory into `~/.claude/skills/` to make it available globally in Claude Code:

```bash
# Install a single skill
cp -r html-slides ~/.claude/skills/
cp -r confluence-wiki ~/.claude/skills/

# Or install all skills
cp -r */ ~/.claude/skills/
```

## Skill Design Principles

These skills follow key design principles:

- **Adaptive agent, not template factory** — output adapts to context, audience, and purpose
- **Progressive disclosure** — reference files loaded only when needed (see Reference Loading Guide in each SKILL.md)
- **Copy-and-check validation** — quality checklists embedded in output for self-verification
- **Anti-pattern examples** — concrete ❌/✅ mistakes documented to prevent common errors
- **Token efficiency** — SKILL.md stays under 500 lines; details live in reference files with TOCs

## License

MIT
