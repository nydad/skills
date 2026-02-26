---
name: design-system
description: |
  Generates complete design systems tailored to project context, industry, and audience.
  Use when starting a new project, refreshing a brand, standardizing UI styles, or capturing an existing design into reusable tokens.
  Produces design tokens (CSS/Tailwind/JSON), color palettes, typography pairings, and component guidelines.
  Supports 30+ UI styles with industry-specific reasoning.

  Triggers: design system, design tokens, UI style, color palette, typography, 디자인 시스템, 디자인 토큰
---

# Design System Generator

Generate complete, implementation-ready design systems tailored to project context, industry, audience, and brand personality. Outputs design tokens, color palettes, typography, spacing, component guidelines, and style documentation.

## When to Use

- Starting a new project and need a cohesive visual foundation
- Brand refresh or visual identity update
- Documenting an existing design system for team alignment
- Capturing an existing UI's visual aesthetics into a reusable specification
- Standardizing styles across multiple projects or teams
- Any request mentioning: design system, design tokens, UI style, color palette, typography scale

## Generation Workflow (3 Phases)

> **You are an adaptive design system agent.** Every design system should be uniquely shaped by its industry, audience, brand personality, tech stack, and project goals. Style choices, color palettes, typography pairings, and component patterns must all emerge from reasoned analysis of context -- never produce generic or one-size-fits-all output.

### Phase 1: Context Analysis (plan before generating)

1. **Identify the industry** -- fintech, healthcare, e-commerce, SaaS, creative agency, education, etc.
2. **Define the audience** -- developers, end users, enterprise buyers, consumers, children, elderly
3. **Determine brand personality** -- professional, playful, luxurious, minimal, bold, trustworthy
4. **Assess the tech stack** -- React, Vue, Tailwind, vanilla CSS, native mobile, etc.
5. **Check existing assets** -- logos, brand colors, existing components, style guides
6. **Select a UI style** from the catalog (see Style Categories below)
7. **Choose output format(s)** -- CSS variables, Tailwind config, JSON tokens, documentation

### Phase 1 Output Format

Before generating tokens, output this decision summary:

| Dimension | Decision | Rationale |
|-----------|----------|-----------|
| Industry | e.g., Fintech | Requires trust, stability cues |
| Audience | e.g., Professional adults 25-45 | Clean, efficient, no clutter |
| Brand Personality | e.g., Trustworthy + Modern | Blue-dominant, clean lines |
| UI Style | e.g., Clean Minimal | Industry standard for finance |
| Color Strategy | e.g., Blue primary, Green accent | Trust + growth association |
| Typography | e.g., Inter + Source Serif 4 | Geometric clarity + editorial warmth |
| Output Format | e.g., CSS + Tailwind | Project uses Tailwind CSS |

*(Adapt rows to actual project context.)*

### Phase 2: Design Decisions

Based on Phase 1 analysis, make reasoned choices for each design dimension:

1. **Style selection** -- Pick 1 primary style, optionally 1 secondary influence
2. **Color palette** -- Generate full palette: primary, secondary, accent, neutrals (50-950), semantic colors
3. **Typography** -- Select heading + body font pair, define modular scale
4. **Spacing** -- Define base unit and scale (4px or 8px grid)
5. **Border radius** -- Consistent radius scale matching chosen style
6. **Shadows** -- Elevation system (sm, md, lg, xl)
7. **Breakpoints** -- Responsive breakpoints for target devices

### Phase 3: Output Generation

Generate implementation-ready artifacts:

1. **Design tokens** in requested format(s)
2. **Color palette** with all shades, semantic mappings, dark mode variants
3. **Typography scale** with responsive sizes
4. **Spacing scale** with named values
5. **Component guidelines** -- buttons, cards, inputs, navigation patterns
6. **Documentation** summarizing all decisions and usage guidelines

## UI Style Categories (Quick Reference)

| Category | Styles | Signature Traits |
|----------|--------|-----------------|
| Modern Minimal | Clean, Swiss, Scandinavian, Flat | Whitespace, grid, sharp or subtle radius |
| Glass & Depth | Glassmorphism, Neumorphism, Claymorphism | Transparency, blur, soft shadows |
| Bold & Expressive | Brutalism, Neo-Brutalism, Memphis, Maximalist | Thick borders, clashing colors, raw type |
| Dark & Premium | Dark Mode, Luxury, Cyberpunk, Neon Glow | Deep backgrounds, high contrast accents |
| Soft & Friendly | Rounded, Pastel, Playful, Kawaii | Large radius, soft colors, bouncy elements |
| Enterprise | Corporate, Dashboard, SaaS, Data-Dense | Neutral palettes, information hierarchy |
| Retro & Nostalgic | Retro, Pixel, Vaporwave, Y2K, Skeuomorphism | Period-specific textures, gradients |
| Experimental | AI-Native, Bento Grid, Kinetic, Glassmorphism Dark | Asymmetric grids, animation-first, novel layouts |

