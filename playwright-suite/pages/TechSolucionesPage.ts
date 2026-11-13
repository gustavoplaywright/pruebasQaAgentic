import { expect, Locator, Page } from '@playwright/test';

export class TechSolucionesPage {
  readonly url = 'https://gustavoplaywright.github.io/desarrolloWeb/index.html';
  readonly page: Page;
  readonly banner: Locator;
  readonly navigation: Locator;
  readonly main: Locator;
  readonly footer: Locator;
  readonly primaryCarousel: Locator;
  readonly secondaryCarousel: Locator;
  readonly brandLink: Locator;

  constructor(page: Page) {
    this.page = page;
    this.banner = page.getByRole('banner');
    this.navigation = page.getByRole('navigation');
    this.main = page.getByRole('main');
    this.footer = page.getByRole('contentinfo');
    this.primaryCarousel = page.locator('#carouselExampleDark');
    this.secondaryCarousel = page.locator('#carouselExampleDark2');
    this.brandLink = page.getByRole('link', { name: /TECH SOLUCIONES/ }).first();
  }

  async goto() {
    await this.page.goto(this.url);
    await expect(this.page).toHaveTitle('TECH SOLUCIONES');
  }

  activeSlide(carousel: Locator): Locator {
    return carousel.locator('.carousel-item.active');
  }

  activeSlideTitle(carousel: Locator): Locator {
    return this.activeSlide(carousel).getByRole('heading');
  }

  activeIndicator(carousel: Locator): Locator {
    return carousel.locator('.carousel-indicators button.active');
  }

  slideIndicator(carousel: Locator, slideNumber: number): Locator {
    return carousel.getByRole('button', { name: `Slide ${slideNumber}` });
  }

  async selectSlide(carousel: Locator, slideNumber: number) {
    await this.slideIndicator(carousel, slideNumber).click();
  }

  async nextSlide(carousel: Locator) {
    await carousel.getByRole('button', { name: 'Siguiente' }).click();
  }

  async previousSlide(carousel: Locator) {
    await carousel.getByRole('button', { name: 'Anterior' }).click();
  }
}
