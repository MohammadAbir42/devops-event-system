"""
Basic API tests.
"""
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_health():
    """
    Verify that the health endpoint responds successfully.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.get("/health")
    assert res.status_code == 200