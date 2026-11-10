import { expect, test } from '@playwright/test';
import {
  RegistrationPage,
  type RegistrationFormData,
} from '../../pages/RegistrationPage.js';

const validRegistration: RegistrationFormData = {
  fullName: 'Alex Rivera',
  email: 'alex@example.com',
  password: 'ValidPass123!',
  confirmPassword: 'ValidPass123!',
  age: '28',
  country: 'Argentina',
  accountType: 'Personal',
  acceptTerms: true,
};

test.describe('Registro', () => {
  test('crea una cuenta con datos válidos', async ({ page }) => {
    const registrationPage = new RegistrationPage(page);

    await registrationPage.goto();
    await registrationPage.fillForm(validRegistration);
    await registrationPage.submit();

    await expect(page.getByRole('status')).toBeVisible();
  });

  test('no permite enviar el formulario sin completar el nombre requerido', async ({
    page,
  }) => {
    const registrationPage = new RegistrationPage(page);

    await registrationPage.goto();
    await registrationPage.submit();

    await expect(registrationPage.fullNameInput).toHaveAttribute(
      'required',
      '',
    );
    await expect(registrationPage.fullNameInput).toHaveValue('');
    await expect(page.getByRole('status')).toHaveCount(0);
  });
});
