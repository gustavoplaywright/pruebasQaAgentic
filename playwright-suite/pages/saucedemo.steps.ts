// steps/saucedemo.steps.ts
import { expect, test } from '@playwright/test';
import { SauceDemoPage } from '../pages/saucedemoLogin';
import { InventoryPage } from '../pages/saucedemoInventorypage';

export class SauceDemoSteps {
    constructor(
        private readonly loginPage: SauceDemoPage,
        private readonly inventoryPage: InventoryPage,
    ) {}

    async loginSuccessfully(user: string, pass: string): Promise<void> {
        await test.step(`Login como ${user}`, async () => {
            // 1) ir a la página
            await this.loginPage.goto();
            // 2) hacer login con user y pass
            await this.loginPage.login(user, pass);
            // 3) verificar que se ve el título de Products
            await expect(this.inventoryPage.title).toBeVisible();
        });
    }
}