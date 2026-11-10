import type { Locator, Page } from '@playwright/test';

export class DashboardPage {
  readonly orderCount: Locator;
  readonly searchInput: Locator;
  readonly statusFilter: Locator;
  readonly ordersTable: Locator;
  readonly orderRows: Locator;
  readonly newOrderButton: Locator;

  constructor(private readonly page: Page) {
    this.orderCount = page.getByTestId('order-total');
    this.searchInput = page.getByTestId('table-search');
    this.statusFilter = page.getByTestId('status-filter');
    this.ordersTable = page.getByTestId('orders-table');
    this.orderRows = this.ordersTable
      .getByRole('row')
      .filter({ hasText: /ORD-\d+/ });
    this.newOrderButton = page.getByTestId('open-modal');
  }

  async goto(): Promise<void> {
    await this.page.goto('dashboard.html');
  }

  async searchOrders(query: string): Promise<void> {
    await this.searchInput.fill(query);
  }

  async filterByStatus(status: string): Promise<void> {
    await this.statusFilter.selectOption({ label: status });
  }

  async openNewOrder(): Promise<void> {
    await this.newOrderButton.click();
  }
}
