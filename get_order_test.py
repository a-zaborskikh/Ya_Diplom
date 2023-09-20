import sender_stand_request


def positive_assert():
    response = sender_stand_request.receive_order_by_track()
    assert response.status_code == 200


def test_create_and_check_to_track():
    positive_assert()
