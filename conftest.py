import pytest
import requests
import time

from api import Method, ObjectType, make_request


@pytest.fixture(autouse=True)
def avoid_too_many_requests():
    time.sleep(1)


@pytest.fixture(scope="session")
def post():
    # Create post.
    result, result_status_code = make_request(method=Method.wall_post, message="test")

    assert result_status_code == requests.codes.ok
    assert 'error' not in result

    post_id = result['response']['post_id']
    yield post_id
    # Delete post.
    result, result_status_code = make_request(method=Method.wall_delete, post_id=post_id)

    assert result_status_code == requests.codes.ok
    assert 'error' not in result


@pytest.fixture
def like(post):
    # Add like.
    result, result_status_code = make_request(method=Method.likes_add, type=ObjectType.post, item_id=post)

    assert result_status_code == requests.codes.ok
    assert 'error' not in result

    yield result['response']
    # Delete like.
    result, result_status_code = make_request(method=Method.likes_delete, type=ObjectType.post, item_id=post)

    assert result_status_code == requests.codes.ok
    assert 'error' not in result

# Создаём фикстуру, чтобы апперировать с невалидным post_id, на который нельзя поставить лайк.

@pytest.fixture
def deleted_post():
    # Create post
    result, result_status_code = make_request(method=Method.wall_post, message="test")

    assert result_status_code == requests.codes.ok
    assert 'error' not in result

    post_id = result['response']['post_id']
    # Delete post
    result, result_status_code = make_request(method=Method.wall_delete, post_id=post_id)

    assert result_status_code == requests.codes.ok
    assert 'error' not in result

    return post_id
