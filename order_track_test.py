# Наталья Литовка, 11-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def get_new_order_track():
    # Создать новый заказ
    order_body = data.order_body
    # получить ответ по созданному заказу
    response_order = sender_stand_request.post_new_order(order_body)
    # Запомнить трек заказа
    return response_order.json()["track"]


# получить данные заказа по треку
def get_order_info():
    # сохраним трек заказа
    track = get_new_order_track()
    # запрос на данные по номеру трека
    response_order = sender_stand_request.get_order_info(track)
    # вернуть ответ сервера
    return response_order


# проверить статус ответа
def test_order_info():
    assert get_order_info().status_code == 200
