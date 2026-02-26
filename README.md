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

### excalidraw-arch

Excalidraw architecture diagram generator from codebase analysis.

- 6 diagram types (layered, microservices, data flow, network, cloud, component)
- 5 layout strategies (top-down, left-right, hub-spoke, nested, grid)
- Semantic color-coding by architecture layer
- Editable .excalidraw JSON output

**Triggers**: `excalidraw`, `architecture diagram`, `시스템 구조도`

```
excalidraw-arch/
  SKILL.md                        # Main skill definition
  references/
    excalidraw-styles.md          # Shape styles, colors, arrows
    component-library.md          # Reusable component patterns
```

### mermaid-diagram

Mermaid diagram generator supporting 20+ diagram types.

- Adaptive diagram type selection based on content
- Flowchart, sequence, class, ER, Gantt, mindmap, C4, and more
- 5 built-in themes + custom theme configuration
- Markdown code block or standalone .mmd output

**Triggers**: `mermaid`, `diagram`, `flowchart`, `다이어그램`

```
mermaid-diagram/
  SKILL.md                        # Main skill definition
  references/
    diagram-types.md              # 20 diagram type syntax patterns
    theme-config.md               # Theme configuration and styling
```

### design-system

Design system generator with industry-specific reasoning.

- 30+ UI styles (glassmorphism, brutalism, neumorphism, etc.)
- 15 industry-tailored color palettes with full hex values
- 23 Google Fonts typography pairings
- Design tokens output (CSS Custom Properties, Tailwind, JSON)
- Design system capture from existing UIs

**Triggers**: `design system`, `design tokens`, `디자인 시스템`

```
design-system/
  SKILL.md                        # Main skill definition
  references/
    ui-styles.md                  # 22 UI style catalog
    color-palettes.md             # 15 industry color palettes
    typography-guide.md           # Font pairings, scales, loading
```

### playwright-e2e

Playwright E2E test suite generator with adaptive test strategy.

- Framework-aware test generation (React, Next.js, Vue, etc.)
- Page object pattern, fixtures, and configuration
- Visual regression and accessibility testing
- Selector best practices and wait strategies

**Triggers**: `playwright`, `e2e test`, `E2E 테스트`

```
playwright-e2e/
  SKILL.md                        # Main skill definition
  references/
    test-patterns.md              # Common E2E test patterns
    selectors-guide.md            # Selector strategies and waits
```

## Installation

Copy any skill directory into `~/.claude/skills/` to make it available globally in Claude Code:

```bash
# Install a single skill
cp -r html-slides ~/.claude/skills/
cp -r confluence-wiki ~/.claude/skills/
cp -r excalidraw-arch ~/.claude/skills/
cp -r mermaid-diagram ~/.claude/skills/
cp -r design-system ~/.claude/skills/
cp -r playwright-e2e ~/.claude/skills/

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
