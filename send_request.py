import requests
import configuration


# POST-запрос для создания заказа
def post_new_order(order_body):
    return requests.post(configuration.URL + configuration.CREATE_ORDER_PATH, json=order_body)


# GET-запрос для проверки заказа по номеру
def get_order_by_number(get_order_body):
    return requests.get(configuration.URL + configuration.GET_ORDER_PATH, params=get_order_body)
