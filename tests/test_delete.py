import requests
from api import Method, ObjectType, make_request


def test_delete_success(post, like):
    assert like['likes'] == 1

    result, result_status_code = make_request(method=Method.likes_delete,
                                              type=ObjectType.post,
                                              item_id=post)

    assert result_status_code == requests.codes.ok
    assert 'error' not in result
    assert result['response']['likes'] == 0


def test_delete_error_without_likes(post):
    result, result_status_code = make_request(method=Method.likes_delete,
                                              type=ObjectType.post,
                                              item_id=post)

    assert result_status_code == requests.codes.ok
    assert result['error']['error_code'] == 15, 'Expected error "Access denied"'


def test_delete_error_without_post(deleted_post):  
    result, result_status_code = make_request(method=Method.likes_delete, 
                                              type=ObjectType.post,
                                              item_id=deleted_post)

    assert result_status_code == requests.codes.ok
    assert result['error']['error_code'] == 100, 'Expected error "object was not found"'
