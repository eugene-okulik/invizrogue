import requests
import pytest
import allure


@pytest.fixture(scope='session')
def session_info():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def each_test():
    print('before test')
    yield
    print('after test')


def add_object(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    return response


def update_entire_object(obj_id, body):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{obj_id}',
        json=body,
        headers=headers
    )
    return response


def update_part_object(obj_id, body):
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{obj_id}',
        json=body,
        headers=headers
    )
    return response


def delete_object(obj_id):
    response = requests.delete(
        f'http://167.172.172.115:52353/object/{obj_id}'
    )
    return response


def get_object(obj_id):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        f'http://167.172.172.115:52353/object/{obj_id}',
        headers=headers
    )
    return response


@allure.title('Тестирование создания нового объекта')
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature('Create object')
@allure.story('Positive test')
@pytest.mark.critical
@pytest.mark.parametrize('color, size, name', [
    ("red", "nano", "Nano"),
    ("green", "micro", "Micro"),
    ("blue", "mini", "Mini")])
def test_positive_add_object(session_info, color, size, name):
    with allure.step('Подготовка данных'):
        body = {
            "data": {
                "color": color,
                "size": size
            },
            "name": name
        }
    with allure.step('Осуществление POST-запроса для создания объекта'):
        resp = add_object(body)
    with allure.step('Проверка кода ответа'):
        assert resp.status_code == 200, f'Ошибка при добавлении объекта. Статус: {resp.status_code}'
    with allure.step('Проверка имени объекта'):
        assert resp.json()['name'] == name, f'Неверное имя объекта {resp.json()["name"]}'


@allure.title('Тестирование полного изменения объекта')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Update object')
@allure.story('Positive test')
def test_positive_update_entire_object(get_new_id):
    with allure.step('Подготовка данных'):
        body = {
            "data": {
                "color": "green",
                "size": "micro"
            },
            "name": "Mini object"
        }
    with allure.step('Осуществление PUT-запроса для изменения объекта'):
        resp = update_entire_object(get_new_id, body)
    with allure.step('Проверка кода ответа'):
        assert resp.status_code == 200, f'Ошибка при обновлении объекта. Статус: {resp.status_code}'
    with allure.step('Проверка имени объекта'):
        assert resp.json()['name'] == 'Mini object', f'Неверное имя объекта {resp.json()["name"]}'


@allure.title('Тестирование частичного изменения объекта')
@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Update object')
@allure.story('Positive test')
@pytest.mark.medium
def test_positive_update_part_object(get_new_id):
    with allure.step('Подготовка данных'):
        body = {
            "name": "Micro object"
        }
    with allure.step('Осуществление PATCH-запроса для изменения объекта'):
        resp = update_part_object(get_new_id, body)
    with allure.step('Проверка кода ответа'):
        assert resp.status_code == 200, f'Ошибка при обновлении объекта. Статус: {resp.status_code}'
    with allure.step('Проверка имени объекта'):
        assert resp.json()['name'] == 'Micro object', f'Неверное имя объекта {resp.json()["name"]}'


@allure.title('Тестирование удаления объекта')
@allure.severity(allure.severity_level.MINOR)
@allure.feature('Delete object')
@allure.story('Positive test')
def test_positive_delete_object(get_new_id):
    with allure.step('Осуществление запроса DELETE для удаления объекта'):
        resp = delete_object(get_new_id)
    with allure.step('Проверка кода ответа'):
        assert resp.status_code == 200, f'Ошибка при удалении объекта. Статус: {resp.status_code}'
    with allure.step('Проверка сообщения об успешном удалении'):
        assert resp.text == f'Object with id {get_new_id} successfully deleted', f'Неверный id объекта {get_new_id}'


@allure.title('Тестирование чтения объекта')
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature('Get object')
@allure.story('Positive test')
def test_positive_get_object(get_new_id):
    with allure.step('Осуществление GET-запроса для получения объекта'):
        resp = get_object(get_new_id)
    with allure.step('Проверка кода ответа'):
        assert resp.status_code == 200, f'Ошибка при получении существующего объекта. Статус: {resp.status_code}'


@allure.title('Тестирование попытки создания объекта с некорректными данными')
@allure.severity(allure.severity_level.MINOR)
@allure.feature('Create object')
@allure.story('Negative test')
def test_negative_add_object():
    with allure.step('Подготовка данных'):
        body = {}
    with allure.step('Осуществление POST-запроса для создания объекта'):
        resp = add_object(body)
    with allure.step('Проверка кода ответа'):
        assert resp.status_code == 400, \
            f'Неверный статус при добавлении некорректного объекта. Статус: {resp.status_code}'


@allure.title('Тестирование попытки полного изменения объекта некорректными данными')
@allure.severity(allure.severity_level.MINOR)
@allure.feature('Update object')
@allure.story('Negative test')
def test_negative_update_entire_object(get_new_id):
    with allure.step('Подготовка данных'):
        body = {
            "atad": {
                "color": "green",
                "size": "micro"
            },
            "eman": "Mini object"
        }
    with allure.step('Осуществление PUT-запроса для изменения объекта'):
        resp = update_entire_object(get_new_id, body)
    with allure.step('Проверка кода ответа'):
        assert resp.status_code == 400, \
            f'Неверный статус при попытке обновления объекта некорректными данными. Статус: {resp.status_code}'


@allure.title('Тестирование попытки частичного изменения объекта некорректными данными')
@allure.severity(allure.severity_level.MINOR)
@allure.feature('Update object')
@allure.story('Negative test')
def test_negative_update_part_object(get_new_id):
    with allure.step('Подготовка данных'):
        body = {
            "eman": "Mini object"
        }
    with allure.step('Осуществление PATCH-запроса для изменения объекта'):
        resp = update_part_object(get_new_id, body)
    with allure.step('Проверка кода ответа'):
        assert resp.status_code == 400, \
            f'Неверный статус при попытке обновления объекта некорректными данными. Статус: {resp.status_code}'


@allure.title('Тестирование попытки удаления несуществующего объекта')
@allure.severity(allure.severity_level.MINOR)
@allure.feature('Delete object')
@allure.story('Negative test')
def test_negative_delete_object():
    with allure.step('Осуществление запроса DELETE для удаления объекта'):
        resp = delete_object(999999)
    with allure.step('Проверка кода ответа'):
        assert resp.status_code == 404, f'Ошибка при удалении несуществующего объекта. Статус: {resp.status_code}'


@allure.title('Тестирование попытки получения несуществующего объекта')
@allure.severity(allure.severity_level.MINOR)
@allure.feature('Get object')
@allure.story('Negative test')
def test_negative_get_object():
    with allure.step('Осуществление GET-запроса для получения объекта'):
        resp = get_object(999999)
    with allure.step('Проверка кода ответа'):
        assert resp.status_code == 404, f'Ошибка при получении несуществующего объекта. Статус: {resp.status_code}'
