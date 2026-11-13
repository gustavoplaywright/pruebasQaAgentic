import { expect, test } from '@playwright/test';
import { HomePage } from '../../pages/HomePage.js';
import { RegistrationPage } from '../../pages/RegistrationPage.js';

test.describe('Inicio', () => {
  test('muestra la página principal y permite explorar el catálogo', async ({
    page,
  }) => {
    const homePage = new HomePage(page);

    await homePage.goto();

    await expect(homePage.heading).toBeVisible();
    await homePage.openCatalog();
    await expect(page).toHaveURL(/\/catalog\.html$/);
    await expect(
      page.getByRole('heading', { name: 'Un catálogo para probar' }),
    ).toBeVisible();
  });

  test('la navegación al registro mantiene bloqueado el envío con campos vacíos', async ({
    page,
  }) => {
    const homePage = new HomePage(page);
    const registrationPage = new RegistrationPage(page);

    await homePage.goto();
    await homePage.openRegistration();
    await registrationPage.submit();

    await expect(registrationPage.fullNameInput).toHaveAttribute(
      'required',
      '',
    );
    await expect(registrationPage.fullNameInput).toHaveValue('');
  });
});
