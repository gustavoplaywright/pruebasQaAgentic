import type { Locator, Page } from '@playwright/test';

export interface ContactFormData {
  name: string;
  email: string;
  reason: string;
  message: string;
  preferredContact: 'Correo' | 'Teléfono';
  company?: string;
  acceptDataUse: boolean;
  simulateServerError?: boolean;
}

export class ContactPage {
  readonly form: Locator;
  readonly nameInput: Locator;
  readonly emailInput: Locator;
  readonly reasonSelect: Locator;
  readonly messageInput: Locator;
  readonly preferredContactGroup: Locator;
  readonly companyInput: Locator;
  readonly acceptDataUseCheckbox: Locator;
  readonly simulateErrorCheckbox: Locator;
  readonly status: Locator;
  readonly submitButton: Locator;

  constructor(private readonly page: Page) {
    this.form = page.getByTestId('contact-form');
    this.nameInput = this.form.getByLabel('Nombre');
    this.emailInput = this.form.getByLabel('Correo electrónico');
    this.reasonSelect = this.form.getByLabel('Motivo de contacto');
    this.messageInput = this.form.getByLabel('Mensaje');
    this.preferredContactGroup = this.form.getByRole('radiogroup', {
      name: '¿Cómo prefieres que te contactemos?',
    });
    this.companyInput = this.form.getByLabel('Empresa');
    this.acceptDataUseCheckbox = this.form.getByRole('checkbox', {
      name: 'Acepto que se utilicen mis datos para responder esta consulta.',
    });
    this.simulateErrorCheckbox = this.form.getByRole('checkbox', {
      name: 'Simular respuesta de error del servidor (solo para practicar estados E2E)',
    });
    this.status = page.getByTestId('contact-status');
    this.submitButton = this.form.getByRole('button', {
      name: 'Enviar mensaje',
    });
  }

  async goto(): Promise<void> {
    await this.page.goto('contact.html');
  }

  async fillForm(data: ContactFormData): Promise<void> {
    await this.nameInput.fill(data.name);
    await this.emailInput.fill(data.email);
    await this.reasonSelect.selectOption({ label: data.reason });
    if (data.company !== undefined) {
      await this.companyInput.fill(data.company);
    }
    await this.messageInput.fill(data.message);
    await this.preferredContactGroup
      .getByRole('radio', { name: data.preferredContact })
      .check();
    if (data.simulateServerError) {
      await this.simulateErrorCheckbox.check();
    }
    if (data.acceptDataUse) {
      await this.acceptDataUseCheckbox.check();
    }
  }

  async submit(): Promise<void> {
    await this.submitButton.click();
  }
}
