# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: playwright-suite\tests\sauceDemo.spec.ts >> Compra exitosa
- Location: playwright-suite\tests\sauceDemo.spec.ts:32:5

# Error details

```
Error: locator.click: Target page, context or browser has been closed
Call log:
  - waiting for locator('[data-test="checkout"]')

```

# Test source

```ts
  1  | import { Locator, Page } from '@playwright/test';
  2  | 
  3  | export class CartPage {
  4  |     readonly page: Page;
  5  |     readonly title: Locator;
  6  |     readonly continuarButton: Locator;
  7  |     readonly checkoutButton: Locator;
  8  |     readonly cantidad: Locator;
  9  |     readonly descripcion: Locator;
  10 | 
  11 | 
  12 |     constructor(page: Page) {
  13 |         this.page = page;
  14 |         this.title = page.getByText('Your Cart');
  15 |         this.continuarButton = page.locator('[data-test="continue-shopping"]');
  16 |         this.checkoutButton = page.locator('[data-test="checkout"]');
  17 |         this.cantidad = page.locator('[data-test="quantity"]');
  18 |         this.descripcion = page.locator('[data-test="description"]');
  19 |     }
  20 | 
  21 |     async checkoutbtn () {
> 22 |         await this.checkoutButton.click();
     |                                   ^ Error: locator.click: Target page, context or browser has been closed
  23 |     }
  24 | 
  25 |     async continuar () {
  26 |         await this.continuarButton.click();
  27 |     }
  28 | }
  29 | 
```