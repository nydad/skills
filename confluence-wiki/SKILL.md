---
name: confluence-wiki
description: |
  Generates professional Confluence wiki documents. Optionally includes draw.io diagrams when architecture or structural visualization is needed.
  Supports ac:layout, section/column, 7 color themes, and 10+ diagram types.
  Triggers: /confluence, /wiki, /cwiki, confluence 문서, 위키 작성, 컨플루언스, 위키 문서 만들어줘, draw.io 다이어그램
---

# Confluence Wiki Document Generator v3

Generate **senior-engineer-quality** Confluence wiki documents from user content.
Draw.io diagrams are created **only when visual representation of architecture, system topology, or infrastructure is essential**, limited to **1-2 per document**.

---

## PHASE 1: Analysis & Decision

### 1.1 Document Type → Output Format

| Type | Output Format |
|------|---------------|
| Technical docs, study notes, reports, meeting notes | Wiki Markup (.wiki) |
| Architecture, dashboards, onboarding, presentations | XHTML (.xhtml) |
| Incident reports | XHTML (with ac:layout) |

**Format selection criteria:**
- Wiki Markup: Text + tables + status badges, code blocks
- XHTML: ac:layout needed, tab navigation, KPI dashboards

### 1.2 Draw.io Diagram Necessity Check

> **Default principle: Diagrams are optional.** Do not generate if text + tables can convey the information sufficiently.

**Generate only when** (all conditions below):
- System architecture / infrastructure topology requires visual explanation
- Network topology, data flows, etc. are too complex for text alone
- User explicitly requests a diagram

**Do NOT generate for**:
- Meeting notes, study notes, general reports, guide documents
- Simple processes (tables or numbered lists suffice)
- Code explanations, API docs, configuration guides

**Limit: Max 1-2 per document.** Only visualize the most critical structure.

| Diagram Type | Keywords | pageSize |
|-------------|----------|----------|
| Architecture Overview | System topology, infrastructure, cloud | 1200x800 |
| Flowchart | Process, decision branch, approval | 1000x600 |
| Network Topology | Firewall, VPN, DMZ, subnet | 1400x900 |
| CI/CD Pipeline | Build, deploy, Jenkins, GitHub Actions | 1600x350 |
| Data Pipeline | ETL, streaming, BigQuery, Kafka | 1400x500 |
| Microservices | API Gateway, service mesh, gRPC | 1400x900 |
| Swimlane | Cross-team collaboration, role-based process | 1200x800 |
| C4 Model | Context, Container, Component | 1200x800 |
| ERD | Entity, table, relationship | 1200x900 |
| Kubernetes | Pod, Deployment, Ingress, Helm | 1400x800 |
| Sequence | Request/response flow, API call order | 1000x800 |

→ Diagram style patterns: `references/drawio-diagram-templates.md`

### 1.3 Color Theme Selection

Default: Ocean Blue (when unspecified). → Full hex values: `references/design-system.md`

| Theme | Primary | Background | Recommended Use |
|-------|---------|------------|-----------------|
| Ocean Blue | #2c5282 | #eff6ff | Technical docs, architecture |
| Forest Green | #276749 | #f0fdf4 | Operations, monitoring |
| Soft Purple | #553c9a | #f5f3ff | Study, research |
| Warm Amber | #92400e | #fffbeb | Security, incidents |
| Slate Gray | #334155 | #f8fafc | Reports, meeting notes |
| Soft Rose | #9f1239 | #fff1f2 | Marketing, design |
| Teal | #115e59 | #f0fdfa | Data, analytics |

---

## PHASE 2: Document Generation

### 2.1 Output Files
```
{document-title-kebab-case}.wiki or .xhtml
{diagram-name-kebab-case}.drawio (when needed)
```

### 2.2 Confluence-Specific Gotchas (MUST READ)

The model already knows Wiki Markup/XHTML syntax. Only **Confluence server-specific pitfalls** are documented here:

1. `*` at line start = parsed as bullet → Use `{*}text{*}` for bold at line start
2. Status badges: Always use `subtle=true`, place on same line as table `|`
3. `{code}` macro must start on a new line
4. **No nested panels** — Panel inside panel breaks rendering
5. Escape special chars `[ ] { }` with `\`
6. `{toc}` must be on its own line
7. Links: `[text|URL]` (reverse order from Markdown)
8. Cannot mix Wiki Markup and XHTML in one document
9. ac:macro-id must be unique per macro (format: `{feature}-{seq}`)
10. Draw.io macro `diagramName` must exactly match .drawio filename (without extension)

### 2.3 ac:layout Page Layout (XHTML Only)

Built into Confluence. No third-party apps required.

```xml
<ac:layout>
    <ac:layout-section ac:type="TYPE">
        <ac:layout-cell>Content</ac:layout-cell>
    </ac:layout-section>
