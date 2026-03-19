from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities_aaa():
    # Arrange
    url = "/activities"

    # Act
    resp = client.get(url)

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert "Chess Club" in data
    assert isinstance(data["Chess Club"]["participants"], list)


def test_signup_prevents_duplicate_aaa():
    # Arrange
    activity = "Soccer Club"
    email = "aaa@example.com"

    # Act
    first = client.post(f"/activities/{activity}/signup", params={"email": email})
    duplicate = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert first.status_code == 200
    assert "Signed up" in first.json()["message"]
    assert duplicate.status_code == 400
    assert "already signed up" in duplicate.json()["detail"].lower()


def test_remove_participant_aaa():
    # Arrange
    activity = "Soccer Club"
    email = "bbb@example.com"
    client.post(f"/activities/{activity}/signup", params={"email": email})

    # Act
    removed = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert removed.status_code == 200
    assert "Removed" in removed.json()["message"]


def test_remove_missing_returns_404_aaa():
    # Arrange
    activity = "Soccer Club"
    email = "does-not-exist@example.com"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 404
