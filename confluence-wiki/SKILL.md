---
name: confluence-wiki
disable-model-invocation: true
description: |
  Generates professional Confluence wiki documents with optional draw.io diagrams.
  Use this skill whenever the user wants to create documentation for Confluence — technical docs, architecture pages,
  onboarding guides, incident reports, meeting notes, or any wiki page. Supports Wiki Markup and XHTML, ac:layout,
  7 color themes, and 11 diagram types. Also use when the user mentions: confluence, wiki, cwiki, 컨플루언스, 위키,
  기술문서 작성, 온보딩 문서, 장애 보고서, draw.io 다이어그램, or wants to format content for Confluence paste.
---

# Confluence Wiki Document Generator v3

**Table of Contents**
- Quick Start: 3-Step Path
- PHASE 1: Analysis & Decision
- PHASE 2: Document Generation
- PHASE 3: Draw.io Diagram Generation (Conditional)
- PHASE 4: Usage Guide
- Design Constraints
- Accessibility Guidelines
- Quality Checklist
- Common Mistakes
- Reference Loading Guide

You are an adaptive Confluence document agent. Before generating output, **analyze the user's intent, audience, and document purpose** to determine the optimal format, depth, structure, and components. Do not follow a rigid template — choose what fits the context. Draw.io diagrams are included **only when visual representation genuinely aids comprehension**, limited to **1-2 per document**.

> **Simplicity principle: Default to Wiki Markup.** Most Confluence pages don't need multi-column layouts. XHTML with ac:layout adds complexity — use it only when side-by-side comparison or KPI dashboards are genuinely needed. A well-structured Wiki Markup page with headings, tables, status badges, and expand macros covers 80% of use cases. When in doubt, choose Wiki Markup.

## Quick Start: 3-Step Path

1. **Document Type?** → Technical / Architecture / Incident / Notes / Onboarding?
2. **Need Diagram?** → Complex system topology? → YES (1-2 max). Simple process? → NO (use table/list).
3. **Format?** → Text + tables only = Wiki Markup (.wiki). Layouts/dashboards/KPI = XHTML (.xhtml).

**Reference Roadmap** (load only what you need):
- XHTML with ac:layout → Read `references/design-system.md`
- Including draw.io diagrams → Read `references/drawio-diagram-templates.md` + `references/drawio-gcp-reference.md`
- Simple wiki page → No references needed, use defaults below

---

## PHASE 1: Analysis & Decision

### 1.1 Document Type → Output Format

| Type | Output Format |
|------|---------------|
| Technical docs, study notes, reports, meeting notes | Wiki Markup (.wiki) |
| Architecture docs, onboarding guides, incident reports | Wiki Markup (.wiki) |
| KPI dashboards, side-by-side comparison pages | XHTML (.xhtml) |

**Use XHTML only when:**
- You need side-by-side columns (AS-IS/TO-BE, KPI cards 3-column)
- The user explicitly requests ac:layout or multi-column layout

**Otherwise, use Wiki Markup.** Headings + tables + status badges + expand macros handle most document types well without the complexity of ac:layout.

### 1.2 Draw.io Diagram Necessity Check

> **Default principle: Diagrams are optional.** Do not generate if text + tables can convey the information sufficiently.

**Generate when any of the following apply:**
- System architecture / infrastructure topology requires visual explanation
- Network topology, data flows, etc. are too complex for text alone
- User explicitly requests a diagram

**Do NOT generate for**:
- Meeting notes, study notes, general reports, guide documents
- Simple processes (tables or numbered lists suffice)
- Code explanations, API docs, configuration guides

**Limit: Max 1-2 per document.** Only visualize the most critical structure.

| Diagram Type | Keywords | Content Size (권장) |
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

> Content Size = pageWidth × pageHeight = dx × dy. 모든 셀 좌표를 이 범위 안에 배치할 것.

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

