from src.app import activities


def test_unregister_removes_a_participant_from_an_activity(client):
    # Arrange
    activity_name = "Tennis Club"
    email = "james@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_unregister_returns_not_found_for_a_missing_participant(client):
    # Arrange
    activity_name = "Drama Club"
    email = "ghost@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found"}


def test_unregister_returns_not_found_for_an_unknown_activity(client):
    # Arrange
    activity_name = "Robotics Club"
    email = "ghost@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}