"""Register page object."""
from framework.pages.base_page import BasePage

class RegisterPage(BasePage):
    """Register page object."""
    
    URL = "https://www.saucedemo.com/"
    
    # Locators
    FULL_NAME_INPUT = "#fullName"
    EMAIL_INPUT = "#email"
    USERNAME_INPUT = "#userId"
    PASSWORD_INPUT = "#password"
    CONFIRM_PASSWORD_INPUT = "#confirmPassword"
    REGISTER_BUTTON = "button:has-text('Create Account')"
    LOGIN_LINK = "a:has-text('Sign in here')"

    async def navigate(self):
        """Navigate to register page."""
        await self.navigate_to(self.URL)
        
    async def register_user(self, full_name, email, username, password):
        """Register a new user."""
        await self.fill(self.FULL_NAME_INPUT, full_name)
        await self.fill(self.EMAIL_INPUT, email)
        await self.fill(self.USERNAME_INPUT, username)
        await self.fill(self.PASSWORD_INPUT, password)
        await self.fill(self.CONFIRM_PASSWORD_INPUT, password)
        await self.click(self.REGISTER_BUTTON)
