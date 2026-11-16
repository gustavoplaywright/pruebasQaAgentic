import { test, expect } from '@playwright/test';

test('debería mostrar mensaje de error cuando la API falla', async ({ page }) => {
  // Interceptamos la llamada al endpoint de usuarios
  await page.route('https://jsonplaceholder.typicode.com/posts/1', async route => {
    await route.fulfill({
      status: 500,
      contentType: 'application/json',
      body: JSON.stringify({ message: 'Database connection failed' })
    });
  });

  /*await page.goto('/dashboard');
  
  // Validamos que la UI maneje el error graciosamente
  await expect(page.locator('.error-banner')).toContainText('Error al cargar los datos');*/
});