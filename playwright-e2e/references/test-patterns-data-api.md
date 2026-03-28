# Test Patterns: Data Display, API Integration, and Performance

Common E2E test patterns for data tables, search, API mocking, error handling, and performance testing. Each pattern includes when to use, TypeScript code, key assertions, and common gotchas.

## Table of Contents

1. [Data Display](#1-data-display)
   - [Tables with Pagination, Sorting, Filtering](#tables-with-pagination-sorting-filtering)
   - [Infinite Scroll](#infinite-scroll)
   - [Search](#search)
2. [API Integration](#2-api-integration)
   - [Mock Setup and Intercept Patterns](#mock-setup-and-intercept-patterns)
   - [Error State Testing](#error-state-testing)
   - [Loading State Verification](#loading-state-verification)
3. [Performance](#3-performance)
   - [Web Vitals Measurement](#web-vitals-measurement)
   - [Network Throttling](#network-throttling)

---

## 1. Data Display

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

## 2. API Integration

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

## 3. Performance

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
