import requests
#import configuration
import data
import sender_stand_request

def test_create_ordrer():
    get_order = sender_stand_request.get_order()
    assert get_order.status_code == 200
