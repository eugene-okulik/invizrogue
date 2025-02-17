import allure
import requests
from endpoints.commons import Commons


class UpdateObject(Commons):
    @allure.step('Отправка PUT-запроса для полного изменения объекта')
    def upd_entire_object(self, get_id, payload, headers=None):
        self.get_before_update(get_id)

        headers = headers or self.headers
        self.response = requests.put(
            f'{self.url}/{get_id}',
            json=payload,
            headers=headers
        )
        self.status_code = self.response.status_code
        return self.response

    @allure.step('Отправка PATCH-запроса для частичного изменения объекта')
    def upd_part_object(self, get_id, payload, headers=None):
        self.get_before_update(get_id)

        headers = headers or self.headers
        self.response = requests.patch(
            f'{self.url}/{get_id}',
            json=payload,
            headers=headers
        )
        self.status_code = self.response.status_code
        return self.response

    @allure.step('Проверка, что объект был изменен')
    def check_object_has_been_updated(self, data):
        new_data = self.before_update.json()
        for key, value in data.items():
            new_data[key] = value
        assert self.before_update.json() != data, \
            (f'Ожидаемый объект: {new_data},\n'
             f'Полученный объект: {self.before_update.json()}')

    @allure.step('Проверка, что объект не был изменен')
    def check_object_has_not_been_updated(self, object_id):
        self.get_after_update(object_id)
        assert self.before_update.json() == self.after_update.json(), \
            (f'Ожидаемый объект: {self.before_update.json()},\n'
             f'Полученный объект: {self.after_update.json()}')
