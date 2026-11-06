import allure
from playwright.async_api import expect

from framework.pages.login_page import LoginPage


@allure.feature("User Demo Flow")
class TestDemoFlow:

    @allure.story("Demo Flow Test")
    async def test_standard_user_can_view_inventory(self, page):
        """Verify a standard user can log in and see all inventory items."""
        login_page = LoginPage(page)
        await login_page.navigate()

        await expect(page).to_have_title("Swag Labs")
        await expect(page.locator(login_page.USERNAME_INPUT)).to_be_visible()
        await expect(page.locator(login_page.PASSWORD_INPUT)).to_be_visible()

        await login_page.login("standard_user", "secret_sauce")
        await expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        await expect(page.locator(login_page.INVENTORY_CONTAINER)).to_be_visible()
        await expect(page.locator(".inventory_item")).to_have_count(6)
       