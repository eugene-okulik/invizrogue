import pytest

@pytest.mark.critical
def test_positive_delete_object(deleting, del_id):
    deleting.del_object(del_id)
    deleting.check_status_code(200)
    deleting.check_response_message_is_correct()

@pytest.mark.low
def test_negative_delete_object(deleting):
    deleting.del_object(999999999)
    deleting.check_status_code(404)
