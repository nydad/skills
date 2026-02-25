# Creative Guidelines

Rules for composing custom visual layouts beyond the standard component library.

## Table of Contents

1. [When to Go Custom](#when-to-go-custom)
2. [Core Design Tokens](#core-design-tokens-never-deviate)
3. [Common Custom Patterns](#common-custom-patterns)
   - Icon Array | Highlighted Card | Pill Badges | Circular Highlight | Labeled Container Box
4. [Anti-Patterns](#anti-patterns-never-do-these)
5. [Composition Checklist](#composition-checklist)

## When to Go Custom

Use custom inline compositions ONLY when no standard component fits. Before composing custom:
1. Check if a standard pattern (comp, grid, arch-layers, stat-grid, tool-cards) can be adapted
2. If not, compose using the rules below

## Core Design Tokens (never deviate)

### Colors -- ONLY use these

```
Background darks: rgba(255,255,255,0.03-0.05) for containers
Border: rgba(255,255,255,0.07-0.12) for borders
Text primary: #EFF2FA, #E0E6F0, #D8E0F0, #FFF
Text secondary: rgba(255,255,255,0.4-0.7)
Accent blue: #5FB3FF
Accent green: #10E890
Accent red: #FCA5A5
Accent yellow: #FFCF2F, #F2D7A1
Accent violet: #C4B5FD
```

### Spacing

```
Container gaps: 3vw-4vw for major, 14px-16px for minor
Container padding: 20px-40px
Icon sizes: 1.5rem (small), 3rem (medium), 5rem (large)
Border-radius: 8px (small), 12px (medium), 16px (glass card)
```

### Shadows

```
Standard: 0 10px 30px rgba(0,0,0,0.3)
Glass card: 0 14px 34px rgba(0,0,0,0.18), inset 0 1px 0 rgba(255,255,255,0.05)
Heavy: 0 18px 46px rgba(0,0,0,0.22)
Glow: 0 10px 40px rgba([accent-color], 0.15-0.2)
Drop shadow on icon: filter: drop-shadow(0 0 15px rgba([color], 0.3))
```

## Common Custom Patterns

### Icon Array (horizontal visual metaphor)

Use flex row with centered items and connector arrows:

```html
<div style="display: flex; align-items: center; justify-content: center; gap: 3vw; margin: 6vh 0; width: 100%; max-width: 900px;">
    <div style="text-align: center;">
        <i class="ph-fill ph-[icon]" style="font-size: 5rem; color: rgba(255,255,255,0.3);"></i>
        <p style="color: rgba(255,255,255,0.5); margin-top: 1rem; font-weight: 500; font-size: 1.1rem;">Label</p>
    </div>
    <div style="font-size: 2rem; color: rgba(255,255,255,0.2);"><i class="ph-bold ph-arrow-right"></i></div>
    <div style="text-align: center;">
        <i class="ph-fill ph-[icon]" style="font-size: 5.5rem; color: #10E890;"></i>
        <p style="color: #10E890; margin-top: 1rem; font-weight: 800; font-size: 1.2rem;">Highlighted</p>
    </div>
</div>
```

### Highlighted Card (single emphasis)

```html
<div style="text-align: center; background: rgba(16, 232, 144, 0.1); padding: 30px; border-radius: 16px; border: 2px solid rgba(16, 232, 144, 0.3); box-shadow: 0 10px 40px rgba(16, 232, 144, 0.15);">
    <i class="ph-fill ph-shield-check" style="font-size: 5rem; color: #10E890;"></i>
    <p style="color: #D8E0F0; margin-top: 1rem; font-weight: 700; font-size: 1.2rem;">Title</p>
</div>
```

### Pill Badges (horizontal list)

```html
<div style="display: flex; align-items: center; gap: 16px; background: rgba(255,255,255,0.05); padding: 16px 24px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1);">
    <i class="ph-fill ph-[icon]" style="color: #7AB8FF; font-size: 1.5rem;"></i>
    <span style="font-size: 1.1rem; color: #E0E6F0; font-weight: 500;">Label text</span>
</div>
```

### Circular Highlight

```html
<div style="text-align: center; background: rgba(196, 181, 253, 0.1); border: 2px solid rgba(196, 181, 253, 0.25); width: 160px; height: 160px; border-radius: 50%; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 10px 40px rgba(196, 181, 253, 0.15);">
    <i class="ph-fill ph-robot" style="font-size: 4.5rem; color: #C4B5FD;"></i>
    <strong style="color: #FFF; font-size: 1.1rem;">Label</strong>
</div>
```

### Labeled Container Box

```html
<div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); padding: 40px 30px 30px 30px; border-radius: 16px; position: relative; width: 100%;">
    <div style="position: absolute; top: -14px; left: 30px; background: #111422; padding: 0 15px; color: #99ABCA; font-size: 1rem; font-weight: 700; letter-spacing: 0.1em;">
        <i class="ph-fill ph-hard-drives" style="margin-right: 8px; vertical-align: middle;"></i>Container Label
    </div>
    <!-- inner content here -->
</div>
```

## Anti-Patterns (NEVER do these)

1. **Never use brand new colors** -- only token colors listed above
2. **Never use `position: fixed`** -- that's reserved for navigation chrome
3. **Never use `z-index` higher than 10** -- navigation uses z-index: 100
4. **Never add transitions/animations to slides** -- the system uses instant transitions
5. **Never use external CSS/JS files** -- everything must be in the single HTML file
6. **Never override `.em`, `.red`, `.green`, `.yellow` colors** -- these are semantic tokens
7. **Never use font families other than** Noto Sans KR and JetBrains Mono
8. **Never set `overflow: hidden` on slides** -- slides must be scrollable for tall content

## Composition Checklist

When creating a custom layout, verify:
- [ ] Uses only token colors from the list above
- [ ] Flex-based layout (not absolute positioning within content)
- [ ] Responsive-safe (will stack on mobile at 768px)
- [ ] Readable contrast (text on background)
- [ ] Max-width: 900px for contained compositions (matches template.html)
- [ ] Icons are from Phosphor library only
