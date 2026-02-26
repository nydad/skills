# UI Style Catalog

Comprehensive catalog of UI styles with visual characteristics, CSS implementation patterns, and usage guidance.

## Table of Contents

1. [Clean Minimal](#clean-minimal)
2. [Swiss Design](#swiss-design)
3. [Scandinavian](#scandinavian)
4. [Flat Design](#flat-design)
5. [Glassmorphism](#glassmorphism)
6. [Neumorphism](#neumorphism)
7. [Claymorphism](#claymorphism)
8. [Brutalism](#brutalism)
9. [Neo-Brutalism](#neo-brutalism)
10. [Memphis Design](#memphis-design)
11. [Maximalist](#maximalist)
12. [Dark Mode Premium](#dark-mode-premium)
13. [Luxury Minimal](#luxury-minimal)
14. [Cyberpunk](#cyberpunk)
15. [Neon Glow](#neon-glow)
16. [Rounded Soft](#rounded-soft)
17. [Pastel](#pastel)
18. [Corporate Enterprise](#corporate-enterprise)
19. [Dashboard / SaaS](#dashboard--saas)
20. [Retro / Vintage](#retro--vintage)
21. [Bento Grid](#bento-grid)
22. [AI-Native](#ai-native)

---

## Clean Minimal

**Visual traits:** Generous whitespace, subtle borders, restrained color, content-first hierarchy.

**Best for:** Fintech, productivity tools, portfolios, documentation sites.
**Avoid for:** Children's apps, gaming, entertainment platforms.

```css
/* Tokens */
--radius: 8px;
--shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
--shadow-md: 0 4px 6px rgba(0,0,0,0.07);
--border: 1px solid #e5e7eb;
--bg-primary: #ffffff;
--bg-secondary: #f9fafb;
--text-primary: #111827;
--text-secondary: #6b7280;

/* Card pattern */
.card {
  background: var(--bg-primary);
  border: var(--border);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow-sm);
}

/* Button pattern */
.btn-primary {
  background: #111827;
  color: #ffffff;
  border: none;
  border-radius: 6px;
  padding: 10px 20px;
  font-weight: 500;
}
```

---

## Swiss Design

**Visual traits:** Strong grid system, bold sans-serif type, asymmetric layouts, limited color with red/black accents.

**Best for:** Portfolios, editorial, design agencies, architecture firms.
**Avoid for:** Playful consumer apps, children's products.

```css
--radius: 0;
--shadow: none;
--border: 2px solid #000000;
--bg-primary: #ffffff;
--text-primary: #000000;
--accent: #ff0000;
--font-heading: 'Helvetica Neue', 'Arial', sans-serif;
--font-weight-heading: 700;
--letter-spacing-heading: -0.02em;

.card {
  background: var(--bg-primary);
  border: var(--border);
  padding: 32px;
}

.heading {
  font-size: 3rem;
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.03em;
  text-transform: uppercase;
}
```

---

## Scandinavian

**Visual traits:** Warm neutrals, rounded elements, organic shapes, natural textures, cozy feel.

**Best for:** Lifestyle brands, wellness, home goods, organic products.
**Avoid for:** Finance, enterprise software, gaming.

```css
--radius: 12px;
--shadow-sm: 0 2px 8px rgba(0,0,0,0.04);
--bg-primary: #faf8f5;
--bg-secondary: #f0ebe4;
--text-primary: #2c2420;
--text-secondary: #7c6f64;
--accent: #c4956a;
--border: 1px solid #e8e0d8;

.card {
  background: var(--bg-primary);
  border: var(--border);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow-sm);
}
```

---

## Flat Design

**Visual traits:** No shadows, no gradients, solid colors, clean iconography, bold geometry.

**Best for:** Mobile apps, Material-influenced UIs, dashboards.
**Avoid for:** Luxury brands, depth-heavy interfaces.

```css
--radius: 4px;
--shadow: none;
--bg-primary: #ffffff;
--bg-accent: #2196f3;
--text-primary: #212121;
--text-on-accent: #ffffff;
--border: none;

.card {
  background: var(--bg-primary);
  border-radius: var(--radius);
  padding: 16px;
}

.btn-primary {
  background: var(--bg-accent);
  color: var(--text-on-accent);
  border: none;
  border-radius: var(--radius);
  padding: 12px 24px;
  text-transform: uppercase;
  font-weight: 500;
  letter-spacing: 0.05em;
}
```

---

## Glassmorphism

**Visual traits:** Frosted glass backgrounds, transparency, blur effects, subtle borders, gradient overlays.

**Best for:** Landing pages, modals, hero sections, creative portfolios.
**Avoid for:** Data-dense dashboards, accessibility-critical apps, low-end devices.

```css
--radius: 16px;
--glass-bg: rgba(255, 255, 255, 0.15);
--glass-border: 1px solid rgba(255, 255, 255, 0.2);
--glass-blur: blur(12px);
--glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);

.card-glass {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border: var(--glass-border);
  border-radius: var(--radius);
  box-shadow: var(--glass-shadow);
  padding: 24px;
}

/* Requires a vibrant background (gradient or image) behind the glass */
.glass-container {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}
```

---

## Neumorphism

**Visual traits:** Soft extruded shapes, dual shadows (light + dark), monochrome palette, tactile feel.

**Best for:** Calculator UIs, music players, experimental projects.
**Avoid for:** Production business apps, complex forms, accessibility-critical (poor contrast).

```css
--bg: #e0e5ec;
--shadow-light: -6px -6px 12px rgba(255, 255, 255, 0.8);
--shadow-dark: 6px 6px 12px rgba(163, 177, 198, 0.6);
--radius: 16px;
--text-primary: #2d3748;

.card-neu {
  background: var(--bg);
  border-radius: var(--radius);
  box-shadow: var(--shadow-light), var(--shadow-dark);
  padding: 24px;
  border: none;
}

.card-neu-inset {
  background: var(--bg);
  border-radius: var(--radius);
  box-shadow: inset -4px -4px 8px rgba(255,255,255,0.7),
              inset 4px 4px 8px rgba(163,177,198,0.5);
  padding: 20px;
}
```

---

## Claymorphism

**Visual traits:** Soft, inflated 3D look, inner highlights, pastel colors, playful depth.

**Best for:** SaaS marketing, onboarding flows, creative apps.
**Avoid for:** Data-heavy dashboards, enterprise tools, government sites.

```css
--radius: 24px;
--bg-card: #f0e6ff;
--shadow: 0 8px 30px rgba(80, 50, 150, 0.12),
          inset 0 -4px 6px rgba(0, 0, 0, 0.05),
          inset 0 4px 6px rgba(255, 255, 255, 0.6);

.card-clay {
  background: var(--bg-card);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  border: 2px solid rgba(255, 255, 255, 0.5);
  padding: 28px;
}
```

---

## Brutalism

**Visual traits:** Raw, unpolished, thick borders, monospace type, clashing colors, no rounded corners.

**Best for:** Art portfolios, music sites, experimental projects, counter-culture brands.
**Avoid for:** Healthcare, finance, enterprise, government, accessibility-critical apps.

```css
--radius: 0;
--border: 3px solid #000000;
--bg-primary: #ffffff;
--bg-accent: #ff5733;
--text-primary: #000000;
--font-body: 'Courier New', monospace;
--shadow: 4px 4px 0px #000000;

.card-brutal {
  background: var(--bg-primary);
  border: var(--border);
  box-shadow: var(--shadow);
  padding: 20px;
}

.btn-brutal {
  background: var(--bg-accent);
  color: #000000;
  border: 3px solid #000000;
  box-shadow: 4px 4px 0px #000000;
  padding: 12px 24px;
  font-family: var(--font-body);
  font-weight: 700;
  text-transform: uppercase;
  cursor: pointer;
  transition: transform 0.1s, box-shadow 0.1s;
}
.btn-brutal:active {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0px #000000;
}
```

---

## Neo-Brutalism

**Visual traits:** Like brutalism but with bold colors, softer shadows, playful illustrations, more approachable.

**Best for:** Startups, indie products, blogs, creative tools.
**Avoid for:** Corporate, healthcare, government.

```css
--radius: 12px;
--border: 2px solid #1a1a2e;
--shadow: 4px 4px 0px #1a1a2e;
--bg-primary: #fffbf0;
--bg-accent: #ffd166;
--bg-secondary: #a8dadc;
--text-primary: #1a1a2e;

.card-neo {
  background: var(--bg-accent);
  border: var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 24px;
}
```

---

## Memphis Design

**Visual traits:** Geometric shapes, bold patterns, clashing colors, squiggles, dots, zigzags, 80s/90s nostalgia.

**Best for:** Youth brands, event marketing, creative campaigns, fashion.
**Avoid for:** Serious enterprise, finance, healthcare, government.

```css
--bg-primary: #fef9ef;
--color-pink: #ff6b9d;
--color-yellow: #ffd93d;
--color-blue: #6bcb77;
--color-purple: #9b5de5;
--radius: 0;
--border: 3px solid #2d2d2d;

.card-memphis {
  background: var(--color-yellow);
  border: var(--border);
  padding: 24px;
  position: relative;
}
.card-memphis::after {
  content: '';
  position: absolute;
  width: 40px; height: 40px;
  background: var(--color-pink);
  border-radius: 50%;
  top: -10px; right: -10px;
}
```

---

## Maximalist

**Visual traits:** Dense layering, mixed media, overlapping elements, rich textures, bold gradients, pattern mixing.

**Best for:** Creative agencies, fashion, art exhibitions, editorial.
**Avoid for:** Utility apps, enterprise dashboards, accessibility-first products.

```css
--gradient-hero: linear-gradient(135deg, #f093fb 0%, #f5576c 50%, #4facfe 100%);
--radius: 20px;
--text-primary: #1a0a2e;
--shadow-lg: 0 20px 60px rgba(0, 0, 0, 0.15);

.card-max {
  background: #ffffff;
  border-radius: var(--radius);
  box-shadow: var(--shadow-lg);
  padding: 32px;
  overflow: hidden;
}
.card-max::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 6px;
  background: var(--gradient-hero);
}
```

---

## Dark Mode Premium

**Visual traits:** Deep dark backgrounds, elevated surfaces, accent colors pop, reduced eye strain, premium feel.

**Best for:** Developer tools, media players, SaaS dashboards, creative software.
**Avoid for:** Print-focused content, brands requiring bright, cheerful aesthetics.

```css
--bg-base: #0a0a0b;
--bg-surface: #141416;
--bg-elevated: #1c1c1f;
--border: 1px solid rgba(255, 255, 255, 0.08);
--text-primary: #f4f4f5;
--text-secondary: #a1a1aa;
--accent: #818cf8;
--radius: 12px;
--shadow: 0 4px 24px rgba(0, 0, 0, 0.4);

.card-dark {
  background: var(--bg-surface);
  border: var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 24px;
}
```

---

## Luxury Minimal

**Visual traits:** Ultra-restrained palette, generous negative space, thin serif fonts, gold/muted accents.

**Best for:** Jewelry, fashion, real estate, premium hospitality.
**Avoid for:** SaaS, developer tools, children's products, gaming.

```css
--bg-primary: #fdfcfa;
--text-primary: #1a1a1a;
--text-secondary: #8a8680;
--accent: #c8a97e;
--border: 1px solid #e8e4de;
--font-heading: 'Playfair Display', serif;
--font-body: 'Lato', sans-serif;
--radius: 2px;
--letter-spacing: 0.15em;

.card-luxury {
  background: var(--bg-primary);
  border: var(--border);
  border-radius: var(--radius);
  padding: 40px;
}

.heading-luxury {
  font-family: var(--font-heading);
  font-weight: 400;
  letter-spacing: 0.05em;
  font-size: 2.5rem;
  line-height: 1.15;
}
```

---

## Cyberpunk

**Visual traits:** Neon on dark, glitch effects, angular shapes, monospace type, scan lines, tech dystopia.

**Best for:** Gaming, tech events, experimental art, music platforms.
**Avoid for:** Healthcare, finance, government, children, accessibility-first apps.

```css
--bg-base: #0d0221;
--bg-surface: #150535;
--neon-cyan: #00fff5;
--neon-pink: #ff00a0;
--neon-yellow: #f8ff00;
--text-primary: #e0e0e0;
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;
--radius: 2px;
--border-neon: 1px solid var(--neon-cyan);

.card-cyber {
  background: var(--bg-surface);
  border: var(--border-neon);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: 0 0 15px rgba(0, 255, 245, 0.15),
              inset 0 0 15px rgba(0, 255, 245, 0.05);
}

.text-glitch {
  text-shadow: 2px 0 var(--neon-pink), -2px 0 var(--neon-cyan);
}
```

---

## Neon Glow

**Visual traits:** Dark backgrounds, vivid neon accents with glow effects, gradient borders, futuristic feel.

**Best for:** Nightlife, music, gaming, event sites, creative portfolios.
**Avoid for:** Enterprise, healthcare, government, education.

```css
--bg-base: #0f0f1a;
--glow-purple: #a855f7;
--glow-blue: #3b82f6;
--glow-pink: #ec4899;
--radius: 16px;

.card-neon {
  background: rgba(15, 15, 26, 0.8);
  border: 1px solid rgba(168, 85, 247, 0.3);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: 0 0 20px rgba(168, 85, 247, 0.1),
              0 0 60px rgba(168, 85, 247, 0.05);
}

.btn-glow {
  background: linear-gradient(135deg, var(--glow-purple), var(--glow-blue));
  color: #ffffff;
  border: none;
  border-radius: 9999px;
  padding: 12px 32px;
  box-shadow: 0 0 20px rgba(168, 85, 247, 0.4);
}
```

---

## Rounded Soft

**Visual traits:** Large border radii, soft shadows, friendly colors, approachable, modern SaaS aesthetic.

**Best for:** Consumer apps, SaaS onboarding, health/wellness, education.
**Avoid for:** Finance, legal, enterprise where formality is needed.

```css
--radius-sm: 12px;
--radius-md: 16px;
--radius-lg: 24px;
--radius-full: 9999px;
--bg-primary: #ffffff;
--bg-secondary: #f0f4ff;
--text-primary: #1e293b;
--shadow-soft: 0 4px 20px rgba(0, 0, 0, 0.06);
--accent: #6366f1;

.card-soft {
  background: var(--bg-primary);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-soft);
  padding: 28px;
  border: 1px solid #e8ecf4;
}

.btn-soft {
  background: var(--accent);
  color: #ffffff;
  border: none;
  border-radius: var(--radius-full);
  padding: 12px 28px;
  font-weight: 600;
}
```

---

## Pastel

**Visual traits:** Muted, desaturated colors, gentle gradients, light feel, low contrast accents.

**Best for:** Wellness, baby products, creative tools, personal blogs, education.
**Avoid for:** Enterprise, finance, gaming, data-heavy dashboards.

```css
--pastel-pink: #fce4ec;
--pastel-blue: #e3f2fd;
--pastel-green: #e8f5e9;
--pastel-purple: #f3e5f5;
--pastel-yellow: #fff9c4;
--bg-primary: #fefefe;
--text-primary: #424242;
--text-secondary: #9e9e9e;
--radius: 16px;

.card-pastel {
  background: var(--pastel-blue);
  border-radius: var(--radius);
  padding: 24px;
  border: 1px solid rgba(0, 0, 0, 0.04);
}
```

---

## Corporate Enterprise

**Visual traits:** Structured layouts, muted blue/gray palette, clear hierarchy, data tables, form-heavy.

**Best for:** B2B SaaS, enterprise dashboards, admin panels, CRM/ERP systems.
**Avoid for:** Consumer-facing creative products, gaming, lifestyle brands.

```css
--bg-primary: #ffffff;
--bg-secondary: #f8fafc;
--bg-sidebar: #1e293b;
--text-primary: #0f172a;
--text-secondary: #64748b;
--accent: #2563eb;
--border: 1px solid #e2e8f0;
--radius: 6px;
--shadow: 0 1px 3px rgba(0, 0, 0, 0.08);

.card-corp {
  background: var(--bg-primary);
  border: var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 20px;
}

.sidebar {
  background: var(--bg-sidebar);
  color: #cbd5e1;
  width: 260px;
  padding: 16px;
}
```

---

## Dashboard / SaaS

**Visual traits:** Dense information layout, data visualization focus, metric cards, compact spacing.

**Best for:** Analytics dashboards, monitoring tools, admin panels, SaaS products.
**Avoid for:** Marketing sites, portfolios, content-heavy blogs.

```css
--bg-base: #f1f5f9;
--bg-card: #ffffff;
--text-primary: #0f172a;
--text-secondary: #64748b;
--text-muted: #94a3b8;
--accent: #3b82f6;
--success: #22c55e;
--warning: #f59e0b;
--error: #ef4444;
--border: 1px solid #e2e8f0;
--radius: 8px;
--shadow: 0 1px 3px rgba(0,0,0,0.06);

.metric-card {
  background: var(--bg-card);
  border: var(--border);
  border-radius: var(--radius);
  padding: 16px 20px;
  box-shadow: var(--shadow);
}

.metric-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1;
}

.metric-label {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 4px;
}
```

---

## Retro / Vintage

**Visual traits:** Warm earth tones, serif fonts, paper textures, aged feel, decorative borders.

**Best for:** Craft brands, artisan products, restaurants, editorial magazines.
**Avoid for:** Tech startups, SaaS, developer tools, children's apps.

```css
--bg-primary: #f5f0e8;
--bg-card: #faf7f2;
--text-primary: #3d2e1e;
--text-secondary: #7a6b5a;
--accent: #c45d35;
--border: 2px solid #d4c5a9;
--radius: 4px;
--font-heading: 'Playfair Display', Georgia, serif;
--font-body: 'Lora', 'Times New Roman', serif;

.card-retro {
  background: var(--bg-card);
  border: var(--border);
  border-radius: var(--radius);
  padding: 28px;
}

.heading-retro {
  font-family: var(--font-heading);
  font-weight: 700;
  color: var(--text-primary);
  border-bottom: 3px double var(--accent);
  padding-bottom: 8px;
}
```

---

## Bento Grid

**Visual traits:** Asymmetric grid layout (Apple-inspired), varied card sizes, rounded cards, clean within each cell.

**Best for:** Feature showcases, product marketing pages, portfolios, landing pages.
**Avoid for:** Data tables, form-heavy apps, text-heavy documentation.

```css
--radius: 20px;
--bg-base: #f5f5f7;
--bg-card: #ffffff;
--shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
--text-primary: #1d1d1f;
--text-secondary: #86868b;

.bento-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 200px;
  gap: 16px;
}

.bento-card {
  background: var(--bg-card);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 28px;
  overflow: hidden;
}

/* Span variations */
.bento-wide { grid-column: span 2; }
.bento-tall { grid-row: span 2; }
.bento-hero { grid-column: span 2; grid-row: span 2; }
```

---

## AI-Native

**Visual traits:** Gradient meshes, animated backgrounds, conversational UI elements, typing indicators, stream-style layouts.

**Best for:** AI products, chatbots, generative tools, tech demos.
**Avoid for:** Traditional e-commerce, government, print-first content.

```css
--bg-base: #0a0a0f;
--bg-surface: #12121a;
--bg-message: #1a1a2e;
--gradient-ai: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
--text-primary: #e4e4e7;
--text-secondary: #71717a;
--accent: #818cf8;
--radius: 16px;

.card-ai {
  background: var(--bg-surface);
  border: 1px solid rgba(129, 140, 248, 0.15);
  border-radius: var(--radius);
  padding: 24px;
}

.gradient-text {
  background: var(--gradient-ai);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.ai-glow {
  box-shadow: 0 0 30px rgba(129, 140, 248, 0.15),
              0 0 60px rgba(118, 75, 162, 0.08);
}
```
