from fastapi.testclient import TestClient
from fastapi import FastAPI
from main import app
from json import JSONDecoder

client = TestClient(app)

def test_hello():
    res = client.get("/api/hello", headers={"header": "test"})

    assert res.status_code == 200
    assert res.json() == {"message": "Hello from FastAPI!"}