> Full style catalog with CSS patterns: `references/ui-styles.md`

## Industry to Style Mapping

| Industry | Recommended Styles | Color Direction | Key Principle |
|----------|-------------------|-----------------|---------------|
| Fintech / Banking | Clean Minimal, Corporate | Blues, greens, neutrals | Trust + stability |
| Healthcare | Soft, Clean, Rounded | Soft blues, greens, whites | Calm + accessibility-first |
| E-commerce | Bold, Modern, Playful | Vibrant primary + warm accents | Conversion-optimized |
| SaaS / Developer Tools | Dark Mode, Dashboard, Flat | Dark backgrounds, neon accents | Information-dense, scannable |
| Creative / Agency | Brutalism, Maximalist, Bento | Bold palette, custom type | Brand-forward, memorable |
| Education | Rounded, Pastel, Playful | Friendly, warm palette | Approachable, clear hierarchy |
| Luxury / Fashion | Dark Premium, Minimal, Swiss | Black, gold, muted tones | Elegance, exclusivity |
| Government / Legal | Corporate, Clean | Navy, gray, muted | Formality, credibility |
| Gaming / Entertainment | Neon, Cyberpunk, Kinetic | High-saturation, dark base | Energy, immersion |
| Wellness / Lifestyle | Scandinavian, Soft, Pastel | Earth tones, sage, cream | Natural, calming |

## Output Formats

Generate tokens in one or more of these formats based on tech stack:

### CSS Custom Properties
```css
:root {
  --color-primary-500: #2563eb;
  --font-heading: 'Inter', sans-serif;
  --spacing-4: 1rem;
  --radius-md: 0.5rem;
}
```

### Tailwind CSS Config
```js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: { 500: '#2563eb' },
      },
      fontFamily: {
        heading: ['Inter', 'sans-serif'],
      },
    },
  },
};
```

### JSON Design Tokens
```json
{
  "color": {
    "primary": { "500": { "value": "#2563eb" } }
  },
  "font": {
    "heading": { "value": "'Inter', sans-serif" }
  }
}
```

### Documentation (Markdown)
A human-readable style guide documenting all tokens, usage guidelines, and do/don't examples.

## Color Palette Generation Rules

Every palette must include:

| Role | Purpose | Count |
|------|---------|-------|
| Primary | Brand identity, CTAs, key actions | 50-950 scale (10 shades) |
| Secondary | Supporting elements, secondary actions | 50-950 scale |
| Accent | Highlights, badges, decorative elements | 50-950 scale |
| Neutral | Text, backgrounds, borders, dividers | 50-950 scale |
| Success | Positive feedback, confirmations | Single shade + light/dark variant |
| Warning | Caution states, pending actions | Single shade + light/dark variant |
| Error | Errors, destructive actions, alerts | Single shade + light/dark variant |
| Info | Informational messages, tooltips | Single shade + light/dark variant |

**Accessibility requirements:**
- Body text on background: minimum WCAG AA (4.5:1 contrast ratio)
- Large text / headings: minimum 3:1 contrast ratio
- Interactive elements: minimum 3:1 against adjacent colors
- Always provide dark mode variants with equivalent contrast

> Full industry-tailored palettes: `references/color-palettes.md`

## Typography Scale

Use a modular scale ratio appropriate to the project:

| Ratio | Name | Best For |
|-------|------|----------|
| 1.200 | Minor Third | Compact UIs, dashboards, data-dense layouts |
| 1.250 | Major Third | General purpose, most web applications |
| 1.333 | Perfect Fourth | Marketing sites, editorial, presentations |
| 1.500 | Perfect Fifth | Hero sections, landing pages, luxury brands |

**Base size:** 16px (1rem) for body text. Scale up/down using the chosen ratio.

