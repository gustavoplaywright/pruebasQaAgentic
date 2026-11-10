import { expect, test } from '@playwright/test';
import { CatalogPage } from '../../pages/CatalogPage.js';

test.describe('Catálogo', () => {
  test('filtra por categoría y encuentra un producto', async ({ page }) => {
    const catalogPage = new CatalogPage(page);

    await catalogPage.goto();
    await catalogPage.filterByCategory('Kits');
    await catalogPage.searchProducts('Kit de bienvenida');

    await expect(catalogPage.productCard('Kit de bienvenida')).toBeVisible();
    await expect(catalogPage.productCards).toHaveCount(1);
    await expect(catalogPage.resultSummary).toHaveText(
      'Mostrando 1 de 1 productos',
    );
  });

  test('muestra cero resultados para una búsqueda inexistente', async ({
    page,
  }) => {
    const catalogPage = new CatalogPage(page);

    await catalogPage.goto();
    await catalogPage.searchProducts('producto-inexistente');

    await expect(catalogPage.productCards).toHaveCount(0);
    await expect(catalogPage.resultSummary).toHaveText(
      'Mostrando 0 de 0 productos',
    );
  });
});
