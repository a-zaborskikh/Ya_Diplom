# Анастасия Заборских, 8-а когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def positive_assert():
    current_body = data.order_body.copy()
    order_response = sender_stand_request.post_new_order(current_body)
    order_id = order_response.json()["track"]
    get_order_response = sender_stand_request.receive_order_by_track(order_id)

    assert get_order_response.status_code == 200


# Вызов функции
def test_create_order_success_response():
    positive_assert()
