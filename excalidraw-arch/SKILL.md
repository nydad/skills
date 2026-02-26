---
name: excalidraw-arch
description: |
  Generates Excalidraw architecture diagrams from codebase analysis or topic descriptions.
  Use when visualizing system topology, service maps, infrastructure layouts, or component dependencies as editable diagrams.
  Semantic color-coding, grouped containers, elbow-style arrows with labels. Outputs .excalidraw JSON files.

  Triggers: excalidraw, architecture diagram, system diagram, 아키텍처 다이어그램, 시스템 구조도
---

# Excalidraw Architecture Diagram Generator

Generate editable Excalidraw architecture diagrams (.excalidraw JSON) from codebase analysis or topic descriptions. Produces semantically colored, well-laid-out diagrams with grouped containers and labeled arrows.

## When to Use

- Visualizing system architecture, service topology, or infrastructure layout
- Creating component dependency diagrams from codebase analysis
- Mapping microservice communication patterns
- Documenting data flow / pipeline architecture
- Diagramming cloud infrastructure (AWS, GCP, Azure)
- Network topology visualization
- Any request mentioning: excalidraw, architecture diagram, system diagram, 아키텍처 다이어그램, 시스템 구조도

## Generation Workflow (2 Phases)

> **You are an adaptive architecture visualization agent.** Every diagram should be uniquely shaped by the system's actual structure, scale, and complexity. Layout strategy, grouping depth, color assignment, and detail level must all adapt to context -- never produce cookie-cutter output.

### Phase 1: Architecture Analysis

**For codebase-based diagrams:**
1. **Scan** the project structure -- identify entry points, modules, services, data stores
2. **Classify** each component by layer: UI, API/Gateway, Service, Data, Infrastructure, External
3. **Map connections** -- API calls, message queues, database access, file I/O, event streams
4. **Determine diagram type** based on what was found (see Diagram Types below)
5. **Choose layout strategy** based on component count and relationship density

**For topic-based diagrams (no codebase):**
1. **Decompose** the described system into logical components
2. **Assign layers** and identify communication patterns
3. **Choose diagram type** and layout strategy

### Phase 1 Output Format

Before generating JSON, output this planning summary:

| Layer | Components | Color |
|-------|-----------|-------|
| Frontend | React App, Admin Portal | #a5d8ff (UI Blue) |
| API | Gateway, Auth Service | #b2f2bb (API Green) |
| Services | Order Svc, Payment Svc | #ffc9c9 (Service Red) |
| Data | PostgreSQL, Redis | #ffd8a8 (Data Orange) |
| Infrastructure | K8s Cluster, Load Balancer | #d0bfff (Infra Purple) |
| External | Stripe API, SendGrid | #e9ecef (External Gray) |

*(Adapt rows to actual components discovered.)*

### Phase 2: Excalidraw JSON Assembly

1. Read `references/excalidraw-styles.md` for element structure and style presets
2. Read `references/component-library.md` for reusable component patterns
3. **Build the element array** -- create each component as styled rectangles/shapes
4. **Create frames** (groups) for logical containers (layers, zones, clusters)
5. **Add arrows** with labels for all connections
6. **Add text labels** for titles, descriptions, annotations
7. **Position elements** according to chosen layout strategy
8. **Assemble final JSON** with all elements, appState, and files objects
9. Save as `{diagram-name}.excalidraw`

## Diagram Types

| Type | When to Use | Layout |
|------|------------|--------|
| **Layered Architecture** | Frontend/backend/infra stack | Top-down rows |
| **Microservices Topology** | Service mesh, API gateway patterns | Grid or hub-spoke |
| **Data Flow / Pipeline** | ETL, streaming, event processing | Left-to-right chain |
| **Network Topology** | Subnets, firewalls, VPN, DMZ | Zone-based nested |
| **Cloud Infrastructure** | AWS/GCP/Azure resource layout | Provider-grouped containers |
| **Component Dependency** | Module imports, package deps | Force-directed or hierarchical |

## Layout Strategies

| Strategy | Description | Best For |
|----------|------------|----------|
| **Top-Down** | Layers stacked vertically, user at top | Layered architecture, N-tier |
| **Left-to-Right** | Flow from source to sink | Pipelines, data flow, CI/CD |
| **Hub-Spoke** | Central node with radiating connections | API gateway, event bus patterns |
| **Nested Containers** | Frames within frames for zones | Cloud infra, network topology |
| **Grid** | Regular grid of same-tier components | Microservices, module deps |

**Spacing rules:**
- Minimum 40px between elements within a group
- Minimum 80px between groups/containers
- Minimum 120px between major layers
- Arrow labels offset 10-20px from midpoint

## Color Palette Quick Reference

