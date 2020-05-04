import requests
from api import Method, ObjectType, make_request


def test_is_liked_success_like_set(post, like):
    result, result_status_code = make_request(method=Method.likes_is_liked,
                                              type=ObjectType.post,
                                              item_id=post)

    assert result_status_code == requests.codes.ok
    assert 'error' not in result
    assert result['response']['liked'] == 1


def test_is_liked_success_with_deleted_post(deleted_post):
    result, result_status_code = make_request(method=Method.likes_is_liked,
                                              type=ObjectType.post,
                                              item_id=deleted_post)

    assert result_status_code == requests.codes.ok
    assert result['response']['liked'] == 0


def test_is_liked_error_without_item_id(post):
    result, result_status_code = make_request(method=Method.likes_is_liked, type=ObjectType.post)

    assert result_status_code == requests.codes.ok
    assert result['error']['error_code'] == 100, 'Expected error "object was not found"'
