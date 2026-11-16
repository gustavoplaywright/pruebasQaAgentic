import { expect, Locator, Page } from '@playwright/test';
export class HerokuappPage {
    readonly url = 'https://the-internet.herokuapp.com/login';
    readonly page: Page;
    readonly username: Locator;
    readonly password: Locator;
    readonly submit: Locator;

    constructor(page: Page) {
        this.page = page;
        this.username = page.getByRole('textbox', { name: 'Username' });
        this.password = page.getByRole('textbox', { name: 'Password' });
        this.submit = page.getByRole('button', { name: 'Login' });
    }


    async goto() {
        await this.page.goto(this.url);
        await expect(this.page).toHaveTitle('The Internet');
    }
}