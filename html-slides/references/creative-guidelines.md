# Creative Guidelines

Rules for composing custom visual layouts beyond the standard component library.

## Table of Contents

1. [Design Philosophy](#design-philosophy)
2. [When to Go Custom](#when-to-go-custom)
3. [Core Design Tokens](#core-design-tokens-never-deviate)
4. [Common Custom Patterns](#common-custom-patterns)
5. [Inline SVG Icon Style](#inline-svg-icon-style)
6. [Anti-Patterns](#anti-patterns-never-do-these)
7. [Composition Checklist](#composition-checklist)

## Design Philosophy

This design system is **editorial-minimal**:
- **Black base** (#0D0D0D) with white typography
- **Monochromatic** by default — color is a punctuation mark, not a background
- **Thin line separators** instead of card backgrounds
- **Figtree display font** for impact, Noto Sans KR for readability
- **Generous whitespace** — let content breathe
- Color themes (samsung, blue, mint, etc.) are for **occasional accent** — not every slide

## When to Go Custom

Use custom inline compositions ONLY when no standard component fits. Before composing custom:
1. Check if a standard pattern (pillars, compare, stat-row, accent-card, flow) can be adapted
2. If not, compose using the rules below

## Core Design Tokens (never deviate)

### Colors — ONLY use these

```
Background: #0D0D0D (slide), #080808 (code), #000 (body)
Border: rgba(255,255,255,0.05-0.12)
Line decoration: rgba(255,255,255,0.18)

Text primary: #fff
Text secondary: rgba(255,255,255,0.45-0.55)
Text muted: rgba(255,255,255,0.2-0.3)

Accent blue: #60a5fa
Accent blue bg: rgba(96,165,250,0.08)
Accent blue border: rgba(96,165,250,0.3-0.35)

Color helpers:
  Red: #FCA5A5
  Green: #86efac
  Yellow: #F2D7A1
  Violet: #c4b5fd
```

### Spacing

```
Content area: 5vh 10vw padding
Max widths: 960px (pillars), 900px (compare/cards), 800px (stat-row), 760px (video), 720px (code)
Gaps: 3vw-4vw for major, 1.5vw for flow steps
Separator lines: 1px solid rgba(255,255,255,0.08)
Decorative .line: 40px × 1px
Border-radius: 12px (pills), 16px (accent cards), 50% (nav buttons)
```

### Shadows (use sparingly)

```
Subtle: 0 10px 30px rgba(0,0,0,0.3)
Image: box-shadow: 0 10px 30px rgba(0,0,0,0.3); border-radius: 12px;
```

## Common Custom Patterns

### Side-by-side Layout (generic flex)

```html
<div style="display:flex; gap:3vw; margin-top:4vh; width:100%; max-width:800px;">
    <div style="flex:1; text-align:center;">
        <!-- Left content -->
    </div>
    <div style="width:1px; height:14vh; background:rgba(255,255,255,0.12); flex-shrink:0; align-self:center;"></div>
    <div style="flex:1; text-align:center;">
        <!-- Right content -->
    </div>
</div>
```

### Inline Stat Display (mini metrics within a slide)

```html
<div style="display:flex; gap:0; width:100%; max-width:640px; justify-content:center;">
    <div style="flex:1; text-align:center; padding:0 3vw; border-right:1px solid rgba(255,255,255,0.08);">
        <p style="font-size:clamp(2.2rem,3.5vw,3.2rem); font-weight:900; font-family:'Figtree',sans-serif; color:#fff; letter-spacing:-0.03em; line-height:1;">1/5</p>
        <p style="font-size:clamp(0.8rem,1vw,0.9rem); color:rgba(255,255,255,0.35); letter-spacing:0.12em; text-transform:uppercase; margin-top:1vh;">Label</p>
    </div>
    <div style="flex:1; text-align:center; padding:0 3vw;">
        <p style="font-size:clamp(2.2rem,3.5vw,3.2rem); font-weight:900; font-family:'Figtree',sans-serif; color:#60a5fa; letter-spacing:-0.03em; line-height:1;">1/12</p>
        <p style="font-size:clamp(0.8rem,1vw,0.9rem); color:rgba(255,255,255,0.35); letter-spacing:0.12em; text-transform:uppercase; margin-top:1vh;">Label</p>
    </div>
</div>
```

### Accent Highlight Box (single emphasis)

```html
<div style="background:rgba(96,165,250,0.08); border:1px solid rgba(96,165,250,0.3); border-radius:16px; padding:3vh 3vw; text-align:center; max-width:400px;">
    <p style="font-family:'Figtree',sans-serif; font-size:clamp(2.8rem,4.5vw,4rem); font-weight:900; color:#fff; letter-spacing:-0.04em; line-height:1;">Value</p>
    <p style="font-size:clamp(1rem,1.3vw,1.2rem); color:rgba(255,255,255,0.5); letter-spacing:0.1em; text-transform:uppercase; margin-top:1.5vh;">Label</p>
</div>
```

### Full-width Text Divider

```html
<div style="display:flex; align-items:center; gap:2vw; width:100%; max-width:900px; margin:3vh 0;">
    <div style="flex:1; height:1px; background:rgba(255,255,255,0.08);"></div>
    <span style="font-size:clamp(0.8rem,1vw,0.9rem); color:rgba(255,255,255,0.3); letter-spacing:0.18em; text-transform:uppercase; white-space:nowrap;">Section Label</span>
    <div style="flex:1; height:1px; background:rgba(255,255,255,0.08);"></div>
</div>
```

## Inline SVG Icon Style

Use simple, thin-stroke SVGs — no heavy fills, no complex gradients:

```html
<svg width="72" height="72" viewBox="0 0 36 36" fill="none"
     stroke="rgba(255,255,255,0.95)" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round">
    <!-- Simple geometric shapes -->
</svg>
```

Rules:
- **Stroke-based**: `stroke="rgba(255,255,255,0.95)"`, `stroke-width="1.5"`
- **Minimal fill**: Use `fill="none"` by default; small accent fills like `fill="#60a5fa"` for focal points
- **Sizes**: 72×72px for pillar icons, 48×48px for inline, 220×160px for hero illustrations
- **Opacity**: 0.7-0.85 on the `<svg>` element for subtlety
- **No external icon libraries** — all SVGs are inline

## Anti-Patterns (NEVER do these)

1. **Never use glass-morphism** (no `backdrop-filter`, no multi-layer box-shadows on cards)
2. **Never use radial gradient backgrounds** on body — pure black only
3. **Never use `position: fixed`** on content — reserved for nav chrome
4. **Never use `z-index` higher than 10** — navigation uses z-index: 100-200
5. **Never add transitions/animations to slides** — instant navigation only
6. **Never use external CSS/JS files** — everything inline in the single HTML
7. **Never override `.accent`, `.red`, `.green`, `.yellow`** — these are semantic tokens
8. **Never use fonts other than** Figtree, Noto Sans KR, and JetBrains Mono
9. **Never set `overflow: hidden` on `.slide`** — already set in template
10. **Never use colored backgrounds on most slides** — black is the default; color themes are for occasional dividers only (1-3 per deck)
11. **Never use heavy borders or card outlines** — thin 1px separators only

## Composition Checklist

When creating a custom layout, verify:
- [ ] Uses only token colors from the list above
- [ ] Flex-based layout (not absolute positioning within content)
- [ ] Responsive-safe (will stack on mobile at 768px)
- [ ] Readable contrast (white/muted text on dark background)
- [ ] Max-width set appropriately (800-960px for contained content)
- [ ] Figtree font for all display numbers and bold headings
- [ ] Noto Sans KR for body text and descriptions
- [ ] Thin separators (1px) not thick borders
- [ ] No box-shadows on cards (except images and accent cards)
