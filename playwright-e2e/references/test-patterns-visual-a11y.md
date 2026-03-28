# Test Patterns: Interactive Components, Visual Regression, and Accessibility

Common E2E test patterns for interactive UI components, visual regression testing, and accessibility compliance. Each pattern includes when to use, TypeScript code, key assertions, and common gotchas.

## Table of Contents

1. [Interactive Components](#1-interactive-components)
   - [Modals and Dialogs](#modals-and-dialogs)
   - [Dropdowns and Select Menus](#dropdowns-and-select-menus)
   - [Drag and Drop](#drag-and-drop)
   - [Tabs and Accordions](#tabs-and-accordions)
2. [Visual Regression](#2-visual-regression)
   - [Screenshot Comparison Setup](#screenshot-comparison-setup)
   - [Viewport Matrix Testing](#viewport-matrix-testing)
   - [Threshold Configuration](#threshold-configuration)
3. [Accessibility](#3-accessibility)
   - [axe-core Integration](#axe-core-integration)
   - [Keyboard Navigation](#keyboard-navigation)
   - [Focus Management](#focus-management)

---

## 1. Interactive Components

### Modals and Dialogs

**When to use:** Modal dialogs, confirmation popups, side panels.

```typescript
test.describe('Modals', () => {
  test('should open and close modal', async ({ page }) => {
    await page.goto('/items');
    await page.getByRole('button', { name: 'Delete item' }).first().click();

    const dialog = page.getByRole('dialog');
    await expect(dialog).toBeVisible();
    await expect(dialog.getByText('Are you sure?')).toBeVisible();

    await dialog.getByRole('button', { name: 'Cancel' }).click();
    await expect(dialog).not.toBeVisible();
  });

  test('should close modal with Escape key', async ({ page }) => {
    await page.goto('/items');
    await page.getByRole('button', { name: 'Delete item' }).first().click();
    await expect(page.getByRole('dialog')).toBeVisible();

    await page.keyboard.press('Escape');
    await expect(page.getByRole('dialog')).not.toBeVisible();
  });

  test('should confirm destructive action', async ({ page }) => {
    await page.goto('/items');
    const itemCount = await page.getByTestId('item-row').count();

    await page.getByRole('button', { name: 'Delete item' }).first().click();
    await page.getByRole('dialog').getByRole('button', { name: 'Delete' }).click();

    await expect(page.getByTestId('item-row')).toHaveCount(itemCount - 1);
  });
});
```

**Key assertions:** Dialog visible/hidden, Escape key closes, action completes after confirm.
**Gotcha:** Use `getByRole('dialog')` to scope assertions within the modal -- avoids matching background content.

### Dropdowns and Select Menus

**When to use:** Custom dropdown menus, select components, comboboxes.

```typescript
test('should select option from dropdown', async ({ page }) => {
  await page.goto('/form');

  // Native <select>
  await page.getByLabel('Country').selectOption('US');
  await expect(page.getByLabel('Country')).toHaveValue('US');

  // Custom combobox / listbox
  await page.getByRole('combobox', { name: 'Role' }).click();
  await page.getByRole('option', { name: 'Admin' }).click();
  await expect(page.getByRole('combobox', { name: 'Role' })).toContainText('Admin');
});

test('should filter dropdown options by typing', async ({ page }) => {
  await page.goto('/form');
  const combobox = page.getByRole('combobox', { name: 'City' });
  await combobox.fill('New');

  const options = page.getByRole('option');
  await expect(options).toHaveCount(2); // New York, New Orleans
  await options.first().click();
  await expect(combobox).toHaveValue('New York');
});
```

**Key assertions:** Selected value reflected in control, filtered options reduce count, keyboard navigation works.
**Gotcha:** Custom dropdowns use `role="combobox"` + `role="option"` -- use these roles, not CSS classes.

### Drag and Drop

**When to use:** Drag-and-drop interfaces (kanban boards, sortable lists, file drop zones).

```typescript
test('should reorder items via drag and drop', async ({ page }) => {
  await page.goto('/kanban');

  const source = page.getByText('Task A');
  const target = page.getByText('Task C');

  await source.dragTo(target);

  // Verify new order
  const items = page.getByTestId('task-item');
  await expect(items.nth(0)).toContainText('Task B');
  await expect(items.nth(1)).toContainText('Task A');
});

test('should move card between columns', async ({ page }) => {
  await page.goto('/kanban');

  const card = page.getByText('Task A');
  const doneColumn = page.getByTestId('column-done');

  await card.dragTo(doneColumn);
  await expect(doneColumn.getByText('Task A')).toBeVisible();
});
```

**Key assertions:** Element appears in new position, source list updated, drop target receives item.
**Gotcha:** `dragTo` works for most HTML5 DnD -- for complex libraries (react-beautiful-dnd), you may need manual mouse event sequences.

### Tabs and Accordions

**When to use:** Tab panels, accordions, collapsible sections.

```typescript
test.describe('Tabs', () => {
  test('should switch tab content', async ({ page }) => {
    await page.goto('/settings');
    await page.getByRole('tab', { name: 'Profile' }).click();
    await expect(page.getByRole('tabpanel')).toContainText('Display name');

    await page.getByRole('tab', { name: 'Security' }).click();
    await expect(page.getByRole('tabpanel')).toContainText('Change password');
  });

  test('should navigate tabs with keyboard', async ({ page }) => {
    await page.goto('/settings');
    await page.getByRole('tab', { name: 'Profile' }).focus();
    await page.keyboard.press('ArrowRight');
    await expect(page.getByRole('tab', { name: 'Security' })).toBeFocused();

    await page.keyboard.press('Enter');
    await expect(page.getByRole('tabpanel')).toContainText('Change password');
  });
});

test.describe('Accordion', () => {
  test('should expand and collapse sections', async ({ page }) => {
    await page.goto('/faq');

    const section = page.getByRole('button', { name: 'How do I reset my password?' });
    await section.click();
    await expect(page.getByText('Go to Settings > Security')).toBeVisible();

    await section.click();
    await expect(page.getByText('Go to Settings > Security')).not.toBeVisible();
  });
});
```

**Key assertions:** Active tab state, panel content changes, keyboard navigation works.
**Gotcha:** Use ARIA roles (`tab`, `tabpanel`) for selection -- components should follow WAI-ARIA tab pattern.

---

## 2. Visual Regression

### Screenshot Comparison Setup

**When to use:** Catch unintended UI regressions across releases.

```typescript
import { test, expect } from '@playwright/test';

test.describe('Visual regression', () => {
  test('should match homepage screenshot', async ({ page }) => {
    await page.goto('/');
    // Wait for all images and fonts to load
    await page.waitForLoadState('networkidle');

    await expect(page).toHaveScreenshot('homepage.png', {
      maxDiffPixelRatio: 0.01,
    });
  });

  test('should match component in specific state', async ({ page }) => {
    await page.goto('/components');
    await page.getByRole('button', { name: 'Toggle dark mode' }).click();

    await expect(page.getByTestId('hero-section')).toHaveScreenshot('hero-dark.png');
  });

  test('should match full page with scroll', async ({ page }) => {
    await page.goto('/long-page');
    await expect(page).toHaveScreenshot('long-page-full.png', {
      fullPage: true,
    });
  });
});
```

**Key assertions:** Screenshot matches baseline within threshold.
**Gotcha:** Always use `networkidle` or specific load waits before screenshots -- in-progress animations cause flaky diffs. Set meaningful screenshot names for easy debugging.

### Viewport Matrix Testing

**When to use:** Verify responsive design across multiple viewport sizes.

```typescript
const viewports = [
  { name: 'mobile', width: 375, height: 667 },
  { name: 'tablet', width: 768, height: 1024 },
  { name: 'desktop', width: 1440, height: 900 },
];

for (const vp of viewports) {
  test(`should render correctly on ${vp.name}`, async ({ browser }) => {
    const context = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
    });
    const page = await context.newPage();
    await page.goto('/');
    await page.waitForLoadState('networkidle');

    await expect(page).toHaveScreenshot(`homepage-${vp.name}.png`);
    await context.close();
  });
}

// Alternative: use Playwright projects for device testing
// In playwright.config.ts:
// projects: [
//   { name: 'mobile', use: { ...devices['iPhone 13'] } },
//   { name: 'tablet', use: { ...devices['iPad (gen 7)'] } },
//   { name: 'desktop', use: { ...devices['Desktop Chrome'] } },
// ]
```

**Key assertions:** Each viewport matches its baseline screenshot.
**Gotcha:** Prefer Playwright `projects` with `devices` in config for standard viewport testing -- loop pattern is for custom sizes only.

### Threshold Configuration

**When to use:** Fine-tune visual comparison sensitivity.

```typescript
// Strict comparison (pixel-perfect)
await expect(page).toHaveScreenshot('precise.png', {
  maxDiffPixelRatio: 0,
});

// Lenient comparison (allows minor anti-aliasing diffs)
await expect(page).toHaveScreenshot('lenient.png', {
  maxDiffPixelRatio: 0.02,  // 2% pixel difference allowed
});

// Absolute pixel count threshold
await expect(page).toHaveScreenshot('absolute.png', {
  maxDiffPixels: 100,  // allow up to 100 different pixels
});

// Mask dynamic content (timestamps, avatars)
await expect(page).toHaveScreenshot('masked.png', {
  mask: [
    page.getByTestId('timestamp'),
    page.getByTestId('user-avatar'),
  ],
});

// Global config in playwright.config.ts
// expect: {
//   toHaveScreenshot: { maxDiffPixelRatio: 0.01 },
// },
```

**Key assertions:** Screenshot matches within configured threshold.
**Gotcha:** Mask dynamic content (dates, avatars, ads) to prevent false failures. Use `maxDiffPixelRatio` for responsive layouts, `maxDiffPixels` for fixed-size components.

---

## 3. Accessibility

### axe-core Integration

**When to use:** Automated accessibility compliance checking.

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility', () => {
  test('should have no a11y violations on homepage', async ({ page }) => {
    await page.goto('/');
    const results = await new AxeBuilder({ page }).analyze();

    expect(results.violations).toEqual([]);
  });

  test('should have no a11y violations on login page', async ({ page }) => {
    await page.goto('/login');
    const results = await new AxeBuilder({ page })
      .include('#login-form')  // Scan specific section
      .analyze();

    expect(results.violations).toEqual([]);
  });

  test('should pass WCAG 2.1 AA standards', async ({ page }) => {
    await page.goto('/');
    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21aa'])
      .analyze();

    expect(results.violations).toEqual([]);
  });

  test('should have no violations after dynamic content loads', async ({ page }) => {
    await page.goto('/dashboard');
    await page.getByRole('tab', { name: 'Reports' }).click();
    await expect(page.getByRole('tabpanel')).toBeVisible();

    const results = await new AxeBuilder({ page }).analyze();
    expect(results.violations).toEqual([]);
  });
});
```

**Key assertions:** Zero violations array, specific WCAG tag compliance.
**Gotcha:** Run axe after all dynamic content has loaded -- scan after user interactions that change DOM. Install via `npm i -D @axe-core/playwright`.

### Keyboard Navigation

**When to use:** Verify full keyboard operability for interactive elements.

```typescript
test('should navigate form with keyboard only', async ({ page }) => {
  await page.goto('/login');

  await page.keyboard.press('Tab');
  await expect(page.getByLabel('Email')).toBeFocused();

  await page.keyboard.type('user@example.com');
  await page.keyboard.press('Tab');
  await expect(page.getByLabel('Password')).toBeFocused();

  await page.keyboard.type('password123');
  await page.keyboard.press('Tab');
  await expect(page.getByRole('button', { name: 'Sign in' })).toBeFocused();

  await page.keyboard.press('Enter');
  await expect(page).toHaveURL('/dashboard');
});

test('should navigate menu with arrow keys', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Menu' }).click();

  await page.keyboard.press('ArrowDown');
  await expect(page.getByRole('menuitem', { name: 'Profile' })).toBeFocused();

  await page.keyboard.press('ArrowDown');
  await expect(page.getByRole('menuitem', { name: 'Settings' })).toBeFocused();

  await page.keyboard.press('Escape');
  await expect(page.getByRole('menu')).not.toBeVisible();
});
```

**Key assertions:** Focus moves in logical order, Enter activates, Escape closes, arrow keys navigate.
**Gotcha:** Test tab order matches visual order. Skip links should be the first focusable element.

### Focus Management

**When to use:** Verify focus trapping in modals, focus return after close, skip links.

```typescript
test('should trap focus inside modal', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Open dialog' }).click();
  const dialog = page.getByRole('dialog');

  // Focus should be inside the dialog
  await expect(dialog.getByRole('button', { name: 'Close' })).toBeFocused();

  // Tab through all focusable elements, focus stays in dialog
  const focusableCount = await dialog.locator('button, input, [tabindex="0"]').count();
  for (let i = 0; i < focusableCount + 1; i++) {
    await page.keyboard.press('Tab');
  }

  // Focus should wrap back to first element in dialog (not escape)
  const focusedElement = page.locator(':focus');
  await expect(dialog).toContainText(await focusedElement.textContent() ?? '');
});

test('should return focus after modal close', async ({ page }) => {
  await page.goto('/');
  const trigger = page.getByRole('button', { name: 'Open dialog' });
  await trigger.click();

  await page.getByRole('dialog').getByRole('button', { name: 'Close' }).click();
  await expect(trigger).toBeFocused(); // Focus returns to trigger
});

test('should have skip-to-content link', async ({ page }) => {
  await page.goto('/');
  await page.keyboard.press('Tab');

  const skipLink = page.getByRole('link', { name: /skip to content/i });
  await expect(skipLink).toBeFocused();
  await skipLink.click();

  const mainContent = page.getByRole('main');
  await expect(mainContent).toBeVisible();
});
```

**Key assertions:** Focus trapped in modal, focus returns to trigger on close, skip link works.
**Gotcha:** Focus trap must wrap -- pressing Tab on the last element should move focus to the first. Test with real keyboard events, not just `focus()` calls.
