import pytest

NEGATIVE_TEST_DATA = [9999999, "abc", "!"]


def test_positive_get_existing_object(getting):
    getting.get_object(1)
    getting.check_status_code(200)

def test_positive_get_object(getting, get_id):
    getting.get_object(get_id)
    getting.check_status_code(200)

@pytest.mark.low
@pytest.mark.parametrize("neg_id", NEGATIVE_TEST_DATA)
def test_negative_get_object(getting, neg_id):
    getting.get_object(neg_id)
    getting.check_status_code(404)
