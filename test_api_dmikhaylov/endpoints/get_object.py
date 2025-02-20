import allure
import requests
from endpoints.commons import Commons


class GetObject(Commons):
    @allure.step('Отправка GET-запроса для получения объекта')
    def get_object(self, get_id, headers=None):
        headers = headers or self.headers
        self.response = requests.get(f'{self.url}/{get_id}', headers=headers)
        self.status_code = self.response.status_code
        return self.response
