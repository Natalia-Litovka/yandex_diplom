import requests
import configuration
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)


def get_order_info():
    track_number = data.headers.copy()
    track_number["track"] = "t"
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK,
                        params={"t": track_number})
