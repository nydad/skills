# Mermaid Theme & Styling Configuration

## Table of Contents

1. [Built-in Themes](#built-in-themes)
2. [Init Directive](#init-directive)
3. [Custom Theme Variables](#custom-theme-variables)
4. [classDef Styling](#classdef-styling)
5. [Individual Element Styling](#individual-element-styling)
6. [Edge Styling](#edge-styling)
7. [Font Configuration](#font-configuration)
8. [Responsive Considerations](#responsive-considerations)
9. [Theme Recipes](#theme-recipes)

---

## Built-in Themes

| Theme | Description | Colors | Best For |
|-------|-------------|--------|----------|
| `default` | Standard blue tones on white | Blue nodes, light bg | General purpose, documentation |
| `forest` | Green-dominated palette | Green nodes, cream bg | Organic topics, growth |
| `dark` | Dark background, light elements | Gray bg, light text | Dark mode, presentations |
| `neutral` | Grayscale, no color | Gray tones only | Print, formal docs |
| `base` | Minimal starting point | Bare colors | Custom theme foundation |

Apply a theme:
```
%%{init: {'theme': 'dark'}}%%
flowchart TD
    A --> B
```

---

## Init Directive

The `%%{init}%%` directive MUST be the very first line of the diagram. It configures theme, layout, and diagram-specific settings.

### Basic Theme Selection
```
%%{init: {'theme': 'forest'}}%%
```

### Theme with Custom Variables
```
%%{init: {
    'theme': 'base',
    'themeVariables': {
        'primaryColor': '#4f46e5',
        'primaryTextColor': '#ffffff',
        'primaryBorderColor': '#3730a3',
        'lineColor': '#6366f1',
        'secondaryColor': '#e0e7ff',
        'tertiaryColor': '#f5f3ff'
    }
}}%%
```

### Diagram-Specific Configuration
```
%%{init: {
    'theme': 'default',
    'flowchart': { 'curve': 'basis', 'padding': 20 },
    'sequence': { 'mirrorActors': false }
}}%%
```

**Important:** No blank line between the init directive and the diagram type declaration.

---

## Custom Theme Variables

When using `'theme': 'base'`, you have full control over colors via `themeVariables`:

### Core Variables

| Variable | Affects | Default |
|----------|---------|---------|
| `primaryColor` | Main node fill | `#4f46e5` |
| `primaryTextColor` | Text on primary nodes | `#ffffff` |
| `primaryBorderColor` | Primary node borders | `#3730a3` |
| `secondaryColor` | Secondary node fill | `#e0e7ff` |
| `secondaryTextColor` | Text on secondary nodes | `#1e1b4b` |
| `secondaryBorderColor` | Secondary borders | `#a5b4fc` |
| `tertiaryColor` | Tertiary elements fill | `#f5f3ff` |
| `tertiaryTextColor` | Text on tertiary | `#1e1b4b` |
| `lineColor` | Edge/arrow color | `#6366f1` |
| `textColor` | General text | `#1e1b4b` |

### Background Variables

| Variable | Affects | Default |
|----------|---------|---------|
| `background` | Diagram background | `#ffffff` |
| `mainBkg` | Main element background | `#4f46e5` |
| `nodeBorder` | Node border color | `#3730a3` |

### Flowchart-Specific Variables

| Variable | Affects |
|----------|---------|
| `nodeTextColor` | Text inside flowchart nodes |
| `clusterBkg` | Subgraph background |
| `clusterBorder` | Subgraph border |
| `defaultLinkColor` | Arrow color |

### Sequence Diagram Variables

| Variable | Affects |
|----------|---------|
| `actorBkg` | Participant box background |
| `actorBorder` | Participant box border |
| `actorTextColor` | Participant text |
| `activationBorderColor` | Activation bar border |
| `activationBkgColor` | Activation bar fill |
| `signalColor` | Arrow color |
| `signalTextColor` | Arrow label color |
| `noteBkgColor` | Note background |
| `noteTextColor` | Note text |
| `noteBorderColor` | Note border |

---

## classDef Styling

Define reusable style classes for nodes:

```
classDef className fill:#color,stroke:#color,stroke-width:2px,color:#textColor
```

### Apply to Nodes

**Inline (at node definition):**
```
flowchart TD
    A[Server]:::primary --> B[Database]:::storage
    classDef primary fill:#4f46e5,stroke:#3730a3,color:#fff
    classDef storage fill:#0891b2,stroke:#0e7490,color:#fff
```

**Bulk assignment:**
```
classDef active fill:#22c55e,stroke:#16a34a,color:#fff
class nodeA,nodeB,nodeC active
```

### Common classDef Patterns

```
%% Status colors
classDef success fill:#22c55e,stroke:#16a34a,color:#fff
classDef warning fill:#f59e0b,stroke:#d97706,color:#000
classDef error fill:#ef4444,stroke:#dc2626,color:#fff
classDef info fill:#3b82f6,stroke:#2563eb,color:#fff

%% Infrastructure
classDef server fill:#6366f1,stroke:#4f46e5,color:#fff
classDef database fill:#0891b2,stroke:#0e7490,color:#fff
classDef cloud fill:#8b5cf6,stroke:#7c3aed,color:#fff
classDef external fill:#9ca3af,stroke:#6b7280,color:#fff,stroke-dasharray: 5 5

%% Emphasis
classDef highlight fill:#fbbf24,stroke:#f59e0b,color:#000,stroke-width:3px
classDef dimmed fill:#f3f4f6,stroke:#d1d5db,color:#9ca3af
```

---

## Individual Element Styling

Style specific nodes by ID (overrides classDef):

```
flowchart TD
    A[Critical Service] --> B[Database]
    style A fill:#ef4444,stroke:#dc2626,color:#fff,stroke-width:3px
    style B fill:#0891b2,stroke:#0e7490,color:#fff
```

**Available style properties:**
- `fill` -- background color
- `stroke` -- border color
- `stroke-width` -- border thickness
- `color` -- text color
- `stroke-dasharray` -- dashed border (e.g., `5 5`)
- `opacity` -- transparency (0 to 1)

---

## Edge Styling

### Link Styles (by index)

Edges are numbered starting from 0 in order of appearance:

```
flowchart TD
    A --> B
    B --> C
    linkStyle 0 stroke:#ef4444,stroke-width:3px
    linkStyle 1 stroke:#22c55e,stroke-width:2px,stroke-dasharray:5
```

### Default Link Style

```
linkStyle default stroke:#6366f1,stroke-width:2px
```

---

## Font Configuration

Set via init directive:

```
%%{init: {
    'theme': 'base',
    'themeVariables': {
        'fontFamily': 'Inter, system-ui, sans-serif',
        'fontSize': '14px'
    }
}}%%
```

**Common font stacks:**
- Technical: `'JetBrains Mono, monospace'`
- Business: `'Inter, system-ui, sans-serif'`
- Presentation: `'Poppins, sans-serif'`

Note: Font availability depends on the rendering environment. Stick to system fonts or common web fonts.

---

## Responsive Considerations

Mermaid diagrams auto-scale to their container width. For optimal rendering:

1. **Keep node labels short** -- long text causes overflow on small screens
2. **Limit diagram width** -- prefer TD (top-down) for narrow containers, LR for wide
3. **Use abbreviations** in node labels with full text in tooltips (if supported)
4. **HTML output**: Set max-width on the container `<pre>` element:
   ```html
   <pre class="mermaid" style="max-width: 800px; margin: 0 auto;">
   ```

---

## Theme Recipes

### Corporate Blue
```
%%{init: {
    'theme': 'base',
    'themeVariables': {
        'primaryColor': '#1e40af',
        'primaryTextColor': '#ffffff',
        'primaryBorderColor': '#1e3a8a',
        'lineColor': '#3b82f6',
        'secondaryColor': '#dbeafe',
        'tertiaryColor': '#eff6ff',
        'background': '#ffffff'
    }
}}%%
```

### Dark Mode
```
%%{init: {
    'theme': 'base',
    'themeVariables': {
        'primaryColor': '#6366f1',
        'primaryTextColor': '#f9fafb',
        'primaryBorderColor': '#818cf8',
        'lineColor': '#a5b4fc',
        'secondaryColor': '#312e81',
        'tertiaryColor': '#1e1b4b',
        'background': '#0f172a',
        'textColor': '#e2e8f0',
        'mainBkg': '#1e293b',
        'nodeBorder': '#475569'
    }
}}%%
```

### Nature / Organic
```
%%{init: {
    'theme': 'base',
    'themeVariables': {
        'primaryColor': '#15803d',
        'primaryTextColor': '#ffffff',
        'primaryBorderColor': '#166534',
        'lineColor': '#22c55e',
        'secondaryColor': '#dcfce7',
        'tertiaryColor': '#f0fdf4',
        'background': '#ffffff'
    }
}}%%
```

### Warning / Alert
```
%%{init: {
    'theme': 'base',
    'themeVariables': {
        'primaryColor': '#dc2626',
        'primaryTextColor': '#ffffff',
        'primaryBorderColor': '#991b1b',
        'lineColor': '#ef4444',
        'secondaryColor': '#fee2e2',
        'tertiaryColor': '#fef2f2',
        'background': '#ffffff'
    }
}}%%
```

### Minimal / Print-Friendly
```
%%{init: {
    'theme': 'base',
    'themeVariables': {
        'primaryColor': '#f9fafb',
        'primaryTextColor': '#111827',
        'primaryBorderColor': '#374151',
        'lineColor': '#6b7280',
        'secondaryColor': '#f3f4f6',
        'tertiaryColor': '#f9fafb',
        'background': '#ffffff'
    }
}}%%
```
