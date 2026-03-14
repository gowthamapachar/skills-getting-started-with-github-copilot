import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    # Arrange
    test_client = client

    # Act
    response = test_client.get("/")

    # Assert
    assert response.status_code == 200
    assert "<title>Mergington High School Activities</title>" in response.text
