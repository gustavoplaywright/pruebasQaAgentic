import { expect, test } from '@playwright/test';
import { DashboardPage } from '../../pages/DashboardPage.js';

test.describe('Dashboard', () => {
  test('filtra pedidos por texto y estado', async ({ page }) => {
    const dashboardPage = new DashboardPage(page);

    await dashboardPage.goto();
    await dashboardPage.searchOrders('Sofía Martínez');

    await expect(dashboardPage.orderRows).toHaveCount(1);
    await expect(dashboardPage.orderRows).toContainText('ORD-1042');

    await dashboardPage.searchOrders('');
    await dashboardPage.filterByStatus('Pendiente');

    await expect(dashboardPage.orderRows).toHaveCount(2);
    await expect(dashboardPage.orderRows).toContainText([
      'ORD-1041',
      'ORD-1038',
    ]);
  });

  test('no muestra pedidos con una búsqueda sin coincidencias', async ({
    page,
  }) => {
    const dashboardPage = new DashboardPage(page);

    await dashboardPage.goto();
    await dashboardPage.searchOrders('pedido-inexistente');

    await expect(dashboardPage.orderRows).toHaveCount(0);
  });
});
