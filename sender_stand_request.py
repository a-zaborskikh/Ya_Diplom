# Анастасия Заборских, 8-а когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)


def get_order_track():
    post_new_order(data.order_body)
    track = post_new_order(data.order_body).json()["track"]
    return track


def receive_order_by_track():
    return requests.get(configuration.URL_SERVICE + '?t=' + configuration.GET_ORDER)
