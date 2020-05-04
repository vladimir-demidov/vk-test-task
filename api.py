import requests
import config
from enum import Enum

BASE_VK_URL = "https://api.vk.com/method/"
API_VERSION = "5.103"


class ObjectType(str, Enum):
    post = "post"


class Method(str, Enum):
    likes_add = 'likes.add'
    likes_delete = 'likes.delete'
    likes_is_liked = 'likes.isLiked'
    likes_get_list = 'likes.getList'
    wall_post = 'wall.post'
    wall_delete = 'wall.delete'


# Создаём функцию, которая внутри себя собирает url нужного нам метода vk api и делает на него get запрос.
# Функция возвращает ответ в формате .json и статус код ответа.

def make_request(*, method: Method, **kwargs):
    params = {'owner_id': config.owner_id, 'access_token': config.access_token, 'v': API_VERSION, **kwargs}
    resp = requests.get(f"{BASE_VK_URL}/{method.value}", params=params)
    result = resp.json()
    code = resp.status_code

    return result, code
