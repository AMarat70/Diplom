import configuration
import requests
import data

def create_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=data.order_body,
                         headers=data.headers)
    return response.json()["track"]