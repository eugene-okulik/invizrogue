import requests
import pytest


@pytest.fixture
def get_new_id():
    body = {
        "data": {
            "color": "test",
            "size": "test"
        },
        "name": "New test object"
    }
    response = add_object(body).json()
    yield response['id']
    delete_object(response['id'])


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


@pytest.mark.critical
@pytest.mark.parametrize('color, size, name', [
    ("red", "nano", "Nano"),
    ("green", "micro", "Micro"),
    ("blue", "mini", "Mini")])
def test_positive_add_object(session_info, color, size, name):
    body = {
        "data": {
            "color": color,
            "size": size
        },
        "name": name
    }
    resp = add_object(body)
    assert resp.status_code == 200, f'Ошибка при добавлении объекта. Статус: {resp.status_code}'
    assert resp.json()['name'] == name, f'Неверное имя объекта {resp.json()["name"]}'


def test_positive_update_entire_object(get_new_id):
    body = {
        "data": {
            "color": "green",
            "size": "micro"
        },
        "name": "Mini object"
    }
    resp = update_entire_object(get_new_id, body)
    assert resp.status_code == 200, f'Ошибка при обновлении объекта. Статус: {resp.status_code}'
    assert resp.json()['name'] == 'Mini object', f'Неверное имя объекта {resp.json()["name"]}'


@pytest.mark.medium
def test_positive_update_part_object(get_new_id):
    body = {
        "name": "Micro object"
    }
    resp = update_part_object(get_new_id, body)
    assert resp.status_code == 200, f'Ошибка при обновлении объекта. Статус: {resp.status_code}'
    assert resp.json()['name'] == 'Micro object', f'Неверное имя объекта {resp.json()["name"]}'


def test_positive_delete_object(get_new_id):
    resp = delete_object(get_new_id)
    assert resp.status_code == 200, f'Ошибка при удалении объекта. Статус: {resp.status_code}'
    assert resp.text == f'Object with id {get_new_id} successfully deleted', f'Неверный id объекта {get_new_id}'


def test_positive_get_object(get_new_id):
    resp = get_object(get_new_id)
    assert resp.status_code == 200, f'Ошибка при получении существующего объекта. Статус: {resp.status_code}'


def test_negative_add_object():
    body = {}
    resp = add_object(body)
    assert resp.status_code == 400, f'Неверный статус при добавлении некорректного объекта. Статус: {resp.status_code}'


def test_negative_update_entire_object(get_new_id):
    body = {
        "atad": {
            "color": "green",
            "size": "micro"
        },
        "eman": "Mini object"
    }
    resp = update_entire_object(get_new_id, body)
    assert resp.status_code == 400, \
        f'Неверный статус при попытке обновления объекта некорректными данными. Статус: {resp.status_code}'


def test_negative_update_part_object(get_new_id):
    body = {
        "eman": "Mini object"
    }
    resp = update_part_object(get_new_id, body)
    assert resp.status_code == 400, \
        f'Неверный статус при попытке обновления объекта некорректными данными. Статус: {resp.status_code}'


def test_negative_delete_object():
    resp = delete_object(999999)
    assert resp.status_code == 404, f'Ошибка при удалении несуществующего объекта. Статус: {resp.status_code}'


def test_negative_get_object():
    resp = get_object(999999)
    assert resp.status_code == 404, f'Ошибка при получении несуществующего объекта. Статус: {resp.status_code}'
