"""Login page object."""
from framework.pages.base_page import BasePage

class LoginPage(BasePage):
    """Login page object."""
    
    URL = "https://www.saucedemo.com/"
    
    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    INVENTORY_CONTAINER = '[data-test="inventory-container"]'
    
    async def navigate(self):
        """Navigate to login page."""
        await self.navigate_to(self.URL)
        
    async def login(self, username, password):
        """Perform login."""
        await self.fill(self.USERNAME_INPUT, username)
        await self.fill(self.PASSWORD_INPUT, password)
        await self.click(self.LOGIN_BUTTON)