1. Bold `*text*` needs whitespace or boundary (space, `|`, line start/end) on BOTH sides. No boundary → asterisks render literally. **Always use `{*}text{*}` form** — it works everywhere without spacing issues. `*` at line start is parsed as bullet, so `{*}` is mandatory there too.
2. Status badges: Always use `subtle=true`, place on same line as table `|`
3. `{code}` macro must start on a new line
4. **No nested panels** — Panel inside panel breaks rendering
5. Escape special chars `[ ] { }` with `\`
6. `{toc}` must be on its own line
7. Links: `[text|URL]` (reverse order from Markdown)
8. Cannot mix Wiki Markup and XHTML in one document
9. ac:macro-id must be unique per macro (format: `{feature}-{seq}`)
10. Draw.io macro `diagramName` must exactly match .drawio filename (without extension)
11. `{expand}` macro: title is required — omitting it renders as blank toggle
12. Nested `{expand}` inside `{expand}` is supported but avoid 3+ levels (readability)

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

**Composite layout — keep it simple:**
- Max 2-3 layout sections per page. Stacking 4+ sections makes pages harder to maintain than Wiki Markup.
- If your layout plan has 4+ sections, reconsider — Wiki Markup with tables and expand macros is likely simpler.
```
KPI dashboard:   single (title) → three_equal (KPI) → single (table)
Comparison page: single (title) → two_equal (A vs B)
```

→ ac:layout XHTML patterns: `references/design-system.md` §5

### 2.4 Expand/Collapse for Readability

Documents get long fast. Use expand/collapse to keep the page scannable — readers see the key points immediately and drill into details on demand.

**When to collapse (접기):**
- Raw data, full logs, verbose output, JSON/XML payloads
- Configuration details, environment variable lists
- Step-by-step procedures that most readers already know
- Supplementary references, appendices, change history
- Code blocks longer than ~20 lines

**When to keep expanded (펼치기):**
- Executive summary, key decisions, action items
- Architecture diagrams, critical metrics (KPI)
- Current status, blockers, deadlines
- Anything the reader needs without clicking

**Wiki Markup:**
```
{expand:title=상세 로그 보기}
Raw log content here...
{expand}
```

**XHTML:**
```xml
<ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="expand-1">
    <ac:parameter ac:name="title">상세 설정 보기</ac:parameter>
    <ac:rich-text-body>
        <p>Collapsed content here...</p>
    </ac:rich-text-body>
</ac:structured-macro>
```

**Expand title rules:**
- Always include counts or scope in the title — readers decide whether to expand based on the title alone
- Good: `{expand:Backend 미테스트 사유 (ServiceImpl 18개, Controller 54개)}`
- Good: `{expand:Vue Frontend — 90 files, 2,133 tests}`
- Bad: `{expand:상세 보기}` — too vague, no information scent

**Content hierarchy pattern (summary → detail):**
1. Panel (`{panel}`) → key message, motivation, conclusion — always visible
2. Summary table → aggregated numbers with status badges — always visible
3. Expand (`{expand}`) → per-category breakdowns, raw data, reasons — collapsed
4. This lets readers scan the summary in seconds and drill into specifics on demand

**Practical patterns:**
- **Incident report**: Timeline summary visible → full log in expand
- **Architecture doc**: Decision visible → alternatives considered in expand
- **Onboarding guide**: Quick steps visible → detailed explanation in expand
- **Meeting notes**: Decisions/actions visible → discussion details in expand
- **Coverage report**: Summary table visible → per-category details in expand, exclusion reasons in expand

### 2.5 Draw.io Macro Insertion (XHTML Only)
```xml
<ac:structured-macro ac:name="drawio" ac:schema-version="0" ac:macro-id="drawio-1">
    <ac:parameter ac:name="diagramName">filename-without-extension</ac:parameter>
    <ac:parameter ac:name="simpleViewer">false</ac:parameter>
    <ac:parameter ac:name="diagramWidth">1200</ac:parameter>
    <ac:parameter ac:name="lbox">true</ac:parameter>
    <ac:parameter ac:name="revision">1</ac:parameter>
