import type { Locator, Page } from '@playwright/test';

export class HomePage {
  readonly heading: Locator;
  readonly explorePlaygroundLink: Locator;
  readonly registrationLink: Locator;

  constructor(private readonly page: Page) {
    this.heading = page.getByRole('heading', {
      name: 'Prueba con confianza. Automatiza con claridad.',
    });
    this.explorePlaygroundLink = page.getByRole('link', {
      name: 'Explorar el playground',
    });
    this.registrationLink = page
      .getByRole('navigation', { name: 'Navegación principal' })
      .getByRole('link', { name: 'Registro' });
  }

  async goto(): Promise<void> {
    await this.page.goto('./');
  }

  async openCatalog(): Promise<void> {
    await this.explorePlaygroundLink.click();
  }

  async openRegistration(): Promise<void> {
    await this.registrationLink.click();
  }
}
