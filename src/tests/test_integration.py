from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_tron_info_integration(monkeypatch):
    class DummyTron:
        def get_account_balance(self, address: str) -> float:
            return 100.0

        def get_account_resource(self, address: str) -> dict:
            return {"free_net_limit": 50, "energy_limit": 20}

    monkeypatch.setattr("src.tron.service.Tron", lambda: DummyTron())

    response = client.post("/tron/", json={"address": "TXYZ"})
    assert response.status_code == 200
    data = response.json()
    assert data["address"] == "TXYZ"
    assert data["trx_balance"] == 100.0
    assert data["bandwidth"] == 50
    assert data["energy"] == 20
