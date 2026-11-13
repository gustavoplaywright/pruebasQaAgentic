import { Page, Locator, expect } from '@playwright/test';

/**
 * Page Object Model para el Módulo: Autenticacion Y Seguridad
 * Encapsula la interacción con la interfaz y selectores orientados al usuario.
 */
export class AutenticacionYSeguridadPage {
  readonly page: Page;
  readonly path: string;

  // Localizadores principales del componente
  readonly mainHeading: Locator;
  readonly submitButton: Locator;
  readonly successAlert: Locator;
  readonly errorAlert: Locator;
  readonly validationMessage: Locator;

  // Elementos específicos de Autenticación
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly confirmPasswordInput: Locator;
  readonly lockoutBanner: Locator;

  constructor(page: Page) {
    this.page = page;
    this.path = '/login';
    this.mainHeading = page.getByRole('heading', { level: 1 });
    this.emailInput = page.getByLabel('Correo Electrónico').or(page.getByPlaceholder('usuario@dominio.com'));
    this.passwordInput = page.getByLabel('Contraseña').or(page.getByPlaceholder('Ingresa tu contraseña'));
    this.confirmPasswordInput = page.getByLabel('Confirmar Contraseña');
    this.submitButton = page.getByRole('button', { name: /Iniciar Sesión|Registrarse|Enviar/i });
    this.successAlert = page.getByRole('alert').filter({ hasText: /éxito|bienvenido|confirmación/i });
    this.errorAlert = page.getByRole('alert').filter({ hasText: /error|inválid|bloquead|requerid/i });
    this.validationMessage = page.locator('.field-validation-error, .invalid-feedback');
    this.lockoutBanner = page.getByRole('alert').filter({ hasText: /bloqueada temporalmente/i });
  }

  async goto() {
    await this.page.goto(this.path);
    await expect(this.mainHeading).toBeVisible();
  }

  async fillCredentials(email: string, pass: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(pass);
  }

  async submit() {
    await this.submitButton.click();
  }

  async login(email: string, pass: string) {
    await this.fillCredentials(email, pass);
    await this.submit();
  }

  async register(email: string, pass: string, confirmPass?: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(pass);
    if (confirmPass && await this.confirmPasswordInput.isVisible()) {
      await this.confirmPasswordInput.fill(confirmPass);
    }
    await this.submit();
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
