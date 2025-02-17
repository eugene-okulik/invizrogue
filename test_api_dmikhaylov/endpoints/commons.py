import allure
import requests

class Commons:
    url = "http://167.172.172.115:52353/object"
    headers = {'Content-Type': 'application/json'}
    response = None
    status_code = None
    before_update = None
    after_update = None

    @allure.step('Проверка статус кода ответа')
    def check_status_code(self, status_code):
        assert self.status_code == status_code, \
            f'Ожидаемый статус код: {status_code}, полученный статус код: {self.status_code}'

    def __get_object(self, object_id):
        return requests.get(f'{self.url}/{object_id}', headers=self.headers)

    @allure.step('Получение объекта до его изменения')
    def get_before_update(self, object_id):
        self.before_update = self.__get_object(object_id)

    @allure.step('Получение объекта после его изменения')
    def get_after_update(self, object_id):
        self.after_update = self.__get_object(object_id)
