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
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    ).json()
    yield response['id']
    requests.delete(f"http://167.172.172.115:52353/object/{response['id']}")
