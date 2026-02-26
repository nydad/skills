---
name: playwright-e2e
description: |
  Generates Playwright E2E test suites by analyzing application structure, routes, and components.
  Use when adding E2E tests, setting up visual regression, creating page objects, or building test infrastructure for web apps.
  Adaptive test generation based on app framework (React, Next.js, Vue, etc.) and testing requirements.

  Triggers: playwright, e2e test, end-to-end, visual regression, integration test, E2E 테스트, 플레이라이트
---

# Playwright E2E -- Adaptive Test Suite Generator

Generate comprehensive Playwright E2E test suites by analyzing application structure, routes, and components. Produces page objects, fixtures, visual regression tests, accessibility checks, and full configuration -- adapted to the specific framework and testing needs.

## When to Use

- Generating E2E test suites for web applications
- Creating page object models for complex UIs
- Setting up visual regression testing with screenshot comparisons
- Adding accessibility (a11y) testing with axe-core integration
- Building test infrastructure: fixtures, helpers, configuration
- Any request mentioning: playwright, e2e, end-to-end, visual regression, integration test

## Generation Workflow (3 Phases)

> **You are an adaptive testing agent.** Every test suite should be uniquely shaped by the application's architecture, routes, components, and risk profile. Test count, pattern selection, assertion depth, and coverage strategy must all adapt to context -- never produce cookie-cutter tests.

### Phase 1: App Analysis (understand before generating)

1. **Scan the project** to detect framework, router, and key dependencies:
   - Package.json: framework (React, Next.js, Vue, Angular, Svelte), test deps
   - Directory structure: pages/, routes/, components/, layouts/
   - Existing tests: check for test/ or __tests__/ directories, existing Playwright config
2. **Map routes and pages**: identify all navigable URLs and their components
3. **Identify critical user flows**: auth, checkout, forms, search, CRUD operations
4. **Detect API layer**: REST endpoints, GraphQL queries, tRPC routes for mocking
5. **Check existing test coverage**: avoid duplicating what already exists

### Phase 1 Output Format

Before generating tests, output this analysis table:

| Route/Page | Components | Risk Level | Test Types |
|------------|-----------|------------|------------|
| /login | LoginForm, OAuthButton | High | auth, a11y, visual |
| /dashboard | DataTable, Charts | Medium | data display, a11y |
| /settings | SettingsForm, FileUpload | Medium | form, validation |
| /checkout | Cart, PaymentForm | Critical | multi-step, e2e flow |

*(Adapt rows to actual application routes.)*

### Phase 2: Test Strategy

1. **Prioritize by risk**: Critical flows first (auth, payments, data mutation)
2. **Select test types** per route using the decision matrix below
3. **Plan page objects**: one POM per major page/component group
4. **Design fixtures**: shared auth states, test data, API mocks
5. **Determine visual regression scope**: which pages need screenshot baselines

### Phase 3: Code Generation

1. Generate `playwright.config.ts` adapted to the framework
2. Create page objects in `tests/pages/` or `e2e/pages/`
3. Generate test files organized by feature or route
4. Create shared fixtures in `tests/fixtures/`
5. Add helper utilities as needed (test data factories, custom matchers)

## Test Type Decision Matrix

| App Feature | Test Pattern | Priority |
|------------|-------------|----------|
| Auth flows (login/logout/signup) | Multi-step sequence with session validation | Critical |
| Forms with validation | Input validation + submission + error states | High |
| Navigation and routing | Route transitions + deep linking + back/forward | Medium |
| Data tables and lists | API mock + pagination + sorting + filtering | Medium |
| Interactive components (modals, dropdowns) | User interaction + state verification | Medium |
| File upload | File chooser API + progress + validation | Medium |
| Search | Debounce + results + empty state + error state | Medium |
| Visual consistency | Screenshot comparison across viewports | Low-Medium |
| Accessibility | axe-core scan + keyboard nav + focus management | High |
| Performance | Web vitals measurement + resource timing | Low |

## Framework Detection and Adaptation

| Framework | Router | Dev Server | Base URL | Special Config |
|-----------|--------|-----------|----------|---------------|
| Next.js | App Router / Pages | `next dev` | `http://localhost:3000` | `webServer` in config |
| React + Vite | React Router | `vite dev` | `http://localhost:5173` | `webServer` in config |
| Vue | Vue Router | `vite dev` | `http://localhost:5173` | `webServer` in config |
| Angular | Angular Router | `ng serve` | `http://localhost:4200` | `webServer` in config |
| Svelte | SvelteKit | `vite dev` | `http://localhost:5173` | `webServer` in config |
| Generic / Static | N/A | varies | varies | Manual baseURL |

## Page Object Pattern

Generate page objects when a page has **3+ interactive elements** or is tested by **2+ test files**.

```typescript
// tests/pages/login.page.ts
import { type Locator, type Page } from '@playwright/test';

export class LoginPage {
  readonly page: Page;
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly submitButton: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.emailInput = page.getByLabel('Email');
    this.passwordInput = page.getByLabel('Password');
    this.submitButton = page.getByRole('button', { name: 'Sign in' });
    this.errorMessage = page.getByRole('alert');
  }

  async goto() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }
}
```

