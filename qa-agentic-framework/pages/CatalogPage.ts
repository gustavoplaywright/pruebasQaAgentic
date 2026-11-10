import type { Locator, Page } from '@playwright/test';

export class CatalogPage {
  readonly searchInput: Locator;
  readonly categoryFilter: Locator;
  readonly productList: Locator;
  readonly productCards: Locator;
  readonly resultSummary: Locator;
  readonly loadMoreButton: Locator;

  constructor(private readonly page: Page) {
    this.searchInput = page.getByTestId('product-search');
    this.categoryFilter = page.getByTestId('category-filter');
    this.productList = page.getByTestId('product-list');
    this.productCards = this.productList.getByTestId('product-card');
    this.resultSummary = page.getByText(/^Mostrando \d+ de \d+ productos$/);
    this.loadMoreButton = page.getByTestId('load-more');
  }

  async goto(): Promise<void> {
    await this.page.goto('catalog.html');
  }

  async searchProducts(query: string): Promise<void> {
    await this.searchInput.fill(query);
  }

  async filterByCategory(category: string): Promise<void> {
    await this.categoryFilter.selectOption({ label: category });
  }

  productCard(productName: string): Locator {
    return this.productCards.filter({
      has: this.page.getByRole('heading', {
        level: 3,
        name: productName,
      }),
    });
  }

  async loadMore(): Promise<void> {
    await this.loadMoreButton.click();
  }
}
