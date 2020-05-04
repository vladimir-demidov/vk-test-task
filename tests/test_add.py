import requests
from api import Method, ObjectType, make_request


def test_add_success(like):
    assert like['likes'] == 1


def test_add_error_without_post(deleted_post):
    result, result_status_code = make_request(method=Method.likes_add,
                                              type=ObjectType.post,
                                              item_id=deleted_post)

    assert result_status_code == requests.codes.ok
    assert result['error']['error_code'] == 100, 'Expected error "object was not found"'
