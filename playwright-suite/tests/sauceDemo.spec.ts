import { expect, test } from '@playwright/test';
import { SauceDemoPage } from '../pages/saucedemoLogin';
import { CheckoutPage } from '../pages/saucedemoCheckout';
import { InventoryPage } from '../pages/saucedemoInventorypage';
import { CartPage } from '@pages/saucedemoCart';
import { SauceDemoSteps } from '@pages/saucedemo.steps';
import { log } from 'node:console';

let sauceDemoPage: SauceDemoPage;
let checkoutPage: CheckoutPage;

test('Login exitoso', async({page})=>{

    const loginPage = new SauceDemoPage(page);
    const inventory = new InventoryPage(page);
    const steps = new SauceDemoSteps(loginPage, inventory);
    await steps.loginSuccessfully('standard_user','secret_sauce');
    await expect(page).toHaveURL(/inventory/);
    
    /*cambio a steps
    await sauceDemoPage.goto();
    await sauceDemoPage.username.fill('standard_user');
    await sauceDemoPage.password.fill('secret_sauce');
    await sauceDemoPage.loginButton.click();
    await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
    await expect(page.getByText('Products')).toBeVisible();*/
});

test('Login fallido',async({page})=>{
    const sauceDemoPage = new SauceDemoPage(page);
    await sauceDemoPage.goto();

    /*Aca cambio a pageObjectsModel a la page saucedemoLogin.ts  
    await sauceDemoPage.username.fill('standard_user');
    await sauceDemoPage.password.fill('wrong_password');
    await sauceDemoPage.loginButton.click();*/
    await sauceDemoPage.login('standard_user','wrong_password');
    await expect(page.locator('body')).toContainText(/Username and password do not match any user in this service/);
})

test('Compra exitosa', async({page})=>{
    const sauceDemoPage = new SauceDemoPage(page);
    const inventoryPage = new InventoryPage(page);
    const saucedemoCheckout = new CheckoutPage(page);
    const cartPage = new CartPage(page);
    await sauceDemoPage.goto();
    await sauceDemoPage.login('standard_user', 'secret_sauce'); /*Aca paso el metodo de saucedemoLogin*/
    await expect(page.getByText('Products')).toBeVisible();

    /*Reemplazo mis pasos por el metodo goToCart() de la page saucedemoInventorypage.ts

    await page.locator('[data-test="shopping-cart-link"]').click();*/
    await page.locator('#add-to-cart-sauce-labs-backpack').click();
    await page.locator('#add-to-cart-sauce-labs-fleece-jacket').click();
    await inventoryPage.goToCart();
    await cartPage.checkoutbtn();
    /*reemplazo por el de arriba await page.locator('[data-test="checkout"]').click();*/

    
    await expect(page.getByText('Checkout: Your Information')).toBeVisible();

  
    await saucedemoCheckout.fillInformation('Gustavo', 'Morales', 'AB1708'); /*Aca paso el metodo de saucedemoCheckout.ts*/
   /* antes de llamar al metodo checkout se hacia asi
    await checkoutPage.firstName.fill('Gustavo');
    await checkoutPage.lastName.fill('Morales');
    await checkoutPage.postalCode.fill('AB1708');*/

    /*Aca cambio a pageObjectsModel a la page sacedemoCheckout.ts
    await page.locator('[data-test="firstName"]').fill('Gustavo');
    await page.locator('[data-test="lastName"]').fill('Morales');
    await page.locator('[data-test="postalCode"]').fill('AB1708');*/


    await page.locator('[data-test="continue"]').click();
    /*await cartPage.checkoutbtn();*/
    await expect(page.getByText('Checkout: Overview')).toBeVisible();
})

