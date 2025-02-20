import pytest
from endpoints.get_object import GetObject
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.update_object import UpdateObject


@pytest.fixture
def clean(deleting):
    objects = []

    def add_object_id(obj_id):
        objects.append(obj_id)
    yield add_object_id
    for object_id in objects:
        deleting.del_object(object_id)


@pytest.fixture
def get_id(creating, clean):
    payload = {
        "data": {
            "color": "test",
            "size": "test"
        },
        "name": "New test object"
    }
    yield creating.new_object(clean, payload).json()['id']


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
