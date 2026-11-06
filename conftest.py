"""Global pytest configuration."""
import subprocess

import pytest
import pytest_asyncio
from playwright.async_api import async_playwright

from framework.utils.config_reader import get_config
from framework.utils.logger import setup_logger

# Setup logging
setup_logger()

@pytest.fixture(scope="session")
def config():
    """Configuration fixture."""
    return get_config()

def pytest_addoption(parser):
    """Add browser options for the async Playwright fixtures."""
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        choices=("chromium", "firefox", "webkit"),
        help="Browser to run tests on",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        help="Run tests in headed mode",
    )

@pytest.fixture(scope="session")
def browser_type_launch_args(config, request):
    """
    Browser type launch arguments.
    Can be customized based on config and CLI arguments.
    """
    headless = config.get('headless', True)
    if request.config.getoption("--headed"):
        headless = False
        
    launch_args = {
        "headless": headless,
        "slow_mo": config.get('slow_mo', 0),
        "args": []
    }

    if not headless:
        launch_args["args"].append("--start-maximized")
        
    return launch_args

@pytest.fixture(scope="session")
def browser_context_args(request):
    """
    Browser context arguments.
    """
    if request.config.getoption("--headed"):
        return {"viewport": {"width": 1920, "height": 1080}}
    else:
        return {"viewport": {"width": 1920, "height": 1080}}

@pytest.fixture(scope="session")
def browser_name(request):
    """Configured browser name."""
    return request.config.getoption("--browser")

@pytest_asyncio.fixture(scope="function")
async def browser_instance(browser_name, browser_type_launch_args):
    """
    Function-scoped browser instance.
    Launches the browser for each test to ensure isolation and stability.
    """
    async with async_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = await browser_type.launch(**browser_type_launch_args)
        yield browser
        await browser.close()

@pytest_asyncio.fixture(scope="function")
async def context(browser_instance, browser_context_args):
    """
    Function-scoped browser context.
    Creates a new context for each test to ensure isolation.
    """
    browser_context = await browser_instance.new_context(**browser_context_args)
    yield browser_context
    await browser_context.close()

@pytest_asyncio.fixture(scope="function")
async def page(context):
    """
    Function-scoped page fixture.
    Creates a new page within the context.
    """
    page = await context.new_page()
    yield page
    

def pytest_sessionfinish(session, exitstatus):
    """Generate the single-file Allure report after the pytest session completes."""
    print("\n--- Generating Single-File Allure Report ---")
    report_dir = "reports/allure-results"
    output_dir = "reports/allure-report"

    try:
        subprocess.run(
            [
                "/bin/rm -rf reports/allure-results/*",
               
                
            ],
            check=True,
        )
        print(f"Existing reports deleted successfully.")
    except FileNotFoundError:
        print(
            "Error: Allure CLI is not installed or not in your system PATH. "
            "Install it with: brew install allure or npm install -g allure-commandline"
        )
    except subprocess.CalledProcessError as e:
        print(f"Failed to delete report: {e}")

        subprocess.run(
            [
                "allure",
                "generate",
                report_dir,
                
     
                "--single-file",
                "--clean",
                 "-o",
                output_dir,
            ],
            check=True,
        )
        print(f"Report successfully generated inside {output_dir}/index.html")
    except FileNotFoundError:
        print(
            "Error: Allure CLI is not installed or not in your system PATH. "
            "Install it with: brew install allure or npm install -g allure-commandline"
        )
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate report: {e}")