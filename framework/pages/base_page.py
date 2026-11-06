"""Base page class for all page objects."""
import logging
from playwright.async_api import Page, Locator, expect

class BasePage:
    """Base page class with common utility methods."""
    
    def __init__(self, page: Page):
        """Initialize base page."""
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)
    
    async def navigate_to(self, url: str):
        """Navigate to URL."""
        self.logger.info(f"Navigating to {url}")
        await self.page.goto(url, wait_until="networkidle")

      #  await self.page.pause()

    
    async def get_title(self) -> str:
        """Get page title."""
        title = await self.page.title()
        self.logger.info(f"Page title: {title}")
        return title

    async def click(self, selector: str):
        """Click on an element."""
        self.logger.info(f"Clicking on element: {selector}")
        await self.page.click(selector)

    async def fill(self, selector: str, text: str):
        """Fill text into an element."""
        self.logger.info(f"Filling '{text}' into element: {selector}")
        await self.page.fill(selector, text)

    async def get_text(self, selector: str) -> str:
        """Get text content of an element."""
        self.logger.info(f"Getting text from element: {selector}")
        return await self.page.text_content(selector)

    async def wait_for_element(self, selector: str, state: str = "visible"):
        """Wait for an element to be in a specific state."""
        self.logger.info(f"Waiting for element: {selector} to be {state}")
        await self.page.wait_for_selector(selector, state=state)

    async def is_visible(self, selector: str) -> bool:
        """Check if an element is visible."""
        return await self.page.is_visible(selector)