| Layer | Fill Color | Stroke Color | Use For |
|-------|-----------|-------------|---------|
| UI / Frontend | #a5d8ff | #339af0 | Web apps, mobile, SPA |
| API / Gateway | #b2f2bb | #40c057 | REST API, GraphQL, gateways |
| Service / Logic | #ffc9c9 | #fa5252 | Business logic, workers |
| Data / Storage | #ffd8a8 | #fd7e14 | Databases, caches, storage |
| Infrastructure | #d0bfff | #7950f2 | K8s, load balancers, CDN |
| External | #e9ecef | #868e96 | Third-party APIs, SaaS |
| Message / Event | #fff3bf | #fab005 | Queues, event bus, streams |

All elements use `strokeWidth: 2`, `roughness: 1` (hand-drawn feel).

> Full style definitions and hex values: `references/excalidraw-styles.md`

## Element Types Quick Reference

| Element | Excalidraw Type | Typical Use |
|---------|----------------|-------------|
| Service box | `rectangle` | Services, apps, modules |
| Database | `ellipse` | Databases, data stores |
| Decision / Router | `diamond` | Load balancers, routers, switches |
| Label | `text` | Titles, annotations, descriptions |
| Connection | `arrow` | Data flow, API calls, dependencies |
| Divider | `line` | Separating layers or zones |
| Container | `rectangle` (frame-like) | Grouping related components |

## Arrow Styles

| Style | roundness | Use For |
|-------|-----------|---------|
| Elbow (default) | `{ type: 3 }` (round) | Most connections -- clean routing |
| Straight | `null` | Short direct connections |

**Arrow labeling:** Add a `text` element near the arrow midpoint to describe the connection (e.g., "REST API", "gRPC", "Event", "SQL").

**Arrow conventions:**
- Solid line + arrowhead: synchronous call / direct dependency
- Dashed line + arrowhead: asynchronous / event-driven
- Numbered labels (1, 2, 3...) for sequential flow diagrams

## Excalidraw JSON Structure

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "claude-excalidraw-arch",
  "elements": [ /* all shapes, text, arrows */ ],
  "appState": {
    "gridSize": 20,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

Each element requires: `id`, `type`, `x`, `y`, `width`, `height`, `strokeColor`, `backgroundColor`, `fillStyle`, `strokeWidth`, `roughness`, plus type-specific fields.

> Full element schema: `references/excalidraw-styles.md`

## Validation Checklist

**After generating, copy this checklist and verify each item:**

```
[ ] Valid JSON -- parseable without errors
[ ] "type": "excalidraw" and "version": 2 present at root
[ ] Every element has a unique "id" (use descriptive IDs like "svc-auth", "db-postgres")
[ ] All elements have required fields: type, x, y, width, height
[ ] Arrows have valid "startBinding" and "endBinding" referencing existing element IDs
[ ] No overlapping elements -- check x/y/width/height for collisions
[ ] Color coding consistent with layer assignments from Phase 1
[ ] Container rectangles fully enclose their child elements (with padding)
[ ] Text labels readable -- fontSize >= 16 for titles, >= 14 for labels
[ ] Arrow labels present for all non-obvious connections
[ ] Diagram fits reasonable canvas (typically 1200-2400px wide, 800-1600px tall)
[ ] appState.gridSize set to 20, viewBackgroundColor set
```

## Common Mistakes

| | Pattern | Fix |
|---|---------|-----|
| ❌ | Arrow `startBinding`/`endBinding` references non-existent element ID | ✅ Verify all binding IDs exist in the elements array before output |
| ❌ | Elements overlap -- two boxes at same x/y coordinates | ✅ Calculate positions with spacing rules (40px min between elements) |
| ❌ | All components same color -- no visual layer distinction | ✅ Assign colors by layer using the color palette |
| ❌ | Container rectangle smaller than its contents | ✅ Container x/y must be less than children; width/height must exceed children + padding |
| ❌ | Missing `"type": "excalidraw"` or `"version": 2` at root | ✅ Always include the standard Excalidraw root structure |
| ❌ | Text labels with `fontSize: 10` -- too small to read | ✅ Minimum fontSize: 16 for titles, 14 for component labels, 12 for annotations |
| ❌ | Arrows without labels -- unclear what the connection means | ✅ Add text label near midpoint: "REST", "gRPC", "SQL", "Event" |
| ❌ | Giant monolithic diagram with 50+ elements on flat canvas | ✅ Use containers/frames to group by layer; break into zones |

## Reference Loading Guide

**Always read first:**
- This SKILL.md -- core workflow, diagram types, layout strategies

**Load for element styling:**
- `references/excalidraw-styles.md` -- Element JSON structure, style presets, color palette details

**Load for component patterns:**
- `references/component-library.md` -- Reusable component JSON snippets, layout templates

## References

- `references/excalidraw-styles.md` -- Element structure, style presets, colors, arrow configs
- `references/component-library.md` -- Reusable architecture component patterns, layout templates
