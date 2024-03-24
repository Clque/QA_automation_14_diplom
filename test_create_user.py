# Верховский Данила, 14-ая когорта - Финальный проект. Инженер по тестированию плюс.
import send_request
import data


def test_status_code_200():
    create_order = send_request.post_new_order(data.body_order_with_optional)
    order_num = {"t": create_order.json()["track"]}
    get_order_by_num = send_request.get_order_by_number(order_num)
    assert get_order_by_num.status_code == 200, "Статус код не равен 200"
