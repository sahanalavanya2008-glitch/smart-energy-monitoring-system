from fastapi.testclient import TestClient
from backend_api import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_energy_endpoint():

    response = client.get("/energy")

    assert response.status_code == 200
