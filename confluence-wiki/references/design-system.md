# Confluence Design System — Color Palettes + ac:layout Patterns

**Table of Contents**
- §1 Default Palette (Ocean Blue)
- §2 Theme Color Palettes (7 Themes)
- §3 KPI Card Colors by Theme
- §4 XHTML Table Styling
- §5 ac:layout Practical XHTML Patterns

---

## 1. Default Palette (Ocean Blue)

| Purpose | Hex |
|---------|-----|
| Panel header, primary border | #2c5282 |
| Panel background | #f7fafc |
| Subtle border | #e2e8f0 |
| Success | #22c55e |
| Warning | #dd6b20 |
| Error | #dc2626 |
| Tab navigation | #403294 |
| Link | #2684ff |

Status badges: Green/Yellow/Red/Blue/Grey (always subtle=true)

---

## 2. Theme Color Palettes (7 Themes)

Each theme has 7 layers: Primary → Accent → Background → Surface → Border → Text → Muted

### Ocean Blue (Default)
`#2c5282` · `#3182ce` · `#eff6ff` · `#dbeafe` · `#93c5fd` · `#1e3a5f` · `#64748b`

Panel: `titleBGColor=#2c5282|titleColor=#ffffff|bgColor=#eff6ff|borderColor=#2c5282`

### Forest Green (Operations/Monitoring)
`#276749` · `#38a169` · `#f0fdf4` · `#dcfce7` · `#86efac` · `#14532d` · `#6b7280`

Panel: `titleBGColor=#276749|titleColor=#ffffff|bgColor=#f0fdf4|borderColor=#276749`

### Soft Purple (Study/Research)
`#553c9a` · `#6b46c1` · `#f5f3ff` · `#ede9fe` · `#c4b5fd` · `#3b0764` · `#78716c`

Panel: `titleBGColor=#553c9a|titleColor=#ffffff|bgColor=#f5f3ff|borderColor=#553c9a`

### Warm Amber (Security/Incidents)
`#92400e` · `#d97706` · `#fffbeb` · `#fef3c7` · `#fbbf24` · `#78350f` · `#a16207`

Panel: `titleBGColor=#92400e|titleColor=#ffffff|bgColor=#fffbeb|borderColor=#92400e`

### Slate Gray (Reports/Meeting Notes)
`#334155` · `#64748b` · `#f8fafc` · `#f1f5f9` · `#cbd5e1` · `#0f172a` · `#94a3b8`

Panel: `titleBGColor=#334155|titleColor=#ffffff|bgColor=#f8fafc|borderColor=#334155`

### Soft Rose (Marketing/Design)
`#9f1239` · `#e11d48` · `#fff1f2` · `#ffe4e6` · `#fda4af` · `#881337` · `#9ca3af`

Panel: `titleBGColor=#9f1239|titleColor=#ffffff|bgColor=#fff1f2|borderColor=#9f1239`

### Teal (Data/Analytics)
`#115e59` · `#14b8a6` · `#f0fdfa` · `#ccfbf1` · `#5eead4` · `#134e4a` · `#6b7280`

Panel: `titleBGColor=#115e59|titleColor=#ffffff|bgColor=#f0fdfa|borderColor=#115e59`

---

## 3. KPI Card Colors by Theme

| Theme | bgColor | borderColor |
|-------|---------|-------------|
| Ocean Blue | #eff6ff | #2c5282 |
| Forest Green | #f0fdf4 | #276749 |
| Soft Purple | #f5f3ff | #553c9a |
| Warm Amber | #fffbeb | #92400e |
| Slate Gray | #f8fafc | #334155 |
| Soft Rose | #fff1f2 | #9f1239 |
| Teal | #f0fdfa | #115e59 |

---

## 4. XHTML Table Styling

Header background + alternating rows:
```xml
<tr><th style="background-color: #2c5282; color: #ffffff;">Header</th></tr>
<tr style="background-color: #f7fafc;"><td>Alternating row</td></tr>
```

> **Theme-aware:** The header `background-color` should use the selected theme's **Primary** color, not hardcoded Ocean Blue. For example, Forest Green uses `#276749`, Soft Purple uses `#553c9a`. See §2 for each theme's Primary value.

---

## 5. ac:layout Practical XHTML Patterns

