import requests
import configuration
import data
import sender_stand_request

def test_create_ordrer():
    order_track = sender_stand_request.create_order(data.order_body)
    get_orders = requests.get(configuration.URL_SERVICE + configuration.ORDERS_PATH + str(order_track))
    assert get_orders.status_code == 200
