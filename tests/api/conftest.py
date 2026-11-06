
import httpx
import pytest_asyncio


@pytest_asyncio.fixture
async def api_request_context():
    """Provide an async HTTP client for the ReqRes API tests."""
    async with httpx.AsyncClient(
        base_url="https://reqres.in",
        headers={"Accept": "application/json"},
        timeout=10.0,
    ) as client:
        yield client