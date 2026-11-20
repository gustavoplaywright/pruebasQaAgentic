import { Locator, Page } from '@playwright/test';
export class CheckoutPage {
    readonly url = 'https://www.saucedemo.com/checkout-step-one.html'
    readonly page: Page;
    readonly firstName: Locator;
    readonly lastName: Locator;
    readonly postalCode: Locator;
    readonly continue: Locator;

    constructor(page: Page) {
        this.page = page;
        this.firstName = page.locator('[data-test="firstName"]');
        this.lastName = page.locator('[data-test="lastName"]');
        this.postalCode = page.locator('[data-test="postalCode"]');
        this.continue = page.locator('[data-test="continue"]');
    }


async fillInformation(first: string, last: string, zip: string) {
        await this.firstName.fill(first);
        await this.lastName.fill(last);
        await this.postalCode.fill(zip);
    }

async continueToOverview(){
    await this.continue.click();
}

}

