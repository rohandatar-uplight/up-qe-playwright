"""Home page object."""
from framework.pages.base_page import BasePage

class HomePage(BasePage):
    """Home page of the application."""
    
    # Locators
    GET_STARTED_LINK = "text=Get started"
    SEARCH_BUTTON = "button.DocSearch-Button"
    
    async def navigate(self):
        """Navigate to home page."""
        # We access config from a centralized place or pass it. 
        # For now, we'll assume the URL is passed or we get it from config if we import it.
        # But navigate_to accepts a URL.
        # Let's keep it simple and just use the method from BasePage with explicit URL in test for now, 
        # or better, use a relative path if we had a baseUrl set in context (which we don't yet).
        pass 

    async def click_get_started(self):
        """Click on Get Started link."""
        await self.click(self.GET_STARTED_LINK)
        
    async def is_search_visible(self) -> bool:
        """Check if search button is visible."""
        return await self.is_visible(self.SEARCH_BUTTON)
