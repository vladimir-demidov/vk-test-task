## Задача:

С помощью модуля Pytest в Pyton3 протестировать следующие методы для работы с отметками "Мне нравится" из секции API VK Likes:

1. likes.add  https://vk.com/dev/likes.add
2. likes.delete https://vk.com/dev/likes.delete
3. likes.getList https://vk.com/dev/likes.getList
4. likes.isLiked https://vk.com/dev/likes.isLiked

Тесты проверяют работу методов на стене пользователя в посте, который создаётся с помощью метода wall.post https://vk.com/dev/wall.post 

Так как мы используем приватное апи, для корректной работы тестов требуется получить access_token  https://vk.com/dev/access_token и owner_id. Для успешного запуска тестов запишите ваши access_token и owner_id в соответствующие переменные файла config.py

Тесты запускаются с помощью команды pytest из терминала, находясь в директории проекта vk_test_task_project

##  Список тестов:

|                  Тест                   |     Метод     |                           Описание                           | Тип      | Результат |
| :-------------------------------------: | :-----------: | :----------------------------------------------------------: | -------- | --------- |
|            test_add_success             |   likes.add   | создаёт пост, ставит на нём лайк и проверяет наличие лайка у поста | Positive | PASSED    |
|       test_add_error_without_post       |   likes.add   | создаёт пост и удаляет его, затем пытается на удалённый  пост поставить лайк, проверяет, что в результате ошибка | Negative | PASSED    |
|           test_delete_success           | likes.delete  | ставит лайк на посте, проверяет наличие лайка, удаляет лайк, проверяет отсутствие лайка у поста | Positive | PASSED    |
|     test_delete_error_without_likes     | likes.delete  | пытается удалить лайк у поста без лайка, проверяет, что в результате ошибка | Negative | PASSED    |
|     test_delete_error_without_post      | likes.delete  | создаёт пост, удаляет его, пытается удалить лайк,  проверяет, что в результате ошибка | Negative | PASSED    |
|     test_is_liked_success_like_set      | likes.isLiked | ставит лайк на посте, проверяет, что owner_id поставил лайк  | Positive | PASSED    |
| test_is_liked_success_with_deleted_post | likes.isLiked | создаёт пост, удаляет его, проверяет, что у удалённого поста не было лайка от owner_id | Positive | PASSED    |
|   test_is_liked_error_without_item_id   | likes.isLiked | пытается проверить наличие лайка у незаданного объекта, проверяет, что в результате ошибка | Negative | PASSED    |
|          test_get_list_success          | likes.getList | ставит лайк на посте и получает список id пользователей, поставивших лайк. Проверяет, есть ли лайк от owner_id | Positive | PASSED    |
|   test_get_list_error_without_item_id   | likes.getList | пытается получить список id пользователей, поставивших лайк на незаданном объекте. Проверяет, что в результате ошибка | Negative | PASSED    |

