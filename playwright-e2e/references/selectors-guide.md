# Playwright Selectors & Locator Guide

**Table of Contents**
- §1 Selector Priority Hierarchy
- §2 Role-Based Selectors
- §3 Label & Placeholder Selectors
- §4 Text Selectors
- §5 Test ID Selectors
- §6 CSS & XPath (Last Resort)
- §7 Locator Chaining & Filtering
- §8 List Operations
- §9 Frame & Shadow DOM
- §10 Wait Strategies
- §11 Anti-Patterns

---

## §1 Selector Priority Hierarchy

Always prefer higher-priority selectors. Lower ones are fragile and break on refactors.

| Priority | Method | Resilience | When to Use |
|----------|--------|------------|-------------|
| 1 (best) | `getByRole()` | Very high | Buttons, links, headings, inputs with accessible names |
| 2 | `getByLabel()` | High | Form fields with `<label>` |
| 3 | `getByPlaceholder()` | Medium-high | Inputs with placeholder text |
| 4 | `getByText()` | Medium | Static text content, non-interactive elements |
| 5 | `getByTestId()` | Medium | Dynamic content, no stable accessible name |
| 6 | `locator('css')` | Low | Complex structural queries, nth-child |
| 7 | `locator('xpath=...')` | Very low | Legacy, cross-shadow-DOM edge cases only |

---

## §2 Role-Based Selectors

The most resilient selector strategy. Maps to ARIA roles.

```typescript
// Buttons
page.getByRole('button', { name: 'Submit' })
page.getByRole('button', { name: /submit/i })  // regex, case-insensitive

// Links
page.getByRole('link', { name: 'Home' })

// Headings
page.getByRole('heading', { name: 'Dashboard', level: 1 })

// Form inputs (via associated label)
page.getByRole('textbox', { name: 'Email' })
page.getByRole('checkbox', { name: 'Remember me' })
page.getByRole('combobox', { name: 'Country' })
page.getByRole('spinbutton', { name: 'Quantity' })

// Navigation & regions
page.getByRole('navigation')
page.getByRole('main')
page.getByRole('banner')

// Tables
page.getByRole('row', { name: /john doe/i })
page.getByRole('cell', { name: '42' })

// Dialogs
page.getByRole('dialog', { name: 'Confirm deletion' })

// Tabs
page.getByRole('tab', { name: 'Settings' })
page.getByRole('tabpanel')
```

**Key options:**
- `name`: accessible name (string or regex)
- `exact`: `true` for exact match (default: false)
- `pressed`, `checked`, `selected`, `expanded`, `disabled`: state filters
- `level`: heading level (1-6)
- `includeHidden`: include `aria-hidden` elements

```typescript
// State-filtered examples
page.getByRole('checkbox', { name: 'Terms', checked: true })
page.getByRole('button', { name: 'Menu', expanded: false })
page.getByRole('tab', { name: 'Active', selected: true })
```

---

## §3 Label & Placeholder Selectors

```typescript
// Label association (for, aria-labelledby, wrapping <label>)
page.getByLabel('Email address')
page.getByLabel(/email/i)

// Placeholder text
page.getByPlaceholder('Search...')
page.getByPlaceholder(/enter your/i)
```

---

## §4 Text Selectors

```typescript
// Exact substring match (default)
page.getByText('Welcome back')

// Regex match
page.getByText(/total: \$[\d.]+/i)

// Exact full match
page.getByText('Submit', { exact: true })

// Alt text for images
page.getByAltText('Company logo')

// Title attribute
page.getByTitle('Close dialog')
```

**Gotcha:** `getByText` matches substrings by default. Use `{ exact: true }` or regex with `^...$` anchors for precise matching.

---

## §5 Test ID Selectors

For dynamic content where no stable accessible name exists.

**Setup (playwright.config.ts):**
```typescript
export default defineConfig({
  use: {
    testIdAttribute: 'data-testid',  // default
    // testIdAttribute: 'data-cy',   // Cypress migration
  },
});
```

**Usage:**
```typescript
page.getByTestId('user-avatar')
page.getByTestId(/^product-card-/)  // regex for dynamic IDs

// In component HTML
// <div data-testid="user-avatar">...</div>
```

**When to use test IDs:**
- Generated/dynamic content (lists, tables with dynamic data)
- Third-party components without accessible roles
- Complex interactive widgets (drag handles, canvas regions)
- Migration from Cypress/Selenium (temporary, refactor to roles later)

---

## §6 CSS & XPath (Last Resort)

```typescript
// CSS selectors
page.locator('.card >> .title')          // descendant
page.locator('div.card:has-text("Pro")')  // :has-text pseudo
page.locator('input[type="email"]')       // attribute
page.locator(':nth-match(button, 3)')     // nth match

// XPath (avoid if possible)
page.locator('xpath=//div[@class="item"]//span')
```

