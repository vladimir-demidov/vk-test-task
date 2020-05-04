import requests
import config
from api import Method, ObjectType, make_request


def test_get_list_success(post, like):
    result, result_status_code = make_request(method=Method.likes_get_list,
                                              type=ObjectType.post,
                                              item_id=post)

    assert result['response']['count'] == 1
    assert result['response']['items'] == [config.owner_id]


def test_get_list_success_with_deleted_post(deleted_post):
    result, result_status_code = make_request(method=Method.likes_get_list,
                                              type=ObjectType.post,
                                              item_id=deleted_post)

    assert result['response']['count'] == 0
    assert result['response']['items'] == []


def test_get_list_error_without_item_id(post):
    result, result_status_code = make_request(method=Method.likes_get_list, type=ObjectType.post)

    assert result_status_code == requests.codes.ok
    assert result['error']['error_code'] == 100, 'Expected error "object was not found"'