</ac:structured-macro>
```

### 2.6 Quick-Start Templates

**Incident Report** (Wiki Markup):
```
Sections: h1 Title → panel(Impact summary) → h2 Timeline → h2 Root Cause → h2 Action Items
Theme: Warm Amber | Diagram: Optional
Expand: Full logs, raw metrics, config dumps → collapse
Visible: Impact, timeline, action items → always show
```

**Architecture Review** (Wiki Markup):
```
Sections: h1 Title → panel(Decision) → h2 Overview (+ diagram) → h2 Trade-offs → h2 Next Steps
Theme: Ocean Blue | Diagram: Required
Expand: Alternative options, detailed specs, capacity calculations → collapse
Visible: Decision, diagram, key trade-offs → always show
```

**KPI Dashboard** (XHTML — ac:layout justified):
```
ac:layout: single (title) → three_equal (KPI cards) → single (detail table)
Theme: Match domain | Keep layout minimal — avoid 4+ section stacking
```

**Onboarding Guide** (Wiki Markup):
```
Sections: h1 Welcome → h2 Prerequisites → h2 Setup Steps → h2 Key Contacts → h2 FAQ
Theme: Forest Green | Expand: Troubleshooting, detailed config → collapse
```

**Meeting Notes** (Wiki Markup):
```
Sections: h1 [Date] Meeting → h2 Attendees → h2 Agenda → h2 Decisions → h2 Action Items
Theme: Slate Gray | Expand: Discussion details, background context → collapse
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
7. **mxGraphModel: `dx=pageWidth`, `dy=pageHeight`, `page="1"`.** draw.io는 dx/dy를 뷰포트 트랜슬레이트로 사용하며, dx=pageWidth/dy=pageHeight일 때 콘텐츠가 페이지 영역에 정상 배치된다. 콘텐츠 좌표는 반드시 (0,0)~(pageWidth, pageHeight) 범위 안에 배치할 것.

**mxGraphModel 기본 템플릿 (필수):**
```xml
<mxfile host="Confluence">
  <diagram id="d1" name="Diagram">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="800" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- content cells: 좌표를 (0,0)~(1200,800) 안에 배치 -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```
> dx≠pageWidth이거나 page="0"이면 Confluence에서 빈 공간이 생기거나 콘텐츠가 구석에 몰린다.

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

### Wiki Markup 삽입 방법

> **주의**: Editor `+` → "Insert markup" → "Confluence Wiki" 방식은 {*}매크로 블록 안에 마크업이 갇혀{*} 원문이 그대로 노출됩니다. 이 방식은 인라인 삽입용이며, 전체 페이지에는 적합하지 않습니다.

**방법 1 (권장): REST API로 직접 업로드**
```bash
curl -u username:password -X PUT \
  -H "Content-Type: application/json" \
  "https://confluence.example.com/rest/api/content/{pageId}" \
  -d '{
    "version": {"number": N+1},
    "title": "페이지 제목",
    "type": "page",
    "body": {
      "wiki": {
        "value": "<wiki markup content here>",
        "representation": "wiki"
      }
    }
  }'
```
`representation: "wiki"`로 지정하면 Confluence가 자동으로 Storage Format(XHTML)으로 변환합니다.

**방법 2: 소스 편집기에서 XHTML Storage Format으로 변환하여 붙여넣기**
1. 외부 도구(예: Confluence REST API preview)로 Wiki Markup → XHTML 변환
2. Confluence Editor `</>` (소스 편집기) → 변환된 XHTML 붙여넣기 → 저장

**방법 3: "Insert markup" 부분 삽입 (소규모 블록만)**
- Editor `+` → "Insert markup" → "Confluence Wiki" → Paste
- 이 방식은 짧은 블록(테이블 1개 등)에만 사용. 전체 페이지에 사용하면 마크업이 매크로 안에 갇힘.

