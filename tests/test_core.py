from email import message
from fastapi.testclient import TestClient
from api.main import app # api.main esta en la carpeta api el main.py

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello World"}
