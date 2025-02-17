import pytest

POSITIVE_FULL_TEST_DATA = [
    {"data": {"color": "red", "size": "nano"}, "name": "Nano"},
    {"data": {"color": "green", "size": "micro"}, "name": "Micro"},
    {"data": {"color": "blue", "size": "mini"}, "name": "Mini"}
]

NEGATIVE_FULL_TEST_DATA = [
    {"d": {"color": "red", "size": "nano"}, "name": "Nano"},
    {"data": {"color": "green", "size": "micro"}, "n": "Micro"},
    {"name": "Mini"}
]

POSITIVE_PART_TEST_DATA = [
    {"name": "New part name"},
    {"data": {"color": "yellow", "size": "maxi"}},
    {"data": {}}
]

NEGATIVE_PART_TEST_DATA = [
    {"nme": "New part name"},
    {"dat": {"color": "yellow", "size": "maxi"}},
    {"string": "{}"}
]

@pytest.mark.parametrize("data", POSITIVE_FULL_TEST_DATA)
def test_positive_update_entire_object(updating, get_id, data):
    updating.upd_entire_object(get_id, data)
    updating.check_status_code(200)
    updating.check_object_has_been_updated(data)

@pytest.mark.parametrize("data", NEGATIVE_FULL_TEST_DATA)
def test_negative_update_entire_object(updating, get_id, data):
    updating.upd_entire_object(get_id, data)
    updating.check_status_code(400)
    updating.check_object_has_not_been_updated(get_id)

@pytest.mark.medium
@pytest.mark.parametrize("data", POSITIVE_PART_TEST_DATA)
def test_positive_update_part_object(updating, get_id, data):
    updating.upd_part_object(get_id, data)
    updating.check_status_code(200)
    updating.check_object_has_been_updated(data)

@pytest.mark.parametrize("data", NEGATIVE_PART_TEST_DATA)
def test_negative_update_part_object(updating, get_id, data):
    updating.upd_entire_object(get_id, data)
    updating.check_status_code(400)
    updating.check_object_has_not_been_updated(get_id)
