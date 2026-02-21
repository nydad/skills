---
name: html-slides
description: |
  Professional HTML presentation generator with rich dark theme design system.
  Creates polished, high-impact single-file HTML presentations for any topic.
  Glass-morphism cards, 13 color themes, 25+ components, responsive, accessible.

  Triggers: "presentation", "slides", "ppt", "deck", "slideshow", "발표자료", "슬라이드"
  Auto-triggers: presentation, slides, deck, keynote, pitch, ppt
---

# HTML Slides -- Universal Presentation Generator

Generate professional single-file HTML presentations with a rich dark-theme design system.
Works for any topic: tech talks, business pitches, training, reports, keynotes.

## When to Use

- Creating presentation slides, pitch decks, keynote talks
- Converting text content to visual slides
- Technical talks, conferences, training materials, quarterly reports
- Any request mentioning: PPT, slides, presentation, deck, 발표자료, 슬라이드

## Generation Workflow (2 Phases)

### Phase 1: Narrative Architecture (plan before generating)

1. **Analyze** the topic, audience, tone, and target slide count
2. **Plan the arc**: Opening > Context > Depth sections > Synthesis > Close
3. **Assign section themes** from the palette (use 3-5 distinct section colors, not all 13)
4. **Choose component types** per slide based on content type
5. **Map each slide**: `[theme-class, component-pattern, key-content]`

### Phase 2: HTML Assembly

1. Read `references/template.html` -- copy as output skeleton
2. The template already contains the full `<style>` and `<script>` blocks
3. Read `references/slide-patterns.md` -- use patterns for slide content
4. Fill slides into the `.slides` container
5. Update `<title>`, `<html lang="...">`, `.part-label` text

## Key Rules

- **NEVER invent new CSS classes** -- use only classes from the template's `<style>` block
- **NEVER modify the navigation JS** -- it is complete and correct
- **Copy the `<style>` and `<script>` blocks verbatim** from `template.html`
- Theme progression: use 3-5 section themes per presentation, not all 13
- In-section content slides (`in-*`) follow their parent section theme
- Inline styles ONLY for spacing tweaks (`margin-top`, `gap`), never for colors/fonts
- For custom visual compositions (icon diagrams, etc.), follow `references/creative-guidelines.md`

## Slide Count Guidelines

| Size | Slides | Structure |
|------|--------|-----------|
| Short | 10-15 | title + 3 sections + close |
| Medium | 20-30 | title + 4-5 sections + transitions + close |
| Long | 30-50 | title + 5-7 sections + deep dives + close |

## Content Density

| Profile | Description | Use |
|---------|-------------|-----|
| **Minimal** | One message, large type, maximum whitespace | Keynotes, executive summaries |
| **Balanced** | One point + evidence, mixed components | Tech talks, training (DEFAULT) |
| **Dense** | Multiple data points, stat-grids, tables | Reports, technical docs |

## Theme Quick Reference

**Section themes** (vivid, for divider slides):
`samsung` `blue` `navy` `indigo` `violet` `rose` `mint` `teal` `cyan` `amber` `orange`

**Content themes** (for slides within a section):
`surface` (dark) | `light` (white) | `in-blue` `in-navy` `in-indigo` `in-violet` `in-rose` `in-mint` `in-teal` `in-cyan` `in-amber` `in-orange`

See `references/design-tokens.md` for full color values.

## Component Quick Index

### CORE (use in 80%+ of presentations)

| Type | Class | Purpose |
|------|-------|---------|
| Heading | `h1` `h2` `h3` | h1=cover/section, h2=first content after divider, h3=other content |
| Subtitle | `.sub` | Supporting text below headings |
| Emphasis | `.em` `.red` `.green` `.yellow` | Inline color highlights |
| List | `.list` | Bullet-free centered list |
| Comparison | `.comp` > `.comp-item` | Side-by-side cards (2-4 items) |
| Grid | `.grid` > `.grid-item` | Feature/category cards |
| Table | `.tbl` | Data comparison tables |
| Code | `.code` | Code blocks with syntax highlighting |
| Quote | `blockquote` + `cite` | Impactful citations |

### EXTENDED (use as needed)

| Type | Class | Purpose |
|------|-------|---------|
| Stat Grid | `.stat-grid` > `.stat-card` | Multi-metric dashboards (2x2) |
| Architecture | `.arch-layers` > `.arch-layer` | Layered stack diagrams |
| Tool Cards | `.tool-cards` > `.tool-card` | Product/tool showcases with tags |
| Pipeline | `.pipeline` > `.pipeline-step` | Sequential process flows |
| Big Stat | `.stat` > `.number` + `.label` | Single impressive statistic |
| Impact Text | `.impact-text` + `.impact-sub` | Bold typographic statements |
| Formula | `.formula` | Concept equations |
| Alerts | `.note.warn` / `.note.tip` | Warning and tip callouts |
| Two Column | `.two-col` > `.col` | Side-by-side layout |
| Image | `.img` or `<img>` | Placeholder or real image |
| Background | `.big` | Decorative watermark number |
| Meta | `.meta` | Uppercase metadata labels |

See `references/slide-patterns.md` for complete HTML snippets.

## Slide Sequencing Tips

1. **Start strong**: Cover (`samsung` or `blue`) > First section divider (colored)
2. **Build rhythm**: Alternate `surface` / default dark / colored themes
3. **Data sandwich**: Context > Stat > Insight
4. **Visual breaks**: Insert image/quote slides between data-heavy slides
5. **Section flow**: Section divider (colored) > 2-4 content slides (`in-*` or `surface`)
6. **End with impact**: Quote > Summary > Closing (`blue`)

### Theme Pairing Guide

| Content Type | Section Theme | Content Theme |
|-------------|--------------|---------------|
| Technical | cyan / teal | surface / in-cyan / in-teal |
| Business | blue / navy | surface / in-blue / in-navy |
| Creative | violet / indigo | in-violet / in-indigo |
| Success | mint | in-mint |
| Warning/Risk | orange / rose | in-orange / in-rose |
| Strategy | amber | in-amber |

## Validation Checklist

- [ ] Single `.html` file with all CSS/JS inline
- [ ] Google Fonts link (Noto Sans KR + JetBrains Mono) present
- [ ] Phosphor Icons CDN link present
- [ ] `<html lang="...">` set correctly (ko, en, etc.)
- [ ] `.part-label` text updated
- [ ] `<title>` updated
- [ ] All slides have appropriate theme class
- [ ] Navigation JS present and unmodified
- [ ] `<nav>` with `aria-label` on buttons present
- [ ] `.page-num` and `.progress` elements present
- [ ] Responsive `@media (max-width: 768px)` in CSS
- [ ] Print `@media print` in CSS
- [ ] Reduced-motion `@media (prefers-reduced-motion)` in CSS
- [ ] No invented CSS classes -- only those from template

## References

- `references/template.html` -- Complete base template (CSS + JS + skeleton)
- `references/slide-patterns.md` -- All component HTML patterns with examples
- `references/design-tokens.md` -- Quick-reference color/typography cheat sheet
- `references/creative-guidelines.md` -- Rules for custom visual compositions
