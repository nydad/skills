---
name: html-slides
disable-model-invocation: true
description: |
  Generates professional single-file HTML presentations with a minimal black editorial design.
  Use this skill whenever the user wants to create slides, a presentation, pitch deck, keynote talk, training material,
  or conference talk — even if they just say "발표자료 만들어줘", "슬라이드 좀", "PPT 만들어", "프레젠테이션 준비해줘".
  Figtree display font, monochromatic base with accent colors, thin-line separators, optional section color themes.
  Also triggers on: presentation, slides, ppt, deck, slideshow, keynote, pitch, 발표, 프레젠테이션.
---

# HTML Slides — Minimal Black Editorial Presentation Generator

Generate professional single-file HTML presentations with a minimal black editorial design.
Works for any topic: tech talks, business pitches, training, reports, keynotes.

## When to Use

- Creating presentation slides, pitch decks, keynote talks
- Converting text content to visual slides
- Technical talks, conferences, training materials, quarterly reports
- Any request mentioning: PPT, slides, presentation, deck, 발표자료, 슬라이드

## Design Philosophy

> **Editorial-minimal**: Black base, white typography, thin separators, color as punctuation.

- **Background**: Pure black (#0D0D0D) — not gradient, not textured
- **Typography**: Figtree (display/numbers) + Noto Sans KR (body)
- **Color**: Monochromatic by default; `.accent` (#60a5fa) for emphasis
- **Section themes**: Optional colored dividers (samsung, blue, mint, etc.) — use 1-3 per deck
- **Layout**: Thin 1px line separators, generous whitespace, no glass-morphism
- **Navigation**: Round buttons, 1px progress bar

## Generation Workflow (2 Phases)

> **You are an adaptive presentation agent.** Every deck should be uniquely shaped by its topic, audience, tone, and purpose.

### Phase 1: Narrative Architecture (plan before generating)

1. **Analyze** the topic, audience, tone, and purpose — then decide the format:
   - Lightning talk / elevator pitch: **5-7 slides**
   - Standard talk / training: **15-25 slides**
   - Deep-dive / technical report: **30-40 slides**
2. **Plan the arc**: Opening → Context → Depth sections → Synthesis → Close
3. **Choose color accents**: Pick 1-3 section themes for divider slides (rest stay black)
4. **Choose component types** per slide based on content type
5. **Map each slide**: `[theme, component-pattern, key-content]`

### Phase 1 Output Format

Before generating HTML, output this planning table:

| # | Section | Theme | Component | Key Message |
|---|---------|-------|-----------|-------------|
| 1 | Opening | (default) | cover | Title + hook |
| 2 | Context | (default) | pillars | Background, 3 key areas |
| 3-5 | Core | in-blue | compare + stat-row | Main argument with data |
| 6 | Insight | (default) | quote | Key takeaway |
| 7 | Close | blue | closing | Thank you + Q&A |

*(Adapt rows to actual slide count decided in step 1.)*

### Phase 1.5: Content Research (for unfamiliar topics)

When the topic needs research, run parallel research before HTML assembly:

| Track | Focus |
|-------|-------|
| Content Researcher | Find 5 key statistics, 3 expert quotes, main arguments |
| Visual Reference | Find exemplary presentations, extract visual patterns |

Skip this phase if the topic is well-known or user provided all content.

### Phase 2: HTML Assembly

1. Read `references/template.html` — copy as output skeleton
2. The template already contains the full `<style>` and `<script>` blocks
3. Read `references/slide-patterns.md` — use patterns for slide content
4. Fill slides into the `.deck` container
5. Update `<title>` and `<html lang="...">`

## Key Rules

- **NEVER invent new CSS classes** — use only classes from the template's `<style>` block
- **NEVER modify the navigation JS** — it is complete and correct
- **Copy the `<style>` and `<script>` blocks verbatim** from `template.html`
- **Most slides should be plain black** (no theme class) — color themes are accents
- Use 1-3 section color themes per deck, not more
- In-section content slides (`in-*`) follow their parent section theme
- Inline styles ONLY for spacing tweaks (`margin-top`, `gap`, `max-width`)
- For custom visual compositions, follow `references/creative-guidelines.md`

## Slide Count Guidelines

| Size | Slides | Structure |
|------|--------|-----------|
| Short | 5-10 | cover + 2-3 sections + close |
| Medium | 15-25 | cover + 4-5 sections + close |
| Long | 30-40 | cover + 5-7 sections + deep dives + close |

## Content Density

| Profile | Description | Use |
|---------|-------------|-----|
| **Minimal** | One message, large type, maximum whitespace | Keynotes, executive summaries |
| **Balanced** | One point + evidence, mixed components | Tech talks, training (DEFAULT) |
| **Dense** | Multiple data points, stat-rows, tables | Reports, technical docs |

## Theme Quick Reference

**Section themes** (colored, for divider slides — use sparingly):
`samsung` `blue` `navy` `indigo` `violet` `rose` `mint` `teal` `cyan` `amber` `orange`

**Content themes** (dark-tinted, for slides within a section):
`in-blue` `in-navy` `in-indigo` `in-violet` `in-rose` `in-mint` `in-teal` `in-cyan` `in-amber` `in-orange`

**Default**: No class = black (#0D0D0D) — this is what most slides should use.

See `references/design-tokens.md` for full color values.

## Component Quick Index

### CORE (use in 80%+ of presentations)

| Type | Class | Purpose |
|------|-------|---------|
| Hero Title | `.hero` | Cover/section titles (Figtree 900) |
| Subtitle | `.hero-sub` | Supporting text below hero |
| Eyebrow | `.eyebrow` | Category label above title |
| Accent | `.accent` | Inline blue emphasis |
| Line | `.line` | Thin decorative 40px divider |
| List | `.list` | Centered bullet-free list |
| Quote | `blockquote` + `cite` | Impactful citations |
| Code | `.code` | Code blocks (JetBrains Mono) |
| Table | `.tbl` | Data comparison tables |

### EDITORIAL (new minimal components)

| Type | Class | Purpose |
|------|-------|---------|
| Big Number | `.bignum` + `.bignum-label` | Single impressive statistic |
| Pillars | `.pillars` > `.pillar` | 3-4 text columns with thin separators |
| Comparison | `.compare` > `.compare-side` | Before/after with central divider |
| Stat Row | `.stat-row` > `.stat-cell` | Horizontal metric cells |
| Accent Card | `.accent-card` | Highlighted metric box with blue border |
| Flow | `.flow` > `.flow-step` | Sequential text process |
| Pill | `.pill` | Keyword/technology badge |
| Video Box | `.vid-box` | Media placeholder |
| Caption | `.caption` | Bottom-positioned text |

### HELPERS

| Class | Purpose |
|-------|---------|
| `.accent` | Blue emphasis (#60a5fa) |
| `.red` | Warning/negative (#FCA5A5) |
| `.green` | Success/positive (#86efac) |
| `.yellow` | Caution/highlight (#F2D7A1) |
| `h2.hero` | Smaller hero (content headings) |
| `h3` | Slide subheading |

See `references/slide-patterns.md` for complete HTML snippets.

## Slide Sequencing Tips

1. **Start strong**: Cover (black, hero text) → First section
2. **Build rhythm**: Black → Black → Colored divider → Black → Black
3. **Data sandwich**: Context → Big Number or Stat Row → Insight
4. **Visual breaks**: Insert quote/image slides between data-heavy slides
5. **Section flow**: Colored divider → 2-4 black content slides → Next divider
6. **End with impact**: Quote → Summary → Closing (black or blue)

## Large Presentation Strategy

> **Single Write > 800 lines → UND_ERR_SOCKET.** Always use chunked pattern for 20+ slide decks.

```
Write skeleton (CSS + Script + first 5 slides, ~600 lines)
  → Edit × N (insert remaining slides in groups of 3-5)
  → Verify (check total slide count matches plan)
```

### Phase 3: Browser Verification (chrome tools)

After HTML file is saved, verify the actual rendering in Chrome:

1. **Open the file** — use `mcp__claude-in-chrome__navigate` to open the generated HTML file
2. **Cover slide check** — verify title, subtitle, typography renders correctly
3. **Spot-check 3 slides** — navigate to slides #1, middle, last using `#N` hash
4. **Fix issues** — if any rendering problems found, edit the HTML and re-verify

> Skip Phase 3 if: user explicitly says no verification needed, or chrome tools are unavailable.

## Validation Checklist

**After generating, verify each item:**

```
[ ] Single .html file with all CSS/JS inline
[ ] Google Fonts link (Figtree + Noto Sans KR + JetBrains Mono) present
[ ] <html lang="..."> set correctly (ko, en, etc.)
[ ] <title> updated to match presentation title
[ ] All slides use `.slide` class; colored themes applied sparingly
[ ] Navigation JS present and unmodified from template
[ ] <nav> with aria-label on buttons present
[ ] .page-num and .progress elements present
[ ] Responsive @media (max-width: 768px) in CSS
[ ] Print @media print in CSS
[ ] Reduced-motion @media (prefers-reduced-motion) in CSS
[ ] No invented CSS classes — only those from template
[ ] Most slides are plain black (no theme class)
```

## Common Mistakes

| Mistake | Correct Approach |
|---------|-----------------|
| `class="my-custom-card"` — inventing CSS | Only use classes from template `<style>` |
| Modified `<script>` — editing nav JS | Copy JS verbatim from `template.html` |
| `style="color: #123456"` inline theming | Use `.accent`, `.red`, `.green`, `.yellow` |
| Every slide has a colored theme | Most slides should be plain black |
| Glass-morphism cards with box-shadows | Use thin separators and `.accent-card` |
| Heavy borders on components | 1px rgba(255,255,255,0.08) maximum |
| Using Phosphor Icons CDN | Use inline SVGs (stroke-based) |

## Reference Loading Guide

**Always load first:**
- `references/template.html` — Base HTML skeleton (required for all outputs)

**Load for component selection:**
- `references/slide-patterns.md` — When choosing slide components

**Load for styling decisions:**
- `references/design-tokens.md` — When selecting themes or customizing colors

**Load for advanced compositions only:**
- `references/creative-guidelines.md` — Only for custom visual compositions

## References

- `references/template.html` — Complete base template (CSS + JS + skeleton)
- `references/slide-patterns.md` — All component HTML patterns with examples
- `references/design-tokens.md` — Quick-reference color/typography cheat sheet
- `references/creative-guidelines.md` — Rules for custom visual compositions
