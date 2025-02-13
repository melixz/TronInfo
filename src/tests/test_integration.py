import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.tron.service import TronService

client = TestClient(app)


@pytest.mark.asyncio
async def test_get_tron_info_integration(monkeypatch):
    class DummyTronService:
        async def get_tron_info(self, address: str):
            return {
                "address": address,
                "trx_balance": 100.0,
                "bandwidth": 50,
                "energy": 20,
            }

    monkeypatch.setattr(TronService, "get_tron_info", DummyTronService().get_tron_info)

    response = client.post("/tron/", json={"address": "TXYZ"})
    assert response.status_code == 200
    data = response.json()
    assert data["address"] == "TXYZ"
    assert data["trx_balance"] == 100.0
    assert data["bandwidth"] == 50
    assert data["energy"] == 20
