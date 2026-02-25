# Design Tokens Quick Reference

## Table of Contents

1. [Section Theme Colors](#section-theme-colors-for-divider-slides)
2. [In-Section Content Themes](#in-section-content-themes-for-content-slides-within-a-section)
3. [Base Themes](#base-themes)
4. [Text Color Helpers](#text-color-helpers)
5. [Typography Scale](#typography-scale)
6. [Fonts](#fonts)
7. [Card Glass-Morphism Pattern](#card-glass-morphism-pattern)
8. [Card State Modifiers](#card-state-modifiers)
9. [Navigation Keyboard Shortcuts](#navigation-keyboard-shortcuts)

## Section Theme Colors (for divider slides)

| Theme | Class | Background | `.em` Color |
|-------|-------|-----------|-------------|
| Samsung | `.samsung` | gradient(#0A1060 > #1428A0 > #1A7AFC) | #7AB8FF |
| Blue | `.blue` | #1428A0 | #7AB8FF |
| Navy | `.navy` | #0D1B5E | #7AB8FF |
| Indigo | `.indigo` | #2D1FA8 | #A5B4FC |
| Violet | `.violet` | #5B1FA8 | #C4B5FD |
| Rose | `.rose` | #A8194A | #FDA4AF |
| Mint | `.mint` | #0A7A56 | #4EEDB4 |
| Teal | `.teal` | #0A6E62 | #4EEAB8 |
| Cyan | `.cyan` | #0A5E82 | #38E8F8 |
| Amber | `.amber` | #A05C00 | #FBCF60 |
| Orange | `.orange` | #C04800 | #FBCF80 |

All section themes set `.sub` to `rgba(255, 255, 255, 0.75)`.

## In-Section Content Themes (for content slides within a section)

| Theme | Class | Background | `.em` Color |
|-------|-------|-----------|-------------|
| In-Blue | `.in-blue` | #0E1228 | #7AB8FF |
| In-Indigo | `.in-indigo` | #0F1030 | #A5B4FC |
| In-Violet | `.in-violet` | #130D28 | #C4B5FD |
| In-Rose | `.in-rose` | #1A0A14 | #FDA4AF |
| In-Mint | `.in-mint` | #081A14 | #4EEDB4 |
| In-Cyan | `.in-cyan` | #081420 | #38E8F8 |
| In-Amber | `.in-amber` | #1A1000 | #FBCF60 |
| In-Orange | `.in-orange` | #1A0E00 | #FBCF80 |
| In-Navy | `.in-navy` | #0A0E28 | #7AB8FF |
| In-Teal | `.in-teal` | #081418 | #4EEAB8 |

## Base Themes

| Theme | Class | Background | Text Color |
|-------|-------|-----------|------------|
| Default dark | `.slide` | transparent (body gradient) | #EFF2FA |
| Surface | `.surface` | #111422 | #EFF2FA |
| Light | `.light` | #F0F4FF | #0C0F1E |

## Text Color Helpers

| Class | Color | Use |
|-------|-------|-----|
| `.em` | #5FB3FF | Primary emphasis (blue) |
| `.red` | #FCA5A5 | Warning, negative |
| `.green` | #10E890 | Success, positive |
| `.yellow` | #F2D7A1 | Caution, highlight |

## Typography Scale

| Element | Size | Weight | Use |
|---------|------|--------|-----|
| `h1` | clamp(3rem, 6vw, 5.5rem) | 900 | Cover/section titles |
| `h2` | clamp(2.2rem, 4.5vw, 4rem) | 700 | Major headings |
| `h3` | 1.28rem | 800 | Content slide titles |
| `.sub` | clamp(1.3rem, 2.2vw, 1.8rem) | 400 | Subtitle text |
| `.meta` | 0.9rem | 400 | Metadata labels |
| `.impact-text` | clamp(2.8rem, 5vw, 4.5rem) | 900 | Impact statements |
| `.impact-sub` | clamp(1.4rem, 2vw, 1.8rem) | 400 | Impact subtitle |
| `.formula` | clamp(1.5rem, 3vw, 2.2rem) | 700 | Concept formulas |
| `.stat .number` | clamp(4rem, 10vw, 8rem) | 900 | Big statistics |
| `.stat-card .value` | clamp(2.5rem, 4vw, 3.5rem) | 900 | Card metrics |
| `blockquote` | clamp(1.6rem, 3vw, 2.2rem) | 300 | Quotes |
| `.list li` | clamp(1.1rem, 1.8vw, 1.5rem) | 400 | List items |
| `.code` | clamp(0.82rem, 0.95vw, 0.92rem) | 400 | Code blocks |

## Fonts

| Type | Font | Weights |
|------|------|---------|
| Primary | Noto Sans KR | 400, 700, 900 |
| Monospace | JetBrains Mono | 400, 600 |
| Icons | Phosphor Icons | via unpkg CDN |

## Card Glass-Morphism Pattern

Shared by `.comp-item`, `.tool-card`, `.stat-card`:

```
background: rgba(255, 255, 255, 0.045)
border: 1px solid rgba(255, 255, 255, 0.07)
border-top: 2px solid rgba(255, 255, 255, 0.12)
box-shadow: 0 14px 34px rgba(0,0,0,0.18), inset 0 1px 0 rgba(255,255,255,0.05)
```

| Component | border-radius |
|-----------|--------------|
| `.comp-item` | 16px |
| `.tool-card` | 16px |
| `.stat-card` | 20px |
| `.grid-item` | 2px (flat style) |
| `.pipeline-step` | 2px (flat style) |

## Card State Modifiers

| State | Meaning | Available on |
|-------|---------|-------------|
| `.on` | Active/highlighted (blue) | comp-item, stat-card, pipeline-step, arch-layer |
| `.green-on` | Success/positive | comp-item, stat-card |
| `.yellow-on` | Warning/caution | comp-item, stat-card |
| `.red-on` | Danger/negative | comp-item, stat-card |
| `.green` | Complete step | pipeline-step |
| `.red` | Failed step | pipeline-step |
| `.violet` | Creative step | pipeline-step |
| `.recommended` | Recommended (green) | tool-card |
| `.hot` | Trending (amber) | tool-card |

## Navigation Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Arrow Right / Space / PageDown | Next slide |
| Arrow Left / PageUp | Previous slide |
| Home | First slide |
| End | Last slide |
| F | Toggle fullscreen |

Touch: Swipe left/right (50px threshold).
URL: `#N` for direct slide access (e.g., `#5` opens slide 5).
