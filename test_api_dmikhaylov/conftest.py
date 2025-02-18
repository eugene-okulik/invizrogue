import pytest
import requests
from endpoints.commons import Commons
from endpoints.get_object import GetObject
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.update_object import UpdateObject


@pytest.fixture
def clean():
    objects = []

    def add_object_id(obj_id):
        objects.append(obj_id)
    yield add_object_id
    for object_id in objects:
        requests.delete(f"{Commons.url}/{object_id}")


@pytest.fixture
def get_id():
    payload = {
        "data": {
            "color": "test",
            "size": "test"
        },
        "name": "New test object"
    }
    response = requests.post(
        Commons.url,
        json=payload,
        headers=Commons.headers
    ).json()
    yield response['id']
    requests.delete(f"{Commons.url}/{response['id']}")


@pytest.fixture
def del_id():
    payload = {
        "data": {
            "color": "test",
            "size": "test"
        },
        "name": "New test object"
    }
    response = requests.post(
        Commons.url,
        json=payload,
        headers=Commons.headers
    ).json()
    yield response['id']


@pytest.fixture
def creating():
    return CreateObject()


@pytest.fixture
def updating():
    return UpdateObject()


@pytest.fixture
def deleting():
    return DeleteObject()


@pytest.fixture
def getting():
    return GetObject()
