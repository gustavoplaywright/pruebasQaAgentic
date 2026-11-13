import { Page, Locator, expect } from '@playwright/test';

/**
 * Page Object Model para el Módulo: Carrito De Compras Y Checkout
 * Encapsula la interacción con la interfaz y selectores orientados al usuario.
 */
export class CarritoDeComprasYCheckoutPage {
  readonly page: Page;
  readonly path: string;

  // Localizadores principales del componente
  readonly mainHeading: Locator;
  readonly submitButton: Locator;
  readonly successAlert: Locator;
  readonly errorAlert: Locator;
  readonly validationMessage: Locator;

  // Elementos específicos de Checkout y Cupones
  readonly couponInput: Locator;
  readonly applyCouponButton: Locator;
  readonly totalOrderAmount: Locator;
  readonly discountAmount: Locator;

  constructor(page: Page) {
    this.page = page;
    this.path = '/checkout';
    this.mainHeading = page.getByRole('heading', { name: /checkout|carrito|orden/i });
    this.couponInput = page.getByPlaceholder(/código de cupón|cupón/i).or(page.getByLabel('Cupón'));
    this.applyCouponButton = page.getByRole('button', { name: /aplicar|canjear/i });
    this.totalOrderAmount = page.locator('[data-testid="order-total"], .total-price');
    this.discountAmount = page.locator('[data-testid="discount-amount"], .discount-row');
    this.submitButton = page.getByRole('button', { name: /pagar|finalizar compra/i });
    this.successAlert = page.getByRole('alert').filter({ hasText: /descuento aplicado|cupón válido/i });
    this.errorAlert = page.getByRole('alert').filter({ hasText: /inválido|expirado|insuficiente|máximo/i });
    this.validationMessage = page.locator('.coupon-feedback, .error-message');
  }

  async goto() {
    await this.page.goto(this.path);
  }

  async applyCoupon(code: string) {
    await this.couponInput.fill(code);
    await this.applyCouponButton.click();
  }

  async expectSuccess() {
    await expect(this.successAlert).toBeVisible();
  }

  async expectError(messagePattern?: RegExp | string) {
    await expect(this.errorAlert).toBeVisible();
    if (messagePattern) {
      await expect(this.errorAlert).toContainText(messagePattern);
    }
  }
}
