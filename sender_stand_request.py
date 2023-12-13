import requests
import configuration
import data


def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)


def get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK,
                        params={"t": track_number})
