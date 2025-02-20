import pytest

POSITIVE_TEST_DATA = [
    {"data": {"color": "red", "size": "nano"}, "name": "Nano"},
    {"data": {"color": "green", "size": "micro"}, "name": "Micro"},
    {"data": {"color": "blue", "size": "mini"}, "name": "Mini"}
]

NEGATIVE_TEST_DATA = [
    {"dta": {"size": "micro"}, "name": "Micro"},
    {"name": "Nano"},
    {"atad": {"color": "red", "size": "nano"}, "name": "Nano"},
    {"data": {"roloc": "green", "size": "micro"}, "nme": "Micro"},
    {"data": {"color": "blue", "size": "mini"}}
]


@pytest.mark.critical
@pytest.mark.parametrize('data', POSITIVE_TEST_DATA)
def test_positive_add_object(creating, clean, data):
    creating.new_object(clean, payload=data)
    creating.check_status_code(200)
    creating.check_response_name_is_correct(data['name'])
    creating.check_response_color_is_correct(data['data']['color'])
    creating.check_response_size_is_correct(data['data']['size'])


@pytest.mark.critical
@pytest.mark.parametrize('data', NEGATIVE_TEST_DATA)
def test_negative_add_object(creating, clean, data):
    creating.new_object(clean, payload=data)
    creating.check_status_code(400)
