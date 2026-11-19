import { Locator, Page } from '@playwright/test';

export class CartPage {
    readonly page: Page;
    readonly title: Locator;
    readonly continueButton: Locator;
    readonly checkoutButton: Locator;
    readonly quantity: Locator;
    readonly description: Locator;


    constructor(page: Page) {
        this.page = page;
        this.title = page.getByText('Your Cart');
        this.continueButton = page.locator('[data-test="continue-shopping"]');
        this.checkoutButton = page.locator('[data-test="checkout"]');
        this.quantity = page.locator('[data-test="quantity"]');
        this.description = page.locator('[data-test="description"]');
    }

    async checkoutbtn () {
        await this.checkoutButton.click();
    }

    async continuar () {
        await this.continueButton.click();
    }
}

