import { Locator, Page } from '@playwright/test';

export class InventoryPage {
    readonly page: Page;
    readonly title: Locator;
    readonly backpack: Locator;
    readonly fleeceJacket: Locator;
    readonly cart: Locator;

    // agregá acá los locators de: mochila, campera (fleece jacket) y carrito

    constructor(page: Page) {
        this.page = page;
        this.title = page.getByText('Products');
        // asigná acá los demás locators
        this.backpack = page.locator('#add-to-cart-sauce-labs-backpack');
        this.fleeceJacket = page.locator('#add-to-cart-sauce-labs-fleece-jacket');
        this.cart = page.locator('[data-test="shopping-cart-link"]');
    }

    // agregá acá el método goToCart()
    async goToCart() {

        await this.cart.click();

    }
        
    }

