import { Locator, Page } from '@playwright/test';

export class OverviewPage {
    readonly page: Page;
    readonly title: Locator;
    readonly finishButton: Locator;
    readonly cancelButton: Locator;


    constructor(page: Page) {
        this.page = page;
        this.title = page.getByText('Checkout: Complete!');
        this.finishButton = page.locator('[data-test="finish"]');
        this.cancelButton = page.locator('[data-test="cancel"]');

    }

    async finish () {
        await this.finishButton.click();
    }

    async cancel () {
        await this.cancelButton.click();
    }
}