**Responsive pattern (fluid typography):**
```css
/* Example: Major Third scale, fluid between 320px and 1280px */
--font-size-base: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
--font-size-lg: clamp(1.25rem, 1.15rem + 0.5vw, 1.5rem);
--font-size-xl: clamp(1.563rem, 1.35rem + 1.06vw, 2rem);
--font-size-2xl: clamp(1.953rem, 1.6rem + 1.76vw, 2.75rem);
```

> Full font pairing catalog: `references/typography-guide.md`

## Spacing Scale

Use a consistent base unit (4px recommended for most projects):

```
--spacing-0:  0
--spacing-px: 1px
--spacing-0.5: 0.125rem  /* 2px */
--spacing-1:  0.25rem    /* 4px */
--spacing-2:  0.5rem     /* 8px */
--spacing-3:  0.75rem    /* 12px */
--spacing-4:  1rem       /* 16px */
--spacing-5:  1.25rem    /* 20px */
--spacing-6:  1.5rem     /* 24px */
--spacing-8:  2rem       /* 32px */
--spacing-10: 2.5rem     /* 40px */
--spacing-12: 3rem       /* 48px */
--spacing-16: 4rem       /* 64px */
--spacing-20: 5rem       /* 80px */
--spacing-24: 6rem       /* 96px */
```

## Design System Capture Mode

When analyzing an existing UI (screenshot, URL, or codebase):

1. **Extract colors** -- identify primary, secondary, accent, neutral, semantic
2. **Identify typography** -- detect font families, sizes, weights, line heights
3. **Measure spacing** -- determine base unit and scale pattern
4. **Catalog components** -- list UI components with their visual properties
5. **Document patterns** -- note recurring layouts, card styles, button variants
6. **Generate tokens** -- output in requested format matching extracted values

## Validation Checklist

**After generating, copy this checklist and verify each item:**

```
[ ] All color values are real hex codes (no placeholders like #PRIMARY)
[ ] Primary text on background meets WCAG AA contrast (4.5:1)
[ ] Font families are available (Google Fonts, system fonts, or bundled)
[ ] Spacing scale follows consistent base unit multiplication
[ ] Border radius values are consistent across component types
[ ] Dark mode palette provided with equivalent contrast ratios
[ ] Design tokens use consistent naming convention throughout
[ ] Typography scale uses a single modular ratio consistently
[ ] Semantic colors (success/warning/error/info) are distinct and accessible
[ ] Output format matches project's tech stack
[ ] Component guidelines reference the generated tokens (not hardcoded values)
```

## Common Mistakes

| | Pattern | Fix |
|---|---------|-----|
| ❌ | Using 5+ font families across the system | ✅ One heading + one body font (2 families max) |
| ❌ | `color: #2563eb` hardcoded in components | ✅ `color: var(--color-primary-500)` using tokens |
| ❌ | Inventing random spacing values (13px, 17px, 22px) | ✅ Consistent scale: 4, 8, 12, 16, 24, 32, 48, 64 |
| ❌ | Same blue for info messages and error states | ✅ Distinct semantic colors: blue=info, red=error, green=success |
| ❌ | Generating light mode only | ✅ Always provide both light and dark mode tokens |
| ❌ | No contrast checking on color combinations | ✅ Verify WCAG AA (4.5:1) for all text/background pairs |
| ❌ | Generic palette ignoring industry context | ✅ Reason about industry norms (finance=trust blue, health=calm green) |
| ❌ | Border radius: 4px on buttons, 12px on cards, 2px on inputs | ✅ Consistent radius scale: sm=4px, md=8px, lg=12px applied by role |
| ❌ | Typography with no responsive scaling | ✅ Use clamp() for fluid type between breakpoints |
| ❌ | Generating tokens without usage documentation | ✅ Include component guidelines showing how to apply each token |

## Reference Loading Guide

**Always read first:**
- This SKILL.md -- core workflow and decision logic

**Load for style selection:**
- `references/ui-styles.md` -- When choosing or comparing UI styles, visual characteristics, CSS patterns

**Load for color decisions:**
- `references/color-palettes.md` -- Industry-tailored palettes, full hex values, dark/light variants

**Load for typography decisions:**
- `references/typography-guide.md` -- Font pairings, modular scales, responsive patterns

## Reference Files

- `references/ui-styles.md` -- 20+ UI style catalog with visual traits, CSS patterns, and usage guidance
- `references/color-palettes.md` -- 15+ industry-tailored palettes with full hex scales and dark mode
- `references/typography-guide.md` -- 25+ font pairings, modular scales, fluid typography patterns
