from src.app import activities


def test_get_activities_returns_activity_data_and_no_store_header(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.headers["Cache-Control"] == "no-store"

    payload = response.json()
    assert expected_activity in payload
    assert payload[expected_activity]["description"] == activities[expected_activity]["description"]
    assert payload[expected_activity]["participants"] == activities[expected_activity]["participants"]


def test_get_activities_returns_all_configured_activities(client):
    # Arrange
    expected_count = len(activities)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == expected_count