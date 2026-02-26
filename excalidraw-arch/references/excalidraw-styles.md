# Excalidraw Styles Reference

## Table of Contents

1. [Element JSON Structure](#1-element-json-structure)
2. [Common Element Properties](#2-common-element-properties)
3. [Shape Style Presets by Layer](#3-shape-style-presets-by-layer)
4. [Text Element Styles](#4-text-element-styles)
5. [Arrow Style Configurations](#5-arrow-style-configurations)
6. [Line Styles](#6-line-styles)
7. [Color Palette Detail](#7-color-palette-detail)
8. [Container / Frame Patterns](#8-container--frame-patterns)
9. [appState Configuration](#9-appstate-configuration)

---

## 1. Element JSON Structure

Every Excalidraw element shares this base structure:

```json
{
  "id": "unique-id-string",
  "type": "rectangle",
  "x": 100,
  "y": 200,
  "width": 200,
  "height": 80,
  "angle": 0,
  "strokeColor": "#339af0",
  "backgroundColor": "#a5d8ff",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "groupIds": [],
  "frameId": null,
  "index": "a0",
  "roundness": { "type": 3 },
  "seed": 1234567890,
  "version": 1,
  "versionNonce": 1234567890,
  "isDeleted": false,
  "boundElements": null,
  "updated": 1700000000000,
  "link": null,
  "locked": false
}
```

**Required fields for all elements:** `id`, `type`, `x`, `y`, `width`, `height`, `strokeColor`, `backgroundColor`, `fillStyle`, `strokeWidth`, `roughness`, `opacity`, `seed`, `version`, `versionNonce`, `isDeleted`.

**`seed` and `versionNonce`**: Use any random integer. These control the hand-drawn randomness.

**`index`**: Determines z-order. Use fractional indexing: `"a0"`, `"a1"`, `"a2"`, etc.

---

## 2. Common Element Properties

### fillStyle Options
| Value | Effect |
|-------|--------|
| `"solid"` | Flat fill (recommended for architecture diagrams) |
| `"hachure"` | Hand-drawn diagonal lines |
| `"cross-hatch"` | Cross-hatched pattern |

### strokeStyle Options
| Value | Effect |
|-------|--------|
| `"solid"` | Continuous line (default) |
| `"dashed"` | Dashed line (async/event connections) |
| `"dotted"` | Dotted line (optional/weak dependency) |

### roughness Options
| Value | Effect |
|-------|--------|
| `0` | Clean, no hand-drawn effect |
| `1` | Subtle hand-drawn wobble (recommended) |
| `2` | Heavy hand-drawn effect |

### roundness
| Value | Effect |
|-------|--------|
| `null` | Sharp corners |
| `{ "type": 3 }` | Rounded corners (recommended for rectangles) |

---

## 3. Shape Style Presets by Layer

### UI / Frontend Layer
```json
{
  "strokeColor": "#339af0",
  "backgroundColor": "#a5d8ff",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "roundness": { "type": 3 }
}
```

### API / Gateway Layer
```json
{
  "strokeColor": "#40c057",
  "backgroundColor": "#b2f2bb",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "roundness": { "type": 3 }
}
```

### Service / Business Logic Layer
```json
{
  "strokeColor": "#fa5252",
  "backgroundColor": "#ffc9c9",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "roundness": { "type": 3 }
}
```

### Data / Storage Layer
```json
{
  "strokeColor": "#fd7e14",
  "backgroundColor": "#ffd8a8",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "roundness": { "type": 3 }
}
```

### Infrastructure Layer
```json
{
  "strokeColor": "#7950f2",
  "backgroundColor": "#d0bfff",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "roundness": { "type": 3 }
}
```

### External / Third-Party Layer
```json
{
  "strokeColor": "#868e96",
  "backgroundColor": "#e9ecef",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "roundness": { "type": 3 }
}
```

### Message / Event Bus Layer
```json
{
  "strokeColor": "#fab005",
  "backgroundColor": "#fff3bf",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "roundness": { "type": 3 }
}
```

---

## 4. Text Element Styles

### Title Text (Diagram Title)
```json
{
  "type": "text",
  "fontSize": 28,
  "fontFamily": 1,
  "textAlign": "center",
  "verticalAlign": "top",
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "roughness": 0,
  "opacity": 100
}
```

### Component Label (Inside Shapes)
```json
{
  "type": "text",
  "fontSize": 18,
  "fontFamily": 1,
  "textAlign": "center",
  "verticalAlign": "middle",
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "containerId": "parent-element-id"
}
```

When a text element has `containerId`, it is bound inside a shape. The parent shape must include the text element's ID in its `boundElements` array:
```json
"boundElements": [{ "id": "text-id", "type": "text" }]
```

### Arrow Label Text
```json
{
  "type": "text",
  "fontSize": 14,
  "fontFamily": 1,
  "textAlign": "center",
  "verticalAlign": "middle",
  "strokeColor": "#495057",
  "backgroundColor": "#ffffff",
  "containerId": "arrow-element-id"
}
```

### Annotation / Description Text
```json
{
  "type": "text",
  "fontSize": 14,
  "fontFamily": 1,
  "textAlign": "left",
  "verticalAlign": "top",
  "strokeColor": "#868e96",
  "backgroundColor": "transparent"
}
```

### fontFamily Values
| Value | Font |
|-------|------|
| `1` | Hand-drawn (Virgil) -- default, matches Excalidraw aesthetic |
| `2` | Normal (Helvetica) |
| `3` | Code (Cascadia) |

---

## 5. Arrow Style Configurations

### Standard Arrow (Synchronous Call)
```json
{
  "type": "arrow",
  "strokeColor": "#495057",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "roundness": { "type": 2 },
  "startBinding": {
    "elementId": "source-element-id",
    "focus": 0,
    "gap": 5,
    "fixedPoint": null
  },
  "endBinding": {
    "elementId": "target-element-id",
    "focus": 0,
    "gap": 5,
    "fixedPoint": null
  },
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "points": [[0, 0], [200, 100]],
  "elbowed": true
}
```

### Async / Event Arrow (Dashed)
```json
{
  "type": "arrow",
  "strokeColor": "#fab005",
  "strokeStyle": "dashed",
  "strokeWidth": 2,
  "roughness": 1,
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "elbowed": true
}
```

### Bidirectional Arrow
```json
{
  "type": "arrow",
  "strokeColor": "#495057",
  "strokeWidth": 2,
  "startArrowhead": "arrow",
  "endArrowhead": "arrow",
  "elbowed": true
}
```

### Arrow Binding Rules

When an arrow connects two elements:
1. Set `startBinding.elementId` and `endBinding.elementId`
2. The source element must list the arrow in `boundElements`: `[{ "id": "arrow-id", "type": "arrow" }]`
3. The target element must also list the arrow in `boundElements`
4. `points` array: first point is `[0, 0]`, last point is relative offset to end
5. `focus`: `-1` to `1` -- controls which side of the element the arrow attaches to (`0` = center)
6. `gap`: pixel distance between arrow endpoint and element border

### Arrow Label Binding

To label an arrow, create a text element with `containerId` set to the arrow's ID. The arrow must include the text in its `boundElements`:
```json
// Arrow element
"boundElements": [{ "id": "label-text-id", "type": "text" }]

// Text element
"containerId": "arrow-id"
```

---

## 6. Line Styles

### Separator Line (Between Layers)
```json
{
  "type": "line",
  "strokeColor": "#ced4da",
  "strokeWidth": 1,
  "strokeStyle": "dashed",
  "roughness": 1,
  "opacity": 50,
  "points": [[0, 0], [1200, 0]]
}
```

---

## 7. Color Palette Detail

### Architecture Layer Colors

| Layer | Fill (bg) | Stroke | RGB Fill | RGB Stroke |
|-------|----------|--------|----------|------------|
| UI / Frontend | #a5d8ff | #339af0 | 165,216,255 | 51,154,240 |
| API / Gateway | #b2f2bb | #40c057 | 178,242,187 | 64,192,87 |
| Service / Logic | #ffc9c9 | #fa5252 | 255,201,201 | 250,82,82 |
| Data / Storage | #ffd8a8 | #fd7e14 | 255,216,168 | 253,126,20 |
| Infrastructure | #d0bfff | #7950f2 | 208,191,255 | 121,80,242 |
| External | #e9ecef | #868e96 | 233,236,239 | 134,142,150 |
| Message / Event | #fff3bf | #fab005 | 255,243,191 | 250,176,5 |

### Neutral Colors

| Purpose | Color | Use |
|---------|-------|-----|
| Default text | #1e1e1e | Titles, labels |
| Secondary text | #495057 | Descriptions, annotations |
| Muted text | #868e96 | Footnotes, metadata |
| Arrow default | #495057 | Standard connections |
| Background | #ffffff | Canvas background |
| Container border | #dee2e6 | Generic container frames |
| Container fill | #f8f9fa | Light container background |

---

## 8. Container / Frame Patterns

### Layer Container (Groups Related Components)
```json
{
  "type": "rectangle",
  "strokeColor": "#dee2e6",
  "backgroundColor": "#f8f9fa",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "dashed",
  "roughness": 0,
  "roundness": { "type": 3 },
  "opacity": 60
}
```

Place a text label at the top-left corner inside the container as the group title.

### Zone Container (e.g., VPC, Subnet, Cloud Region)
```json
{
  "type": "rectangle",
  "strokeColor": "#7950f2",
  "backgroundColor": "#f3f0ff",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "dashed",
  "roughness": 0,
  "roundness": { "type": 3 },
  "opacity": 40
}
```

### Container Sizing Rules

- **Padding**: 30px on all sides from contained elements
- **Title space**: Add 40px at top for the container label
- Container `x` = min(child.x) - 30
- Container `y` = min(child.y) - 70 (30 padding + 40 title)
- Container `width` = max(child.x + child.width) - min(child.x) + 60
- Container `height` = max(child.y + child.height) - min(child.y) + 100

---

## 9. appState Configuration

```json
{
  "appState": {
    "gridSize": 20,
    "gridStep": 5,
    "gridModeEnabled": false,
    "viewBackgroundColor": "#ffffff",
    "currentItemFontFamily": 1,
    "theme": "light"
  }
}
```

Always include `gridSize: 20` and `viewBackgroundColor: "#ffffff"` for consistent rendering.