- **XHTML**: Editor `</>` (source editor) → Paste → Save
- **Draw.io** (only if generated): Insert draw.io macro on page → 편집 아이콘 클릭 → 상단 메뉴 **Extras** → **Edit Diagram** → Paste XML (Ctrl+Shift+X는 draw.io에 없는 단축키. 공식은 Ctrl+Shift+E이나 Confluence iframe에서 안 먹을 수 있으므로 메뉴 사용 권장)

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
| Expand/Collapse | Use for raw data, logs, verbose details — keep key info visible |
| Visible content | Top-level should be scannable in <2 min without expanding |
| Code blocks | >20 lines → wrap in expand macro |
| Tables | >15 rows of raw data → wrap in expand macro |

---

## Accessibility Guidelines

- [ ] Color is never the ONLY differentiator — use icons/labels alongside colors
- [ ] Tables have `<th>` headers for screen readers
- [ ] Draw.io diagrams include a text summary below (for accessibility)
- [ ] Status badges use text labels, not just colors (e.g., "완료" not just green dot)
- [ ] Links have descriptive text (not "click here")

---

## Quality Checklist

> **Copy this checklist into your response and mark each item before delivering output:**

```
[  ] h1 used exactly once; all macro tags properly opened and closed
[  ] ac:macro-id unique across document (format: {feature}-{seq})
[  ] ac:layout-cell count matches layout type (single=1, two_*=2, three_*=3)
[  ] Wiki Markup and XHTML not mixed in the same document
[  ] (If Draw.io) diagramName matches .drawio filename, XML well-formed, all mxCell IDs unique
[  ] Colors consistent within selected theme palette
[  ] Status badges use subtle=true; panels ≤ 2 and never nested
[  ] Document has author name and creation date
[  ] All external links are valid and accessible
[  ] Accessibility guidelines above are satisfied
[  ] Raw data, logs, verbose details wrapped in expand/collapse macro
[  ] Page scannable in <2 min without expanding any section
```

---

## Common Mistakes

| | Pattern | Fix |
|---|---------|-----|
| ❌ | Nested panels (panel inside panel) | ✅ Flat panel structure — one level only |
| ❌ | Wiki Markup + XHTML mixed in one doc | ✅ Choose one format per document |
| ❌ | `ac:macro-id="drawio-1"` reused across macros | ✅ Unique IDs: `drawio-arch-1`, `drawio-flow-2` |
| ❌ | `*Bold at line start*` (parsed as bullet) | ✅ `{*}Bold text{*}` |
| ❌ | `word*bold*word` (no space around `*`) | ✅ `word {*}bold{*} word` (always use `{*}` form) |
| ❌ | `dx≠pageWidth` or `page="0"` (diagram in corner or wrong canvas) | ✅ `dx=pageWidth, dy=pageHeight, page="1"` (e.g. dx="1200" pageWidth="1200") |
| ❌ | `{code}` on same line as other content | ✅ `{code}` must start on its own line |
| ❌ | `{expand:상세 보기}` (vague title) | ✅ `{expand:Backend — 282 files, 2,889 tests}` (counts in title) |
| ❌ | 30+ row table fully visible | ✅ Summary table visible + detail rows in expand |
| ❌ | All content at same level (flat) | ✅ Panel(key) → Table(summary) → Expand(detail) hierarchy |

---

## Reference Loading Guide

**Always read first:**
- This SKILL.md — core workflow and decision logic

**Load when generating XHTML with ac:layout:**
- `references/design-system.md` — Color palettes, ac:layout XHTML patterns

**Load only when Draw.io diagram is needed (per §1.2):**
- `references/drawio-diagram-templates.md` — Diagram type shape styles
- `references/drawio-gcp-reference.md` — GCP icons, container/arrow styles

---

## Reference Files

- `references/drawio-gcp-reference.md` — GCP prIcon list, style strings, SVG icons, container/arrow patterns
- `references/drawio-diagram-templates.md` — Diagram type shape styles (flowchart, network, CI/CD, etc.)
- `references/design-system.md` — 7 color theme palettes (hex values), ac:layout XHTML patterns
