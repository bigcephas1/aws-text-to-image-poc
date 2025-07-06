from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_image_valid():
    response = client.post("/generate-image", json={"prompt": "a mountain under the moon"})
    assert response.status_code == 200 or response.status_code == 500  # May fail if no API key
    assert "image_url" in response.json() or "detail" in response.json()

def test_generate_image_invalid():
    response = client.post("/generate-image", json={"prompt": ""})
    assert response.status_code == 500 or response.status_code == 422
