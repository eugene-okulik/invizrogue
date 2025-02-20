import allure
import requests
from endpoints.commons import Commons


class CreateObject(Commons):
    @allure.step('Отправка POST-запроса для создания объекта')
    def new_object(self, clean, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.status_code = self.response.status_code

        if self.status_code == 200:
            clean(self.response.json()["id"])
        return self.response

    @allure.step('Проверка названия созданного объекта')
    def check_response_name_is_correct(self, name):
        assert self.response.json()['name'] == name, \
            f'Ожидаемое название объекта: {name}, полученное название объекта: {self.response.json()["name"]}'

    @allure.step('Проверка цвета созданного объекта')
    def check_response_color_is_correct(self, color):
        assert self.response.json()['data']['color'] == color, \
            f'Ожидаемый цвет объекта: {color}, полученный цвет объекта: {self.response.json()["data"]["color"]}'

    @allure.step('Проверка размера созданного объекта')
    def check_response_size_is_correct(self, size):
        assert self.response.json()['data']['size'] == size, \
            f'Ожидаемый размер объекта: {size}, полученный размер объекта: {self.response.json()["data"]["size"]}'
