# Slide Patterns

Complete HTML patterns for all slide types. Copy and adapt these.

## Table of Contents

| # | Pattern | Use |
|---|---------|-----|
| 1 | [Cover Slide](#1-cover-slide) | Opening slide |
| 2 | [Section Divider](#2-section-divider) | Separate major sections |
| 3 | [Content with Heading](#3-content-with-heading) | General content |
| 4 | [Pillars (Text Columns)](#4-pillars-text-columns) | 3-4 column layout |
| 5 | [Comparison (Before/After)](#5-comparison-beforeafter) | Side-by-side compare |
| 6 | [Stat Row](#6-stat-row) | Horizontal metrics |
| 7 | [Big Number](#7-big-number) | Single impressive metric |
| 8 | [Accent Cards](#8-accent-cards) | Highlighted metric boxes |
| 9 | [Flow (Process)](#9-flow-process) | Sequential text steps |
| 10 | [Keyword Pills](#10-keyword-pills) | Tag/keyword display |
| 11 | [Content with List](#11-content-with-list) | Bullet points |
| 12 | [Quote](#12-quote) | Citations, key statements |
| 13 | [Code Block](#13-code-block) | Code snippets |
| 14 | [Data Table](#14-data-table) | Structured data |
| 15 | [Video / Media Placeholder](#15-video--media-placeholder) | Media embed |
| 16 | [Closing Slide](#16-closing-slide) | Thank you, Q&A |

---

## 1. Cover Slide

**Theme**: default (black) or `samsung` | **Use**: Opening slide

```html
<div class="slide">
    <h1 class="hero">Presentation Title</h1>
    <div class="line"></div>
    <p class="hero-sub">Subtitle or tagline</p>
    <p class="eyebrow" style="margin-top:3vh; margin-bottom:0;">Author · Department · Date</p>
</div>
```

With accent word:
```html
<div class="slide">
    <h1 class="hero">일하는 방법을 바꾸다</h1>
    <div class="line"></div>
    <p class="hero-sub"><span class="accent" style="font-size:clamp(2.2rem,4vw,4rem); font-weight:900; font-family:'Figtree',sans-serif; letter-spacing:-0.03em;">Claude Code</span></p>
    <p class="eyebrow" style="margin-top:3vh; margin-bottom:0;">S/W개발팀 SE · 2026. 4</p>
</div>
```

With colored background:
```html
<div class="slide samsung">
    <h1 class="hero">Presentation Title</h1>
    <div class="line" style="background:rgba(255,255,255,0.3);"></div>
    <p class="hero-sub">Subtitle</p>
    <p class="eyebrow" style="margin-top:3vh; margin-bottom:0;">Author · Date</p>
</div>
```

---

## 2. Section Divider

**Theme**: default or any colored | **Use**: Separate major sections

```html
<div class="slide">
    <p class="eyebrow">Section 01</p>
    <h1 class="hero">Section Title</h1>
</div>
```

With colored background:
```html
<div class="slide mint">
    <p class="eyebrow">Section 02</p>
    <h1 class="hero">Growth</h1>
    <p class="hero-sub">Brief <span class="accent">overview</span></p>
</div>
```

---

## 3. Content with Heading

**Theme**: default | **Use**: General content slides

```html
<div class="slide">
    <p class="eyebrow">Topic</p>
    <h2 class="hero">Content <span class="accent">Heading</span></h2>
    <div class="line"></div>
    <p class="hero-sub">Supporting description text</p>
</div>
```

Smaller heading with h3:
```html
<div class="slide">
    <p class="eyebrow">Topic</p>
    <h3>Content Heading</h3>
    <p class="hero-sub" style="font-size:clamp(1rem,1.4vw,1.3rem);">Supporting description</p>
</div>
```

---

## 4. Pillars (Text Columns)

**Theme**: default | **Use**: 3-4 column text with thin separators

```html
<div class="slide">
    <p class="eyebrow">Overview</p>
    <h2 class="hero" style="font-size:clamp(1.8rem,3vw,2.8rem);">Three Pillars</h2>
    <div class="pillars">
        <div class="pillar">
            <p class="pillar-title">Pillar One</p>
            <p class="pillar-desc">Description of the<br>first pillar</p>
        </div>
        <div class="pillar">
            <p class="pillar-title">Pillar Two</p>
            <p class="pillar-desc">Description of the<br>second pillar</p>
        </div>
        <div class="pillar">
            <p class="pillar-title">Pillar Three</p>
            <p class="pillar-desc">Description of the<br>third pillar</p>
        </div>
    </div>
</div>
```

With SVG icons:
```html
<div class="pillar">
    <div class="pillar-icon">
        <svg width="72" height="72" viewBox="0 0 36 36" fill="none"
             stroke="rgba(255,255,255,0.95)" stroke-width="1.5"
             stroke-linecap="round" stroke-linejoin="round">
            <!-- SVG paths here -->
        </svg>
    </div>
    <p class="pillar-title">Title</p>
    <p class="pillar-desc">Description</p>
</div>
```

---

## 5. Comparison (Before/After)

**Theme**: default | **Use**: Side-by-side comparison with central divider

```html
<div class="slide">
    <p class="eyebrow">Comparison</p>
    <h2 class="hero" style="font-size:clamp(1.8rem,3vw,2.8rem);">Before and <span class="accent">After</span></h2>
    <div class="compare" style="margin-top:4vh;">
        <div class="compare-side">
            <p class="compare-year">Before</p>
            <p class="compare-num muted">10명 · 1년</p>
            <p class="compare-detail">Previous state description</p>
        </div>
        <div style="width:1px; height:14vh; background:rgba(255,255,255,0.12); flex-shrink:0; align-self:center;"></div>
        <div class="compare-side">
            <p class="compare-year" style="color:rgba(96,165,250,0.6);">After</p>
            <p class="compare-num bright" style="color:#60a5fa;">2명 · 4주</p>
            <p class="compare-detail">Improved state description</p>
        </div>
    </div>
</div>
```

---

## 6. Stat Row

**Theme**: default | **Use**: Horizontal metric cells with thin separators

```html
<div class="slide">
    <p class="eyebrow">Metrics</p>
    <h2 class="hero" style="font-size:clamp(1.8rem,3vw,2.8rem);">Key Numbers</h2>
    <div class="stat-row">
        <div class="stat-cell">
            <p class="stat-num">1/5</p>
            <p class="stat-desc">인원</p>
        </div>
        <div class="stat-cell">
            <p class="stat-num" style="color:#60a5fa;">1/12</p>
            <p class="stat-desc">기간</p>
        </div>
        <div class="stat-cell">
            <p class="stat-num">↑</p>
            <p class="stat-desc">더 복잡한 작업</p>
        </div>
    </div>
</div>
```

---

## 7. Big Number

**Theme**: default | **Use**: Single impressive metric

```html
<div class="slide">
    <p class="eyebrow">Education</p>
    <div class="bignum">100<span style="font-size:0.4em; color:#60a5fa; margin-left:0.08em;">명+</span></div>
    <p class="bignum-label">2025.12 — 2026.03 교육 완료</p>
    <div class="line"></div>
    <p class="hero-sub">전 임원 · PL <strong>핸즈온 완료</strong></p>
</div>
```

---

## 8. Accent Cards

**Theme**: default | **Use**: Highlighted metric boxes with accent border

Side-by-side cards:
```html
<div class="slide">
    <p class="eyebrow">Quality</p>
    <h2 class="hero" style="font-size:clamp(1.8rem,3vw,2.8rem);">Verification</h2>
    <div style="display:flex; gap:3vw; margin-top:4vh; width:100%; max-width:800px;">
        <div class="accent-card" style="flex:1;">
            <p class="card-num">5,000<span style="font-size:0.5em; color:rgba(255,255,255,0.4);">+</span></p>
            <p class="card-label">자동 검증<br>시나리오</p>
        </div>
        <div class="accent-card" style="flex:1;">
            <p class="card-num">90<span style="font-size:0.5em; color:rgba(255,255,255,0.4);">%+</span></p>
            <p class="card-label">테스트<br>커버리지</p>
        </div>
    </div>
</div>
```

---

## 9. Flow (Process)

**Theme**: default | **Use**: Sequential text-based process steps

```html
<div class="slide">
    <p class="eyebrow">Process</p>
    <h2 class="hero" style="font-size:clamp(1.8rem,3vw,2.8rem);">Workflow</h2>
    <div class="flow">
        <span class="flow-step">AI 작성</span>
        <span class="flow-arrow">→</span>
        <span class="flow-step">자동 검증</span>
        <span class="flow-arrow">→</span>
        <span class="flow-step active">사람이 최종 리뷰</span>
    </div>
</div>
```

**States**: (none)=muted, `.active`=white bold

---

## 10. Keyword Pills

**Theme**: default | **Use**: Tags, keywords, technologies

```html
<div class="slide">
    <p class="eyebrow">Technologies</p>
    <h2 class="hero" style="font-size:clamp(1.8rem,3vw,2.8rem);">Core Stack</h2>
    <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:0; margin-top:3vh;">
        <span class="pill">Claude Code</span>
        <span class="pill">GitHub Copilot</span>
        <span class="pill">Cursor</span>
    </div>
</div>
```

---

## 11. Content with List

**Theme**: default or `in-*` | **Use**: Bullet points, agendas

```html
<div class="slide">
    <p class="eyebrow">Agenda</p>
    <h3>Key Points</h3>
    <ul class="list" style="margin-top:2vh; max-width:640px;">
        <li><strong>Point 1</strong> — Description of the first point</li>
        <li><strong class="accent">Highlighted</strong> — Important point</li>
        <li><strong class="green">Success</strong> — Positive item</li>
        <li><strong class="red">Warning</strong> — Negative item</li>
    </ul>
</div>
```

---

## 12. Quote

**Theme**: default | **Use**: Citations, key statements

```html
<div class="slide">
    <blockquote>
        "Powerful quote that captures<br>your key message."
    </blockquote>
    <cite>&mdash; Name, Title</cite>
</div>
```

---

## 13. Code Block

**Theme**: default | **Use**: Code snippets, terminal output

```html
<div class="slide">
    <p class="eyebrow">Code</p>
    <h3>Example</h3>
    <div class="code"><span class="comment">// Initialize configuration</span>
<span class="keyword">const</span> config = {
    theme: <span class="string">"dark"</span>,
    enabled: <span class="keyword">true</span>
};</div>
</div>
```

**Syntax classes**: `.comment` (dim), `.keyword` (violet), `.string` (green)

---

## 14. Data Table

**Theme**: default | **Use**: Structured data comparison

```html
<div class="slide">
    <p class="eyebrow">Data</p>
    <h3>Comparison Table</h3>
    <table class="tbl" style="margin-top:2vh;">
        <tr><th>Feature</th><th>Basic</th><th>Pro</th></tr>
        <tr><td>Storage</td><td>10GB</td><td class="green">100GB</td></tr>
        <tr><td>Support</td><td class="red">Email</td><td class="green">24/7</td></tr>
    </table>
</div>
```

---

## 15. Video / Media Placeholder

**Theme**: default | **Use**: Video embeds or media placeholders

Placeholder:
```html
<div class="slide">
    <p class="eyebrow">Demo</p>
    <h2 class="hero" style="font-size:clamp(1.8rem,3vw,2.8rem);">Live Demo</h2>
    <div class="vid-box">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <polygon points="5,3 19,12 5,21" fill="rgba(255,255,255,0.15)"/>
        </svg>
        <span>Video Placeholder</span>
    </div>
</div>
```

Real video:
```html
<div class="slide">
    <p class="eyebrow">Demo</p>
    <video controls style="max-width:760px; width:100%; border:1px solid rgba(255,255,255,0.08); margin-top:3vh;">
        <source src="demo.mp4" type="video/mp4">
    </video>
</div>
```

Real image:
```html
<div class="slide">
    <img src="image.png" alt="Description"
        style="max-width:35vw; max-height:40vh; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.3);">
    <p class="hero-sub" style="font-size:clamp(1rem,1.3vw,1.2rem);">Caption</p>
</div>
```

---

## 16. Closing Slide

**Theme**: default or `blue` | **Use**: Thank you, Q&A

```html
<div class="slide">
    <h1 class="hero">감사합니다</h1>
    <div class="line"></div>
    <p class="hero-sub">Q &amp; A</p>
</div>
```

With colored background:
```html
<div class="slide blue">
    <h1 class="hero">Thank You</h1>
    <div class="line" style="background:rgba(255,255,255,0.3);"></div>
    <p class="hero-sub">Questions?</p>
</div>
```

---

## Inline SVG Icon Style

Use simple stroke-based SVGs for pillar icons and custom visuals:

```html
<svg width="72" height="72" viewBox="0 0 36 36" fill="none"
     stroke="rgba(255,255,255,0.95)" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round">
    <circle cx="18" cy="18" r="12"/>
    <line x1="18" y1="10" x2="18" y2="18"/>
    <line x1="18" y1="18" x2="24" y2="18"/>
</svg>
```

Style: thin white strokes, `opacity: 0.7-0.95`, no fill by default.
For accent SVGs, use `stroke="#60a5fa"` or `fill="#60a5fa"`.

---

## Bottom Caption

Add a positioned caption at the slide bottom:

```html
<p class="caption">Source: Company Report 2026</p>
```

Place inside any `<div class="slide">` — it positions itself at the bottom automatically.

---

## Combining Patterns

Multiple components can be combined in a single slide:

```html
<div class="slide">
    <p class="eyebrow">Results</p>
    <h2 class="hero" style="font-size:clamp(1.8rem,3vw,2.8rem);">AI는 도구<br><span class="accent">책임은 엔지니어</span></h2>
    <div style="display:flex; gap:3vw; margin-top:4vh; width:100%; max-width:800px;">
        <div class="accent-card" style="flex:1;">
            <p class="card-num">5,000<span style="font-size:0.5em; color:rgba(255,255,255,0.4);">+</span></p>
            <p class="card-label">자동 검증 시나리오</p>
        </div>
        <div class="accent-card" style="flex:1;">
            <p class="card-num">90<span style="font-size:0.5em; color:rgba(255,255,255,0.4);">%+</span></p>
            <p class="card-label">테스트 커버리지</p>
        </div>
    </div>
    <div class="flow" style="margin-top:3vh;">
        <span class="flow-step">AI 작성</span>
        <span class="flow-arrow">→</span>
        <span class="flow-step">자동 검증</span>
        <span class="flow-arrow">→</span>
        <span class="flow-step active">사람이 최종 리뷰</span>
    </div>
</div>
```
