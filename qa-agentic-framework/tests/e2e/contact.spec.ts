import { expect, test } from '@playwright/test';
import { ContactPage, type ContactFormData } from '../../pages/ContactPage.js';

const validContact: ContactFormData = {
  name: 'Alex Rivera',
  email: 'alex@example.com',
  reason: 'Consulta comercial',
  company: 'PruebaLab QA',
  message: 'Quisiera conocer más sobre sus servicios.',
  preferredContact: 'Correo',
  acceptDataUse: true,
};

test.describe('Contacto', () => {
  test('envía una consulta comercial válida', async ({ page }) => {
    const contactPage = new ContactPage(page);

    await contactPage.goto();
    await contactPage.fillForm(validContact);
    await contactPage.submit();

    await expect(contactPage.status).toBeVisible();
  });

  test('no envía el formulario cuando falta el nombre requerido', async ({
    page,
  }) => {
    const contactPage = new ContactPage(page);

    await contactPage.goto();
    await contactPage.submit();

    await expect(contactPage.nameInput).toHaveAttribute('required', '');
    await expect(contactPage.nameInput).toHaveValue('');
    await expect(contactPage.status).not.toBeVisible();
  });
});
