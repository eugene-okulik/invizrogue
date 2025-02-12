import requests


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


body = {}
resp = add_object(body)
assert resp.status_code == 400, f'Неверный статус при добавлении некорректного объекта. Статус: {resp.status_code}'

body = {
    "data": {
        "color": "red-green",
        "size": "nano"
    },
    "name": "Nano object"
}
resp = add_object(body)
print(f'Добавленный объект:\n{resp.json()}\n')
assert resp.status_code == 200, f'Ошибка при добавлении объекта. Статус: {resp.status_code}'
assert resp.json()['name'] == 'Nano object', f'Неверное имя объекта {resp.json()["name"]}'
object_id = resp.json()['id']

body = {
    "atad": {
        "color": "green",
        "size": "micro"
    },
    "eman": "Mini object"
}
resp = update_entire_object(object_id, body)
assert resp.status_code == 400, \
    f'Неверный статус при попытке обновления объекта некорректными данными. Статус: {resp.status_code}'


body = {
    "data": {
        "color": "green",
        "size": "micro"
    },
    "name": "Mini object"
}
resp = update_entire_object(object_id, body)
print(f'Полностью обновлённый объект:\n{resp.json()}\n')
assert resp.status_code == 200, f'Ошибка при обновлении объекта. Статус: {resp.status_code}'
assert resp.json()['name'] == 'Mini object', f'Неверное имя объекта {resp.json()["name"]}'

body = {
    "eman": "Mini object"
}
resp = update_part_object(object_id, body)
assert resp.status_code == 400, \
    f'Неверный статус при попытке обновления объекта некорректными данными. Статус: {resp.status_code}'

body = {
    "name": "Micro object"
}
resp = update_part_object(object_id, body)
print(f'Частично обновлённый объект:\n{resp.json()}\n')
assert resp.status_code == 200, f'Ошибка при обновлении объекта. Статус: {resp.status_code}'
assert resp.json()['name'] == 'Micro object', f'Неверное имя объекта {resp.json()["name"]}'

resp = get_object(object_id)
print(f'Сообщение о наличии объекта:\n{resp.json()}\n')
assert resp.status_code == 200, f'Ошибка при получении существующего объекта. Статус: {resp.status_code}'

resp = delete_object(999999)
assert resp.status_code == 404, f'Ошибка при удалении несуществующего объекта. Статус: {resp.status_code}'

resp = delete_object(object_id)
print(f'Сообщение об удалении объекта:\n{resp.text}\n')
assert resp.status_code == 200, f'Ошибка при удалении объекта. Статус: {resp.status_code}'
assert resp.text == f'Object with id {object_id} successfully deleted', f'Неверный id объекта {object_id}'

resp = get_object(object_id)
print(f'Сообщение об отсутствии объекта:\n{resp.text}\n')
assert resp.status_code == 404, f'Ошибка при получении несуществующего объекта. Статус: {resp.status_code}'
