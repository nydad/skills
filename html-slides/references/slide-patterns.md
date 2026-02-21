# Slide Patterns

Complete HTML patterns for all slide types. Copy and adapt these.

---

## 1. Cover Slide

**Theme**: `samsung` or `blue` | **Use**: Opening slide

```html
<div class="slide samsung">
    <h1>Presentation<br>Title</h1>
    <p class="sub">Subtitle or one-line description</p>
    <p class="meta" style="margin-top:4vh; color:rgba(255,255,255,0.35);">
        Author · Department · Date</p>
</div>
```

---

## 2. Section Divider

**Theme**: Any colored theme | **Use**: Separate major sections

```html
<div class="slide violet">
    <p class="meta" style="color:rgba(255,255,255,0.4);">SECTION 01</p>
    <h1>Section<br>Title</h1>
    <p class="sub">Brief section overview with <span class="em">emphasis</span></p>
</div>
```

---

## 3. Content with List

**Theme**: `surface` or `in-*` | **Use**: Key points, agendas

```html
<div class="slide surface">
    <h2>Section Title</h2>
    <ul class="list" style="margin-top:2vh;">
        <li><strong>Point 1</strong> — Description</li>
        <li><strong class="em">Highlighted</strong> — Important point</li>
        <li><strong class="green">Success</strong> — Positive item</li>
        <li><strong class="red">Warning</strong> — Negative item</li>
    </ul>
</div>
```

Or with `h3` for content slides within a section:

```html
<div class="slide in-mint">
    <h3>Content Heading</h3>
    <ul class="list" style="margin-top:2vh;">
        <li>Item one</li>
        <li>Item two with <span class="em">emphasis</span></li>
    </ul>
</div>
```

---

## 4. Comparison Cards

**Theme**: default dark | **Use**: Before/after, pros/cons, options (2-4 items)

```html
<div class="slide">
    <h3>Comparison Title</h3>
    <div class="comp">
        <div class="comp-item red-on">
            <div class="tag">Before</div>
            <p>Previous state<br>or problem</p>
        </div>
        <div class="comp-item green-on">
            <div class="tag">After</div>
            <p>Current state<br>or solution</p>
        </div>
    </div>
    <p class="sub" style="margin-top:2vh;">Supporting insight</p>
</div>
```

**States**: (none)=neutral, `.on`=blue, `.green-on`, `.yellow-on`, `.red-on`

---

## 5. Feature Grid

**Theme**: any | **Use**: Features, categories (3-5 items)

```html
<div class="slide">
    <h3>Features Overview</h3>
    <div class="grid">
        <div class="grid-item">
            <p class="name em">Feature 1</p>
            <p class="desc">Short description</p>
        </div>
        <div class="grid-item">
            <p class="name">Feature 2</p>
            <p class="desc">Short description</p>
        </div>
        <div class="grid-item">
            <p class="name">Feature 3</p>
            <p class="desc">Short description</p>
        </div>
    </div>
</div>
```

On colored section themes, add inline styles for visibility:
```html
<div class="grid-item" style="background: rgba(0,0,0,0.3); border-color: rgba(255,255,255,0.2);">
    <p class="name em">Title</p>
    <p class="desc" style="color: rgba(255,255,255,0.7);">Description</p>
</div>
```

---

## 6. Big Statistic

**Theme**: `in-*` | **Use**: Single impressive metric

```html
<div class="slide in-mint">
    <div class="stat">
        <p class="number">90%+</p>
        <p class="label">Metric description</p>
    </div>
    <p class="sub" style="margin-top:3vh;">Context or source citation</p>
</div>
```

---

## 7. Stat Grid (2x2)

**Theme**: `surface` | **Use**: Multi-metric dashboard (2-4 cards)