**POM rules:**
- Locators use semantic selectors (getByRole, getByLabel) -- never raw CSS
- Methods encapsulate user actions, not implementation details
- No assertions inside page objects -- assertions belong in test files
- Constructor accepts `Page`, stores all locators as readonly properties

## Test Structure Quick Reference

```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from './pages/login.page';

test.describe('Login flow', () => {
  let loginPage: LoginPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    await loginPage.goto();
  });

  test('should login with valid credentials', async ({ page }) => {
    await loginPage.login('user@example.com', 'password123');
    await expect(page).toHaveURL('/dashboard');
  });

  test('should show error for invalid credentials', async ({ page }) => {
    await loginPage.login('user@example.com', 'wrong');
    await expect(loginPage.errorMessage).toBeVisible();
    await expect(loginPage.errorMessage).toContainText('Invalid');
  });
});
```

**Naming conventions:**
- Test files: `{feature}.spec.ts`
- Page objects: `{page}.page.ts`
- Fixtures: `{name}.fixture.ts`
- Describe blocks: noun phrase (feature area)
- Test names: `should {expected behavior}` or `{action} → {result}`

## Selector Priority

Use selectors in this priority order (details in `references/selectors-guide.md`):

1. **`getByRole`** -- buttons, links, headings, form controls (best)
2. **`getByLabel`** -- form inputs with associated labels
3. **`getByPlaceholder`** -- inputs with placeholder text
4. **`getByText`** -- visible text content
5. **`getByTestId`** -- data-testid attributes (when semantic selectors fail)
6. **CSS selector** -- last resort only

## API Mocking Patterns

```typescript
// Mock a successful API response
await page.route('**/api/users', (route) =>
  route.fulfill({
    status: 200,
    contentType: 'application/json',
    body: JSON.stringify({ users: [{ id: 1, name: 'Test User' }] }),
  })
);

// Mock an error response
await page.route('**/api/users', (route) =>
  route.fulfill({ status: 500, body: 'Internal Server Error' })
);

// Abort network requests (e.g., analytics)
await page.route('**/analytics/**', (route) => route.abort());

// Intercept and modify requests
await page.route('**/api/data', async (route) => {
  const response = await route.fetch();
  const json = await response.json();
  json.modified = true;
  await route.fulfill({ response, json });
});
```

## Configuration Template

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ['html'],
    ...(process.env.CI ? [['github' as const]] : []),
  ],
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit', use: { ...devices['Desktop Safari'] } },
    { name: 'mobile-chrome', use: { ...devices['Pixel 5'] } },
  ],
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
});
```

## Validation Checklist

**After generating, copy this checklist and verify each item:**

```
[ ] playwright.config.ts uses defineConfig with proper project setup
[ ] All selectors use semantic queries (getByRole/getByLabel) -- no raw CSS for interactive elements
[ ] Page objects contain no assertions -- only locators and action methods
[ ] Test names follow "should {behavior}" convention
[ ] beforeEach handles page navigation and setup
[ ] API mocks use route.fulfill with proper content types
[ ] No hardcoded waits (setTimeout, page.waitForTimeout) -- use auto-waiting or explicit waitFor
[ ] Visual tests specify viewport and have meaningful screenshot names
[ ] Accessibility tests import @axe-core/playwright and check violations
[ ] Test data is isolated -- no shared mutable state between tests
[ ] Fixtures use proper Playwright fixture extension pattern
[ ] Config includes webServer for local dev server startup
```

## Common Mistakes

| | Pattern | Fix |
|---|---------|-----|
| ❌ | `page.locator('#submit-btn')` -- raw CSS selectors | ✅ `page.getByRole('button', { name: 'Submit' })` -- semantic selector |
| ❌ | `await page.waitForTimeout(3000)` -- hardcoded waits | ✅ `await expect(element).toBeVisible()` -- auto-waiting assertion |
| ❌ | Assertions inside page objects | ✅ Page objects return locators/data; tests make assertions |
| ❌ | `test('test 1', ...)` -- vague test names | ✅ `test('should display error when email is invalid', ...)` |
| ❌ | Shared mutable state across tests | ✅ Each test gets fresh page via beforeEach, isolated test data |
| ❌ | `page.click('.btn')` -- legacy action API | ✅ `page.getByRole('button').click()` -- locator-based API |
| ❌ | `expect(await el.textContent()).toBe('x')` -- manual text extraction | ✅ `await expect(el).toHaveText('x')` -- web-first assertion |

## Reference Loading Guide

**Always read first:**
- This SKILL.md -- core workflow, decision matrix, and patterns

**Load for test pattern recipes:**
- `references/test-patterns.md` -- Detailed patterns for auth, forms, visual, a11y, and more

**Load for selector strategy details:**
- `references/selectors-guide.md` -- Complete selector hierarchy, wait strategies, anti-patterns

## References

- `references/test-patterns.md` -- Common E2E test patterns organized by scenario with code snippets
- `references/selectors-guide.md` -- Selector strategies, wait patterns, locator chaining, anti-patterns