</ac:layout>
```

| Type | Ratio | Cells | Typical Use |
|------|-------|-------|-------------|
| `single` | 100% | 1 | Title, TOC, full-width table, footer |
| `two_equal` | 50/50 | 2 | AS-IS/TO-BE, Before/After |
| `two_left_sidebar` | 30/70 | 2 | Quick Info + main detail |
| `two_right_sidebar` | 70/30 | 2 | Main + side reference |
| `three_equal` | 33/33/33 | 3 | KPI cards (3-column) |
| `three_with_sidebars` | 20/60/20 | 3 | Dual sidebars + center |

**ac:layout vs section/column**: ac:layout uses fixed ratios (max 3 columns), section/column uses flexible ratios (unlimited columns). Use ac:layout for overall page structure, section/column for multi-column within a section. Nesting is allowed.

**Composite layout patterns:**
```
Dashboard:       single → three_equal → two_equal → single
Technical doc:   single → two_left_sidebar → single → two_equal → single
Incident report: single → three_equal → single → two_equal → single
```

→ ac:layout XHTML patterns: `references/design-system.md` §5

### 2.4 Draw.io Macro Insertion (XHTML)
```xml
<ac:structured-macro ac:name="drawio" ac:schema-version="0" ac:macro-id="drawio-1">
    <ac:parameter ac:name="diagramName">filename-without-extension</ac:parameter>
    <ac:parameter ac:name="simpleViewer">false</ac:parameter>
    <ac:parameter ac:name="diagramWidth">1200</ac:parameter>
    <ac:parameter ac:name="lbox">true</ac:parameter>
    <ac:parameter ac:name="revision">1</ac:parameter>
</ac:structured-macro>
```

---

## PHASE 3: Draw.io Diagram Generation (Conditional)

> **Execute this PHASE only if §1.2 determined a diagram is needed.**
> Skip to PHASE 4 if no diagram is required.

### 3.1 Design Principles
1. Single-page diagram (no multi-page)
2. Numbered arrows to show flow (① ② ③)
3. Consistent color coding per zone
4. Summary footer bar (key points with colored dots)
5. Font hierarchy: Title 20px > Name 11px > Description 9px > Sub 7px
6. Minimum 30px spacing between elements, grid=10 alignment

### 3.2 GCP Icons + Styles

→ Full prIcon list, container styles, arrow styles, SVG icons: `references/drawio-gcp-reference.md`

Key style summary:

**GCP hexIcon:**
```
shape=mxgraph.gcp2.hexIcon;prIcon=SERVICE;fillColor=#5184F3;strokeColor=none;
```

**Key colors:**
- GCP icons: #5184F3, Connectors: #4284F3
- External zone: fill=#f8f9fa, stroke=#dee2e6
- Internal zone: fill=#f0fdf4, stroke=#22c55e
- Security zone: stroke=#f97316
- Region: fill=#fff2cc, stroke=#d6b656
- Success: #22c55e, Failure: #ef4444

→ Diagram type shape/style patterns: `references/drawio-diagram-templates.md`

---

## PHASE 4: Usage Guide

Always provide these instructions after output:

- **Wiki Markup**: Editor `+` → "Insert markup" → Select "Confluence Wiki" → Paste
- **XHTML**: Editor `</>` (source editor) → Paste → Save
- **Draw.io** (only if generated): Insert draw.io macro on page → "Extras" → "Edit Diagram" (Ctrl+Shift+X) → Paste XML

---

## Design Constraints

| Rule | Limit |
|------|-------|
| h1 | Once per document |
| h2 | 3-7 per document |
| Panels | Max 2 (panels inside ac:layout cells counted separately) |
| Table columns | Max 6 |
| Status badges | Always subtle=true |
| Panel nesting | Forbidden |
| Color scheme | Single theme, consistent throughout |
| Wiki+XHTML mixing | Forbidden |
| Section dividers | `----` horizontal rule |
| Draw.io diagrams | Only when needed, max 1-2 per document |

---

## Quality Checklist

- [ ] h1 once, macro tags properly opened/closed
- [ ] ac:macro-id unique, special characters escaped
- [ ] ac:layout-cell count matches layout type
- [ ] (If Draw.io included) diagramName matches .drawio filename, XML well-formed, mxCell IDs unique
- [ ] Colors consistent within selected theme palette
- [ ] Status badges subtle=true, panels ≤ 2

---

## Reference Files

- `references/drawio-gcp-reference.md` — GCP prIcon list, style strings, SVG icons, container/arrow patterns
- `references/drawio-diagram-templates.md` — Diagram type shape styles (flowchart, network, CI/CD, etc.)
- `references/design-system.md` — 7 color theme palettes (hex values), ac:layout XHTML patterns
