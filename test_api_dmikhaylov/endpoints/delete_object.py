import allure
import requests
from endpoints.commons import Commons


class DeleteObject(Commons):
    obj_id = None

    @allure.step('Отправка запроса DELETE на удаление объекта')
    def del_object(self, obj_id):
        self.obj_id = obj_id
        self.response = requests.delete(f'{Commons.url}/{obj_id}')
        self.status_code = self.response.status_code
        return self.response

    @allure.step('Проверка корректности сообщения об успешном удалении')
    def check_response_message_is_correct(self):
        assert self.response.text == f"Object with id {self.obj_id} successfully deleted", \
               (f'Ожидаемое сообщение: "Object with id {self.obj_id} successfully deleted",\n'
                f'полученное сообщение: "{self.response.text}"')
