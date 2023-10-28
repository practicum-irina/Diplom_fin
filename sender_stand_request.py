import configuration
import requests
import data


def post_new_order(): # Выполнить запрос на создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json=data.order_body)

def save_track():   # Сохранить номер трека заказа
    order_response = post_new_order()
    current_order = order_response.json().copy()
    current_order["t"] = current_order["track"]
    current_order.pop("track")
    return current_order

def get_order_on_track(): # Выполнить запрос на получения заказа по треку
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
                        params=save_track())

response = get_order_on_track()