```html
<div class="slide surface">
    <h3>Key Metrics</h3>
    <div class="stat-grid">
        <div class="stat-card">
            <div class="label">Metric A</div>
            <div class="value">85%</div>
            <div class="source">Source: Report</div>
        </div>
        <div class="stat-card green-on">
            <div class="label">Metric B</div>
            <div class="value" style="color:#10E890;">+110%</div>
            <div class="source">Source: Study</div>
        </div>
        <div class="stat-card">
            <div class="label">Metric C</div>
            <div class="value">4.4<span style="font-size:1.5rem">hrs</span></div>
            <div class="source">Source: Survey</div>
        </div>
        <div class="stat-card red-on">
            <div class="label">Metric D</div>
            <div class="value" style="color:#FCA5A5;">-30%</div>
            <div class="source">Source: Data</div>
        </div>
    </div>
</div>
```

**States**: `.on`, `.green-on`, `.yellow-on`, `.red-on`
**Full-width card**: Add `style="grid-column: span 2;"` to span both columns.

---

## 8. Pipeline / Process

**Theme**: `surface` | **Use**: Workflows, timelines, evolution

```html
<div class="slide surface">
    <h3>Process Flow</h3>
    <div class="pipeline">
        <div class="pipeline-step">Step 1</div>
        <span class="pipeline-arrow">&rarr;</span>
        <div class="pipeline-step on">Step 2</div>
        <span class="pipeline-arrow">&rarr;</span>
        <div class="pipeline-step">Step 3</div>
        <span class="pipeline-arrow">&rarr;</span>
        <div class="pipeline-step green">Done</div>
    </div>
    <p class="sub" style="margin-top:2vh;">Process description</p>
</div>
```

**States**: (none)=gray, `.on`=blue, `.green`, `.red`, `.violet`

---

## 9. Architecture Layers

**Theme**: `surface` or default | **Use**: Technology stacks, organizational layers

```html
<div class="slide surface">
    <h3>System Architecture</h3>
    <div class="arch-layers">
        <div class="arch-layer">
            <div class="role">Layer 1</div>
            <div class="brand">Primary Info</div>
            <div class="desc">Secondary detail</div>
        </div>
        <div class="arch-layer on">
            <div class="role">Layer 2</div>
            <div class="brand">Highlighted Layer</div>
            <div class="desc" style="color:#5FB3FF; font-weight:700;">Key point</div>
        </div>
        <div class="arch-layer">
            <div class="role">Layer 3</div>
            <div class="brand">Another Layer</div>
            <div class="desc">Detail</div>
        </div>
    </div>
</div>
```

Customize `.role` width with `style="width:140px;"` if labels are longer.

---

## 10. Tool / Product Cards

**Theme**: default dark | **Use**: Tool comparison, product showcase

```html
<div class="slide">
    <h3>Tools Overview</h3>
    <div class="tool-cards">
        <div class="tool-card recommended">
            <p class="name">Tool A</p>
            <p class="desc">Description of tool</p>
            <div><span class="tag-item green">free</span><span class="tag-item blue">popular</span></div>
        </div>
        <div class="tool-card hot">
            <p class="name">Tool B</p>
            <p class="desc">Description of tool</p>
            <div><span class="tag-item yellow">new</span></div>
        </div>
        <div class="tool-card">
            <p class="name">Tool C</p>
            <p class="desc">Description of tool</p>
        </div>
    </div>
</div>
```

**Card states**: `.recommended` (green), `.hot` (amber), (none)=neutral
**Tag colors**: `.tag-item.green`, `.tag-item.blue`, `.tag-item.yellow`

---

## 11. Quote

**Theme**: default dark | **Use**: Citations, key statements

```html
<div class="slide">
    <blockquote>
        "Powerful quote that captures<br>your key message."
    </blockquote>
    <cite>&mdash; Name, Title</cite>
</div>
```

---

## 12. Code Block

**Theme**: `surface` | **Use**: Code snippets, terminal output

```html
<div class="slide surface">
    <h3>Code Example</h3>
    <div class="code"><span class="comment">// Initialize configuration</span>
<span class="keyword">const</span> config = {
    theme: <span class="string">"dark"</span>,
    enabled: <span class="keyword">true</span>
};</div>
</div>
```

**Syntax classes**: `.comment` (gray-blue), `.keyword` (violet), `.string` (green)

