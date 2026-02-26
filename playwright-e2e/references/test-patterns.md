# Test Patterns Reference

Common E2E test patterns organized by scenario. Each pattern includes when to use, TypeScript code, key assertions, and common gotchas.

## Table of Contents

1. [Authentication](#1-authentication)
2. [Forms and Validation](#2-forms-and-validation)
3. [Navigation and Routing](#3-navigation-and-routing)
4. [Data Display](#4-data-display)
5. [Interactive Components](#5-interactive-components)
6. [Visual Regression](#6-visual-regression)
7. [Accessibility](#7-accessibility)
8. [API Integration](#8-api-integration)
9. [Performance](#9-performance)

---

## 1. Authentication

### Login Flow

**When to use:** Every app with user authentication.

```typescript
test.describe('Login', () => {
  test('should login with valid credentials', async ({ page }) => {
    await page.goto('/login');
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('securePass123');
    await page.getByRole('button', { name: 'Sign in' }).click();

    await expect(page).toHaveURL('/dashboard');
    await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
  });

  test('should show error for invalid credentials', async ({ page }) => {
    await page.goto('/login');
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('wrongpassword');
    await page.getByRole('button', { name: 'Sign in' }).click();

    await expect(page.getByRole('alert')).toContainText('Invalid email or password');
    await expect(page).toHaveURL('/login');
  });

  test('should validate required fields', async ({ page }) => {
    await page.goto('/login');
    await page.getByRole('button', { name: 'Sign in' }).click();

    await expect(page.getByText('Email is required')).toBeVisible();
    await expect(page.getByText('Password is required')).toBeVisible();
  });
});
```

**Key assertions:** URL change after login, dashboard content visible, error messages for failures.
**Gotcha:** Always wait for navigation to complete via `toHaveURL` -- never use `waitForTimeout`.

### Logout Flow

**When to use:** Verify session cleanup and redirect after logout.

```typescript
test('should logout and redirect to login', async ({ page }) => {
  // Assume already authenticated via storageState fixture
  await page.goto('/dashboard');
  await page.getByRole('button', { name: 'User menu' }).click();
  await page.getByRole('menuitem', { name: 'Logout' }).click();

  await expect(page).toHaveURL('/login');
  // Verify protected route redirects after logout
  await page.goto('/dashboard');
  await expect(page).toHaveURL('/login');
});
```

**Key assertions:** Redirect to login page, protected routes no longer accessible.
**Gotcha:** Use `storageState` fixture for authenticated state -- don't repeat login in every test.

### Session Persistence

**When to use:** Verify auth tokens survive page reload.

```typescript
test('should persist session across page reload', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Email').fill('user@example.com');
  await page.getByLabel('Password').fill('securePass123');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await expect(page).toHaveURL('/dashboard');

  await page.reload();
  await expect(page).toHaveURL('/dashboard');
  await expect(page.getByText('Welcome')).toBeVisible();
});

// Reusable auth fixture using storageState
// tests/fixtures/auth.fixture.ts
import { test as base } from '@playwright/test';

export const test = base.extend({
  storageState: async ({ browser }, use) => {
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto('/login');
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('securePass123');
    await page.getByRole('button', { name: 'Sign in' }).click();
    await page.waitForURL('/dashboard');
    const storage = await context.storageState();
    await context.close();
    await use(storage);
  },
});
```

**Key assertions:** Page remains on dashboard after reload, user content still visible.
**Gotcha:** Store `storageState` to a file in global setup for performance -- avoid re-login per test.

### OAuth / Social Login

**When to use:** Apps with third-party OAuth (Google, GitHub, etc.).

```typescript
test('should handle OAuth login flow', async ({ page }) => {
  // Option 1: Mock the OAuth callback (recommended for E2E)
  await page.route('**/auth/callback*', (route) =>
    route.fulfill({
      status: 302,
      headers: { Location: '/dashboard' },
    })
  );

  // Option 2: Intercept the OAuth redirect and set tokens directly
  await page.goto('/login');
  await page.getByRole('button', { name: 'Sign in with Google' }).click();

  // For real OAuth testing, use API to create session:
  await page.evaluate(() => {
    localStorage.setItem('auth_token', 'test-oauth-token');
  });
  await page.goto('/dashboard');
  await expect(page).toHaveURL('/dashboard');
});
```

**Key assertions:** OAuth button redirects correctly, callback sets session, dashboard accessible.
**Gotcha:** Never test against real OAuth providers in CI -- mock the callback endpoint. Use API-level setup for auth tokens.

---

## 2. Forms and Validation

### Input Validation

**When to use:** Any form with client-side or server-side validation.

```typescript
test.describe('Form validation', () => {
  test('should show inline errors for invalid inputs', async ({ page }) => {
    await page.goto('/register');
    const emailInput = page.getByLabel('Email');

    await emailInput.fill('not-an-email');
    await emailInput.blur();
    await expect(page.getByText('Please enter a valid email')).toBeVisible();

    await emailInput.fill('valid@email.com');
    await expect(page.getByText('Please enter a valid email')).not.toBeVisible();
  });

  test('should enforce password requirements', async ({ page }) => {
    await page.goto('/register');
    await page.getByLabel('Password').fill('short');
    await page.getByLabel('Password').blur();

    await expect(page.getByText('at least 8 characters')).toBeVisible();
  });

  test('should submit form with valid data', async ({ page }) => {
    await page.goto('/register');
    await page.getByLabel('Name').fill('Test User');
    await page.getByLabel('Email').fill('test@example.com');
    await page.getByLabel('Password').fill('SecurePass123!');
    await page.getByLabel('Confirm Password').fill('SecurePass123!');
    await page.getByRole('button', { name: 'Register' }).click();

    await expect(page).toHaveURL('/welcome');
  });
});
```

**Key assertions:** Inline error visibility, error clearance on valid input, successful submission redirect.
**Gotcha:** Use `blur()` to trigger validation on fields that validate on blur, not on change.

### Multi-Step Wizard

**When to use:** Multi-page or multi-step form flows (checkout, onboarding).

```typescript
test('should complete multi-step checkout', async ({ page }) => {
  await page.goto('/checkout');

  // Step 1: Shipping
  await expect(page.getByText('Step 1 of 3')).toBeVisible();
  await page.getByLabel('Address').fill('123 Main St');
  await page.getByLabel('City').fill('Portland');
  await page.getByRole('button', { name: 'Continue' }).click();

  // Step 2: Payment
  await expect(page.getByText('Step 2 of 3')).toBeVisible();
  await page.getByLabel('Card number').fill('4242424242424242');
  await page.getByLabel('Expiry').fill('12/28');
  await page.getByLabel('CVC').fill('123');
  await page.getByRole('button', { name: 'Continue' }).click();

  // Step 3: Review
  await expect(page.getByText('Step 3 of 3')).toBeVisible();
  await expect(page.getByText('123 Main St')).toBeVisible();
  await page.getByRole('button', { name: 'Place order' }).click();

  await expect(page.getByRole('heading', { name: 'Order confirmed' })).toBeVisible();
});

test('should preserve data when navigating back', async ({ page }) => {
  await page.goto('/checkout');
  await page.getByLabel('Address').fill('123 Main St');
  await page.getByRole('button', { name: 'Continue' }).click();
  await page.getByRole('button', { name: 'Back' }).click();

  await expect(page.getByLabel('Address')).toHaveValue('123 Main St');
});
```

**Key assertions:** Step indicator updates, data preserved on back navigation, final confirmation.
**Gotcha:** Always verify data persistence across steps -- many wizard bugs involve lost state.

### File Upload

**When to use:** File upload inputs, drag-and-drop upload zones.

```typescript
test('should upload a file', async ({ page }) => {
  await page.goto('/upload');

  const fileInput = page.locator('input[type="file"]');
  await fileInput.setInputFiles({
    name: 'test-document.pdf',
    mimeType: 'application/pdf',
    buffer: Buffer.from('fake pdf content'),
  });

  await expect(page.getByText('test-document.pdf')).toBeVisible();
  await page.getByRole('button', { name: 'Upload' }).click();
  await expect(page.getByText('Upload successful')).toBeVisible();
});

test('should reject files exceeding size limit', async ({ page }) => {
  await page.goto('/upload');
  const largeBuffer = Buffer.alloc(10 * 1024 * 1024); // 10MB
  const fileInput = page.locator('input[type="file"]');
  await fileInput.setInputFiles({
    name: 'large-file.pdf',
    mimeType: 'application/pdf',
    buffer: largeBuffer,
  });

  await expect(page.getByText('File size exceeds limit')).toBeVisible();
});

test('should handle multiple file upload', async ({ page }) => {
  await page.goto('/upload');
  const fileInput = page.locator('input[type="file"]');
  await fileInput.setInputFiles([
    { name: 'file1.png', mimeType: 'image/png', buffer: Buffer.from('img1') },
    { name: 'file2.png', mimeType: 'image/png', buffer: Buffer.from('img2') },
  ]);

  await expect(page.getByText('file1.png')).toBeVisible();
  await expect(page.getByText('file2.png')).toBeVisible();
});
```

**Key assertions:** File name displayed, upload success/error messages, file type/size validation.
**Gotcha:** Use `setInputFiles` with buffer for synthetic files -- no need for real files on disk.

### Dynamic Forms

**When to use:** Forms that add/remove fields dynamically (repeatable sections, conditional fields).

```typescript
test('should add and remove dynamic form fields', async ({ page }) => {
  await page.goto('/survey-builder');

  // Add a new question field
  await page.getByRole('button', { name: 'Add question' }).click();
  const questions = page.getByRole('textbox', { name: /Question/ });
  await expect(questions).toHaveCount(2); // 1 default + 1 added

  await questions.nth(1).fill('What is your role?');

  // Remove the first question
  await page.getByRole('button', { name: 'Remove' }).first().click();
  await expect(page.getByRole('textbox', { name: /Question/ })).toHaveCount(1);
  await expect(page.getByRole('textbox', { name: /Question/ })).toHaveValue('What is your role?');
});

test('should show conditional fields based on selection', async ({ page }) => {
  await page.goto('/form');
  await page.getByLabel('Has children').check();

  await expect(page.getByLabel('Number of children')).toBeVisible();
  await page.getByLabel('Has children').uncheck();
  await expect(page.getByLabel('Number of children')).not.toBeVisible();
});
```

**Key assertions:** Field count changes, values preserved after reorder, conditional fields toggle.
**Gotcha:** Use `toHaveCount` to verify dynamic element quantity -- avoid index-based checks that break on reorder.

---

## 3. Navigation and Routing

### Route Transitions

**When to use:** Verify SPA navigation, link behavior, and route rendering.

```typescript
test.describe('Navigation', () => {
  test('should navigate between pages via navbar', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('link', { name: 'About' }).click();
    await expect(page).toHaveURL('/about');
    await expect(page.getByRole('heading', { name: 'About Us' })).toBeVisible();
  });

  test('should highlight active nav item', async ({ page }) => {
    await page.goto('/about');
    const aboutLink = page.getByRole('link', { name: 'About' });
    await expect(aboutLink).toHaveAttribute('aria-current', 'page');
  });

  test('should render 404 for unknown routes', async ({ page }) => {
    await page.goto('/non-existent-page');
    await expect(page.getByText('Page not found')).toBeVisible();
  });
});
```

**Key assertions:** URL change, heading/content rendered, active state on nav, 404 handling.
**Gotcha:** SPA navigation doesn't trigger full page load -- use `toHaveURL` not `waitForNavigation`.

### Deep Linking and URL State

**When to use:** Apps that store state in URL params (filters, pagination, tabs).

```typescript
test('should restore state from URL parameters', async ({ page }) => {
  // Navigate directly to a filtered view
  await page.goto('/products?category=electronics&sort=price-asc');

  await expect(page.getByRole('combobox', { name: 'Category' })).toHaveValue('electronics');
  await expect(page.getByRole('combobox', { name: 'Sort' })).toHaveValue('price-asc');
  await expect(page.getByTestId('product-card')).toHaveCount(10);
});

test('should update URL when filters change', async ({ page }) => {
  await page.goto('/products');
  await page.getByRole('combobox', { name: 'Category' }).selectOption('electronics');

  await expect(page).toHaveURL(/category=electronics/);
});
```

**Key assertions:** UI state matches URL params, URL updates on interaction.
**Gotcha:** Use regex with `toHaveURL` for partial URL matching when query param order may vary.

### Back/Forward Navigation

**When to use:** Verify browser back/forward behavior in SPAs.

```typescript
test('should handle browser back/forward', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('link', { name: 'Products' }).click();
  await expect(page).toHaveURL('/products');

  await page.getByRole('link', { name: 'About' }).click();
  await expect(page).toHaveURL('/about');

  await page.goBack();
  await expect(page).toHaveURL('/products');

  await page.goForward();
  await expect(page).toHaveURL('/about');
});
```

**Key assertions:** URL and content update correctly on back/forward.
**Gotcha:** Ensure `goBack()` works with client-side routing -- some SPA routers need `popstate` handling.

---

## 4. Data Display

### Tables with Pagination, Sorting, Filtering

**When to use:** Data grids with pagination, sorting, and filtering.

```typescript
test.describe('Data table', () => {
  test.beforeEach(async ({ page }) => {
    await page.route('**/api/users*', (route) => {
      const url = new URL(route.request().url());
      const page_num = Number(url.searchParams.get('page') ?? 1);
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          data: Array.from({ length: 10 }, (_, i) => ({
            id: (page_num - 1) * 10 + i + 1,
            name: `User ${(page_num - 1) * 10 + i + 1}`,
            email: `user${(page_num - 1) * 10 + i + 1}@test.com`,
          })),
          total: 50,
        }),
      });
    });
  });

  test('should display paginated data', async ({ page }) => {
    await page.goto('/users');
    await expect(page.getByRole('row')).toHaveCount(11); // 10 rows + header

    await page.getByRole('button', { name: 'Next page' }).click();
    await expect(page.getByText('User 11')).toBeVisible();
  });

  test('should sort by column', async ({ page }) => {
    await page.goto('/users');
    await page.getByRole('columnheader', { name: 'Name' }).click();

    const firstCell = page.getByRole('row').nth(1).getByRole('cell').first();
    await expect(firstCell).toBeVisible();
  });

  test('should filter results', async ({ page }) => {
    await page.goto('/users');
    await page.getByPlaceholder('Search users').fill('User 1');

    await expect(page.getByRole('row')).toHaveCount(2); // header + 1 match
  });
});
```

**Key assertions:** Row count matches expected data, pagination changes content, sort changes order.
**Gotcha:** Mock API with dynamic query param handling to test real pagination behavior.

### Infinite Scroll

**When to use:** Infinite scroll / virtual lists.

```typescript
test('should load more items on scroll', async ({ page }) => {
  await page.goto('/feed');
  const items = page.getByTestId('feed-item');

  // Initial load
  await expect(items).toHaveCount(20);

  // Scroll to bottom to trigger load
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));

  // Wait for new items
  await expect(items).toHaveCount(40);
});

test('should show end-of-list message', async ({ page }) => {
  // Mock API to return empty on page 2
  await page.route('**/api/feed?page=2*', (route) =>
    route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({ data: [], hasMore: false }),
    })
  );
  await page.goto('/feed');
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));

  await expect(page.getByText('No more items')).toBeVisible();
});
```

**Key assertions:** Item count increases after scroll, end-of-list indicator appears.
**Gotcha:** Use `page.evaluate` for scroll -- `mouse.wheel` may not trigger intersection observer.

### Search

**When to use:** Search functionality with debounce, results list, empty states.

```typescript
test.describe('Search', () => {
  test('should display results matching query', async ({ page }) => {
    await page.route('**/api/search*', (route) => {
      const url = new URL(route.request().url());
      const q = url.searchParams.get('q');
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          results: q ? [{ id: 1, title: `Result for "${q}"` }] : [],
        }),
      });
    });

    await page.goto('/search');
    await page.getByPlaceholder('Search...').fill('playwright');

    await expect(page.getByText('Result for "playwright"')).toBeVisible();
  });

  test('should show empty state for no results', async ({ page }) => {
    await page.route('**/api/search*', (route) =>
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ results: [] }),
      })
    );
    await page.goto('/search');
    await page.getByPlaceholder('Search...').fill('xyznonexistent');

    await expect(page.getByText('No results found')).toBeVisible();
  });

  test('should debounce search requests', async ({ page }) => {
    let requestCount = 0;
    await page.route('**/api/search*', (route) => {
      requestCount++;
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ results: [] }),
      });
    });

    await page.goto('/search');
    const input = page.getByPlaceholder('Search...');
    await input.pressSequentially('test', { delay: 50 });

    // Wait for debounce to settle
    await page.waitForTimeout(500);
    expect(requestCount).toBeLessThanOrEqual(2); // debounced, not 4 requests
  });
});
```

**Key assertions:** Results appear for valid query, empty state for no matches, debounce limits requests.
**Gotcha:** `pressSequentially` with delay simulates real typing for debounce testing. `waitForTimeout` is acceptable here to verify debounce behavior specifically.

---

## 5. Interactive Components

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

## 6. Visual Regression

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

## 7. Accessibility

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

---

## 8. API Integration

### Mock Setup and Intercept Patterns

**When to use:** Isolate frontend tests from backend dependencies.

```typescript
test.describe('API mocking', () => {
  test('should display mocked user data', async ({ page }) => {
    await page.route('**/api/users', (route) =>
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify([
          { id: 1, name: 'Alice', role: 'Admin' },
          { id: 2, name: 'Bob', role: 'User' },
        ]),
      })
    );

    await page.goto('/users');
    await expect(page.getByText('Alice')).toBeVisible();
    await expect(page.getByText('Bob')).toBeVisible();
  });

  test('should intercept and verify request payload', async ({ page }) => {
    let capturedBody: unknown;
    await page.route('**/api/users', async (route) => {
      capturedBody = route.request().postDataJSON();
      await route.fulfill({ status: 201, body: JSON.stringify({ id: 3 }) });
    });

    await page.goto('/users/new');
    await page.getByLabel('Name').fill('Charlie');
    await page.getByRole('button', { name: 'Create' }).click();

    expect(capturedBody).toEqual(expect.objectContaining({ name: 'Charlie' }));
  });

  test('should mock multiple endpoints', async ({ page }) => {
    await page.route('**/api/users', (route) =>
      route.fulfill({ status: 200, body: JSON.stringify([]) })
    );
    await page.route('**/api/stats', (route) =>
      route.fulfill({ status: 200, body: JSON.stringify({ total: 42 }) })
    );

    await page.goto('/dashboard');
    await expect(page.getByText('42')).toBeVisible();
  });
});
```

**Key assertions:** UI renders mocked data, request payloads captured correctly.
**Gotcha:** Set up routes BEFORE navigation (`page.goto`) -- routes registered after load miss initial requests.

### Error State Testing

**When to use:** Verify graceful error handling for API failures.

```typescript
test.describe('Error states', () => {
  test('should show error message on 500', async ({ page }) => {
    await page.route('**/api/users', (route) =>
      route.fulfill({ status: 500, body: 'Internal Server Error' })
    );

    await page.goto('/users');
    await expect(page.getByRole('alert')).toContainText('Something went wrong');
    await expect(page.getByRole('button', { name: 'Retry' })).toBeVisible();
  });

  test('should handle network failure', async ({ page }) => {
    await page.route('**/api/users', (route) => route.abort('failed'));

    await page.goto('/users');
    await expect(page.getByText('Network error')).toBeVisible();
  });

  test('should retry on transient error', async ({ page }) => {
    let callCount = 0;
    await page.route('**/api/data', (route) => {
      callCount++;
      if (callCount === 1) {
        return route.fulfill({ status: 503 });
      }
      return route.fulfill({
        status: 200,
        body: JSON.stringify({ value: 'success' }),
      });
    });

    await page.goto('/data');
    await page.getByRole('button', { name: 'Retry' }).click();
    await expect(page.getByText('success')).toBeVisible();
    expect(callCount).toBe(2);
  });

  test('should show 404 for missing resource', async ({ page }) => {
    await page.route('**/api/users/999', (route) =>
      route.fulfill({ status: 404, body: JSON.stringify({ message: 'Not found' }) })
    );

    await page.goto('/users/999');
    await expect(page.getByText('User not found')).toBeVisible();
  });
});
```

**Key assertions:** Error UI rendered, retry mechanism works, appropriate message per error type.
**Gotcha:** Use `route.abort('failed')` for network errors vs `route.fulfill({ status: 5xx })` for server errors -- they produce different UI behavior.

### Loading State Verification

**When to use:** Verify loading spinners, skeleton screens, progressive content.

```typescript
test('should show loading state while fetching', async ({ page }) => {
  // Delay the API response to observe loading state
  await page.route('**/api/users', async (route) => {
    await new Promise((resolve) => setTimeout(resolve, 1000));
    await route.fulfill({
      status: 200,
      body: JSON.stringify([{ id: 1, name: 'Alice' }]),
    });
  });

  await page.goto('/users');

  // Loading state should be visible immediately
  await expect(page.getByRole('progressbar')).toBeVisible();
  // Or skeleton screen:
  // await expect(page.getByTestId('skeleton')).toBeVisible();

  // After data loads, loading state disappears
  await expect(page.getByText('Alice')).toBeVisible();
  await expect(page.getByRole('progressbar')).not.toBeVisible();
});

test('should show empty state when no data', async ({ page }) => {
  await page.route('**/api/users', (route) =>
    route.fulfill({
      status: 200,
      body: JSON.stringify([]),
    })
  );

  await page.goto('/users');
  await expect(page.getByText('No users found')).toBeVisible();
  await expect(page.getByRole('link', { name: 'Add first user' })).toBeVisible();
});
```

**Key assertions:** Loading indicator visible during fetch, disappears on data arrival, empty state shown.
**Gotcha:** Delay API response in mock to reliably test loading state -- real APIs may be too fast to observe.

---

## 9. Performance

### Web Vitals Measurement

**When to use:** Measure Core Web Vitals (LCP, FID, CLS) in E2E tests.

```typescript
test('should meet Core Web Vitals thresholds', async ({ page }) => {
  await page.goto('/');

  // Measure Largest Contentful Paint (LCP)
  const lcp = await page.evaluate(() => {
    return new Promise<number>((resolve) => {
      new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const lastEntry = entries[entries.length - 1];
        resolve(lastEntry.startTime);
      }).observe({ type: 'largest-contentful-paint', buffered: true });
    });
  });
  expect(lcp).toBeLessThan(2500); // Good LCP < 2.5s

  // Measure Cumulative Layout Shift (CLS)
  const cls = await page.evaluate(() => {
    return new Promise<number>((resolve) => {
      let clsValue = 0;
      new PerformanceObserver((list) => {
        for (const entry of list.getEntries() as any[]) {
          if (!entry.hadRecentInput) clsValue += entry.value;
        }
        resolve(clsValue);
      }).observe({ type: 'layout-shift', buffered: true });
      setTimeout(() => resolve(clsValue), 3000);
    });
  });
  expect(cls).toBeLessThan(0.1); // Good CLS < 0.1

  // Measure Time to First Byte (TTFB)
  const ttfb = await page.evaluate(() => {
    const nav = performance.getEntriesByType('navigation')[0] as PerformanceNavigationTiming;
    return nav.responseStart - nav.requestStart;
  });
  expect(ttfb).toBeLessThan(800); // Good TTFB < 800ms
});
```

**Key assertions:** LCP < 2.5s, CLS < 0.1, TTFB < 800ms.
**Gotcha:** Performance tests are inherently flaky in CI -- use generous thresholds and run on consistent hardware. Consider separate performance test suite from functional tests.

### Network Throttling

**When to use:** Test app behavior under slow network conditions.

```typescript
test('should load gracefully on slow 3G', async ({ browser }) => {
  const context = await browser.newContext();
  const page = await context.newPage();

  // Simulate slow 3G
  const client = await context.newCDPSession(page);
  await client.send('Network.emulateNetworkConditions', {
    offline: false,
    downloadThroughput: (500 * 1024) / 8,  // 500 kbps
    uploadThroughput: (500 * 1024) / 8,
    latency: 400,  // 400ms RTT
  });

  await page.goto('/');

  // Should show loading state quickly
  await expect(page.getByRole('progressbar').or(page.getByTestId('skeleton'))).toBeVisible();

  // Should eventually load
  await expect(page.getByRole('heading', { name: /Welcome/ })).toBeVisible({ timeout: 30000 });

  await context.close();
});

test('should handle offline gracefully', async ({ browser }) => {
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto('/');

  // Go offline
  await context.setOffline(true);

  await page.getByRole('link', { name: 'About' }).click();
  await expect(page.getByText(/offline|no connection/i)).toBeVisible();

  // Come back online
  await context.setOffline(false);
  await page.reload();
  await expect(page.getByRole('heading', { name: 'About' })).toBeVisible();

  await context.close();
});
```

**Key assertions:** Loading states visible on slow network, content eventually loads, offline state handled.
**Gotcha:** CDP-based network throttling only works in Chromium. Use `context.setOffline()` for cross-browser offline testing.