### 5.1 KPI Cards 3-Column (three_equal + panel)
```xml
<ac:layout>
    <ac:layout-section ac:type="three_equal">
        <ac:layout-cell>
            <ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="kpi-1">
                <ac:parameter ac:name="bgColor">#f0fdf4</ac:parameter>
                <ac:parameter ac:name="borderColor">#22c55e</ac:parameter>
                <ac:parameter ac:name="borderWidth">2</ac:parameter>
                <ac:rich-text-body>
                    <h3><span style="color: #22c55e;">Uptime</span></h3>
                    <p style="font-size: 28px; font-weight: bold;">99.97%</p>
                    <p style="color: #6c757d;">Last 30 days</p>
                </ac:rich-text-body>
            </ac:structured-macro>
        </ac:layout-cell>
        <!-- Remaining 2 cells follow same pattern, change colors only -->
    </ac:layout-section>
</ac:layout>
```

### 5.2 AS-IS / TO-BE Comparison (two_equal)
```xml
<ac:layout>
    <ac:layout-section ac:type="two_equal">
        <ac:layout-cell>
            <ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="asis-1">
                <ac:parameter ac:name="title">AS-IS</ac:parameter>
                <ac:parameter ac:name="titleBGColor">#dc2626</ac:parameter>
                <ac:parameter ac:name="titleColor">#ffffff</ac:parameter>
                <ac:parameter ac:name="bgColor">#fef2f2</ac:parameter>
                <ac:parameter ac:name="borderColor">#dc2626</ac:parameter>
                <ac:rich-text-body><p>Current state</p></ac:rich-text-body>
            </ac:structured-macro>
        </ac:layout-cell>
        <ac:layout-cell>
            <ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="tobe-1">
                <ac:parameter ac:name="title">TO-BE</ac:parameter>
                <ac:parameter ac:name="titleBGColor">#22c55e</ac:parameter>
                <ac:parameter ac:name="titleColor">#ffffff</ac:parameter>
                <ac:parameter ac:name="bgColor">#f0fdf4</ac:parameter>
                <ac:parameter ac:name="borderColor">#22c55e</ac:parameter>
                <ac:rich-text-body><p>Target state</p></ac:rich-text-body>
            </ac:structured-macro>
        </ac:layout-cell>
    </ac:layout-section>
</ac:layout>
```

### 5.3 Sidebar + Main (two_left_sidebar)
```xml
<ac:layout>
    <ac:layout-section ac:type="two_left_sidebar">
        <ac:layout-cell>
            <ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="side-1">
                <ac:parameter ac:name="title">Quick Info</ac:parameter>
                <ac:parameter ac:name="titleBGColor">#2c5282</ac:parameter>
                <ac:parameter ac:name="titleColor">#ffffff</ac:parameter>
                <ac:parameter ac:name="bgColor">#f7fafc</ac:parameter>
                <ac:rich-text-body>
                    <p><strong>Status:</strong> Production</p>
                    <p><strong>Owner:</strong> Platform Team</p>
                </ac:rich-text-body>
            </ac:structured-macro>
        </ac:layout-cell>
        <ac:layout-cell>
            <h2>Details</h2>
            <p>70% width main area</p>
        </ac:layout-cell>
    </ac:layout-section>
</ac:layout>
```

### 5.4 Composite Dashboard (single → three_equal → two_equal → single)
```xml
<ac:layout>
    <ac:layout-section ac:type="single">
        <ac:layout-cell><h1>Dashboard</h1><hr /></ac:layout-cell>
    </ac:layout-section>
    <ac:layout-section ac:type="three_equal">
        <ac:layout-cell><!-- KPI 1 --></ac:layout-cell>
        <ac:layout-cell><!-- KPI 2 --></ac:layout-cell>
        <ac:layout-cell><!-- KPI 3 --></ac:layout-cell>
    </ac:layout-section>
    <ac:layout-section ac:type="two_equal">
        <ac:layout-cell><!-- Chart/Graph --></ac:layout-cell>
        <ac:layout-cell><!-- Detail Table --></ac:layout-cell>
    </ac:layout-section>
    <ac:layout-section ac:type="single">
        <ac:layout-cell><hr /><p style="color: #6c757d;">Last updated by Platform Team</p></ac:layout-cell>
    </ac:layout-section>
</ac:layout>
```

### 5.5 Nested section/column inside ac:layout (4+ columns)
```xml
<ac:layout>
    <ac:layout-section ac:type="single">
        <ac:layout-cell>
            <ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="sec-1">
                <ac:rich-text-body>
                    <ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="col-1">
                        <ac:parameter ac:name="width">25%</ac:parameter>
                        <ac:rich-text-body><p>Col 1</p></ac:rich-text-body>
                    </ac:structured-macro>
                    <!-- col-2, col-3, col-4 follow same pattern -->
                </ac:rich-text-body>
            </ac:structured-macro>
        </ac:layout-cell>
    </ac:layout-section>
</ac:layout>
```
