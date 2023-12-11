# Наталья Литовка, 11-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_create_and_track_order():
    track_number = sender_stand_request.get_track_number_order()
    get_response = sender_stand_request.get_order_info(track_number)
    assert get_response.status_code == 200
