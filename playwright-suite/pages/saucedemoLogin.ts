import { expect, Locator, Page } from '@playwright/test';

export class SauceDemoPage {
    readonly url = 'https://www.saucedemo.com';
    readonly page: Page;
    readonly username: Locator;
    readonly password: Locator;
    readonly loginButton: Locator;

constructor(page: Page) {
    this.page = page;
    this.username = page.locator('#user-name');
    this.password = page.locator('#password');
    this.loginButton = page.locator('#login-button');
}

async goto() {
    await this.page.goto(this.url);
    await expect(this.page).toHaveTitle('Swag Labs');
}

async login(username: string, password: string) {
    await this.username.fill(username);
    await this.password.fill(password);
    await this.loginButton.click();
}
}