**Only use when:**
- No accessible role/label exists AND adding data-testid is not possible
- Complex structural queries (sibling relationships, nth-child)
- Third-party widget internals

---

## §7 Locator Chaining & Filtering

```typescript
// Chain: narrow scope step by step
const card = page.locator('.product-card')
const buyButton = card.getByRole('button', { name: 'Buy' })

// Filter by text
page.getByRole('listitem').filter({ hasText: 'Premium' })

// Filter by child locator
page.getByRole('listitem').filter({
  has: page.getByRole('button', { name: 'Edit' })
})

// Filter by NOT having
page.getByRole('listitem').filter({
  hasNot: page.getByText('Archived')
})

// Chain with .and() — intersection
const saveBtn = page.getByRole('button', { name: 'Save' })
const primary = page.locator('.btn-primary')
const primarySave = saveBtn.and(primary)

// Chain with .or() — union (first match)
const errorOrWarning = page.locator('.error').or(page.locator('.warning'))
```

---

## §8 List Operations

```typescript
const items = page.getByRole('listitem')

// Count
await expect(items).toHaveCount(5)

// Specific index (0-based)
await items.nth(0).click()
await items.first().click()
await items.last().click()

// Iterate all
for (const item of await items.all()) {
  await expect(item).toBeVisible()
}

// Map to text
const texts = await items.allTextContents()
```

---

## §9 Frame & Shadow DOM

**iframes:**
```typescript
// By name or URL
const frame = page.frameLocator('iframe[name="editor"]')
frame.getByRole('button', { name: 'Bold' })

// Nested frames
page.frameLocator('#outer').frameLocator('#inner').getByText('Hello')
```

**Shadow DOM:**
```typescript
// Playwright pierces open shadow DOM automatically
page.locator('my-component').getByRole('button', { name: 'Click' })

// Explicit pierce (if needed)
page.locator('my-component >> shadow=.inner-button')
```

---

## §10 Wait Strategies

Playwright auto-waits for elements before actions. Explicit waits are rarely needed.

**Auto-waiting (built-in):**
- `click()` — waits for visible, stable, enabled, no overlays
- `fill()` — waits for visible, enabled, editable
- `expect()` — retries assertion until timeout

**When explicit waits ARE needed:**
```typescript
// Wait for element state
await page.getByRole('button', { name: 'Submit' }).waitFor({ state: 'visible' })
await page.getByTestId('spinner').waitFor({ state: 'hidden' })
await page.getByTestId('deleted-item').waitFor({ state: 'detached' })

// Wait for network
await page.waitForResponse(resp =>
  resp.url().includes('/api/data') && resp.status() === 200
)

// Wait for URL navigation
await page.waitForURL('**/dashboard')

// Wait for load state
await page.waitForLoadState('networkidle')  // use sparingly

// Wait for function
await page.waitForFunction(() => document.title.includes('Ready'))
```

**Assertion retry (preferred over explicit waits):**
```typescript
// These auto-retry until timeout (default 5s)
await expect(page.getByRole('alert')).toBeVisible()
await expect(page.getByText('Saved')).toBeAttached()
await expect(page.getByRole('table')).toContainText('John')
await expect(page).toHaveURL(/dashboard/)
await expect(page).toHaveTitle(/Home/)
```

---

## §11 Anti-Patterns

| ❌ Anti-Pattern | ✅ Correct Approach |
|----------------|-------------------|
| `page.locator('#btn-7f3a2')` — auto-generated IDs | `page.getByRole('button', { name: 'Submit' })` |
| `page.locator('.MuiButton-root.css-1a2b3c')` — framework classes | `page.getByRole('button', { name: 'Save' })` |
| `page.locator('div > div:nth-child(3) > span')` — structural path | `page.getByText('Expected text')` or `getByTestId` |
| `await page.waitForTimeout(2000)` — hard sleep | `await expect(locator).toBeVisible()` — auto-retry |
| `page.locator('text=Click here')` — old syntax | `page.getByText('Click here')` — recommended API |
| `page.$('selector')` — ElementHandle API | `page.locator('selector')` — Locator API |
| `page.locator('.btn').first()` on dynamic lists | `page.getByRole('button', { name: 'specific' })` |
| `if (await el.isVisible()) { ... }` — race condition | `await expect(el).toBeVisible()` or `.toBeHidden()` |
| `page.locator('[data-testid="x"]')` — raw CSS | `page.getByTestId('x')` — semantic API |
| Multiple `waitForTimeout` between steps | Single `expect` assertion with auto-retry |