---

## 13. Data Table

**Theme**: `surface` | **Use**: Structured data comparison

```html
<div class="slide surface">
    <h3>Comparison Table</h3>
    <table class="tbl">
        <tr><th>Feature</th><th>Basic</th><th>Pro</th></tr>
        <tr><td>Storage</td><td>10GB</td><td class="green">100GB</td></tr>
        <tr><td>Support</td><td class="red">Email</td><td class="green">24/7</td></tr>
    </table>
</div>
```

---

## 14. Warning / Tip Callouts

**Theme**: any | **Use**: Important notices, helpful tips

```html
<div class="note warn">
    <p>Warning: Critical caveat or caution message here.</p>
</div>
<div class="note tip">
    <p>Tip: Helpful suggestion or positive note here.</p>
</div>
```

These are typically placed below other content within a slide, not as standalone slides.

---

## 15. Two Column Layout

**Theme**: default dark | **Use**: Side-by-side content

```html
<div class="slide">
    <h3>Two Perspectives</h3>
    <div class="two-col">
        <div class="col">
            <h3>Left Title</h3>
            <ul class="list">
                <li>Item 1</li>
                <li>Item 2</li>
            </ul>
        </div>
        <div class="col">
            <h3>Right Title</h3>
            <ul class="list">
                <li>Item A</li>
                <li>Item B</li>
            </ul>
        </div>
    </div>
</div>
```

---

## 16. Impact Statement

**Theme**: any | **Use**: Bold typographic statements, key messages

```html
<div class="slide">
    <p class="impact-text">Bold Statement<br>That Demands Attention</p>
    <p class="impact-sub">Supporting context or explanation</p>
</div>
```

---

## 17. Formula / Concept Equation

**Theme**: default dark | **Use**: Key equations, conceptual formulas

```html
<div class="slide">
    <h3>Performance Formula</h3>
    <p class="formula" style="margin:3vh 0;">
        Output = <span class="em">Model</span> &times; <span class="green">Agent</span> &times; <span class="yellow">Pilot</span>
    </p>
    <p class="sub">Explanation of each variable</p>
</div>
```

---

## 18. Image Slide

**Real image**:
```html
<div class="slide">
    <img src="image.png" alt="Description"
        style="max-width: 35vw; max-height: 40vh; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
    <p class="sub">Caption</p>
</div>
```

**Placeholder**:
```html
<div class="slide">
    <div class="img">
        <span class="label">Image Prompt</span>
        <p class="prompt">Minimalist style. Subject. Composition. Colors. Mood.</p>
    </div>
</div>
```

---

## 19. Background Watermark Number

Add a decorative large number behind content:

```html
<div class="slide">
    <p class="big">01</p>
    <h3>Main Content</h3>
    <p class="sub">Description</p>
</div>
```

---

## 20. Closing Slide

**Theme**: `blue` | **Use**: Thank you, Q&A

```html
<div class="slide blue">
    <h1>Thank You</h1>
    <p class="sub">Questions?</p>
    <p class="meta" style="margin-top:5vh; color:rgba(255,255,255,0.35);">
        Q &amp; A</p>
</div>
```

---

## Phosphor Icons Usage

Add icons anywhere using Phosphor's web font classes:

```html
<!-- Regular icon -->
<i class="ph ph-robot"></i>

<!-- Filled icon -->
<i class="ph-fill ph-robot"></i>

<!-- Bold icon -->
<i class="ph-bold ph-arrow-right"></i>
```

Common useful icons:
`ph-robot`, `ph-cpu`, `ph-lightning`, `ph-shield-check`, `ph-rocket-launch`,
`ph-chart-line-up`, `ph-check-circle`, `ph-warning`, `ph-funnel`,
`ph-database`, `ph-code`, `ph-terminal-window`, `ph-chat-teardrop-dots`,
`ph-user-focus`, `ph-device-mobile`, `ph-car-profile`, `ph-book-open-text`

Style inline: `style="font-size: 3rem; color: #5FB3FF;"`
