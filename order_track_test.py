# Наталья Литовка, 11-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_create_and_track_order():
    get_response = sender_stand_request.get_order_info()
    assert get_response.status_code == 200
