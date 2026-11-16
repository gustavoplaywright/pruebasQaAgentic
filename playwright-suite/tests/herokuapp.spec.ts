import { expect, test } from '@playwright/test';
import { HerokuappPage } from '../pages/page_herokuapp';


let herokuappPage: HerokuappPage;

test('Login exitoso', async({page})=>{
    const herokuappPage = new HerokuappPage(page);
    await herokuappPage.goto();
    await herokuappPage.username.fill('tomsmith');
    await herokuappPage.password.fill('SuperSecretPassword!');
    await herokuappPage.submit.click();
    await expect(page).toHaveURL('https://the-internet.herokuapp.com/secure');
    await expect(page.getByText('You logged into a secure area')).toBeVisible();
    await page.getByRole('link', { name: 'Close' }).click();
    await expect(page.getByText('You logged into a secure area')).not.toBeVisible();
    await page.getByRole('link', { name: 'Logout' }).click();
    await expect(page.getByText('You logged out of the secure area')).toBeVisible();

})

test('Login fallido', async({page}) => {
    const herokuappPage = new HerokuappPage(page);
    await herokuappPage.goto();
    await herokuappPage.username.fill('tomsmith');
    await herokuappPage.password.fill('PasswordFalsa');
    await herokuappPage.submit.click();
    await expect (page.locator('body')).toContainText(/is invalid!/);
    await page.getByRole('link', { name: 'Close' }).click();
    await expect (page.locator('body')).not.toContainText(/is invalid!/);
})

