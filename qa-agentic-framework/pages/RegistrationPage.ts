import type { Locator, Page } from '@playwright/test';

export interface RegistrationFormData {
  fullName: string;
  email: string;
  password: string;
  confirmPassword: string;
  age: string;
  country: string;
  accountType: 'Personal' | 'Equipo' | 'Estudiante';
  acceptTerms: boolean;
}

export class RegistrationPage {
  readonly form: Locator;
  readonly fullNameInput: Locator;
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly confirmPasswordInput: Locator;
  readonly ageInput: Locator;
  readonly countrySelect: Locator;
  readonly acceptTermsCheckbox: Locator;
  readonly submitButton: Locator;

  constructor(private readonly page: Page) {
    this.form = page.getByTestId('registration-form');
    this.fullNameInput = this.form.getByLabel('Nombre completo');
    this.emailInput = this.form.getByLabel('Correo electrónico');
    this.passwordInput = this.form.getByRole('textbox', {
      name: 'Contraseña',
      exact: true,
    });
    this.confirmPasswordInput = this.form.getByLabel('Confirmar contraseña');
    this.ageInput = this.form.getByLabel('Edad');
    this.countrySelect = this.form.getByLabel('País');
    this.acceptTermsCheckbox = this.form.getByRole('checkbox', {
      name: 'Acepto los términos de uso y la política de privacidad.',
    });
    this.submitButton = this.form.getByRole('button', { name: 'Crear cuenta' });
  }

  async goto(): Promise<void> {
    await this.page.goto('form.html');
  }

  async fillForm(data: RegistrationFormData): Promise<void> {
    await this.fullNameInput.fill(data.fullName);
    await this.emailInput.fill(data.email);
    await this.passwordInput.fill(data.password);
    await this.confirmPasswordInput.fill(data.confirmPassword);
    await this.ageInput.fill(data.age);
    await this.countrySelect.selectOption({ label: data.country });
    await this.form.getByRole('radio', { name: data.accountType }).check();
    if (data.acceptTerms) {
      await this.acceptTermsCheckbox.check();
    }
  }

  async submit(): Promise<void> {
    await this.submitButton.click();
  }
}
