# Test Patterns: Auth, Forms, and Navigation

Common E2E test patterns for authentication flows, form validation, and navigation/routing. Each pattern includes when to use, TypeScript code, key assertions, and common gotchas.

## Table of Contents

1. [Authentication](#1-authentication)
   - [Login Flow](#login-flow)
   - [Logout Flow](#logout-flow)
   - [Session Persistence](#session-persistence)
   - [OAuth / Social Login](#oauth--social-login)
2. [Forms and Validation](#2-forms-and-validation)
   - [Input Validation](#input-validation)
   - [Multi-Step Wizard](#multi-step-wizard)
   - [File Upload](#file-upload)
   - [Dynamic Forms](#dynamic-forms)
3. [Navigation and Routing](#3-navigation-and-routing)
   - [Route Transitions](#route-transitions)
   - [Deep Linking and URL State](#deep-linking-and-url-state)
   - [Back/Forward Navigation](#backforward-navigation)

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
