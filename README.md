# vk_api_example 2.0
## Пример использования VK API в Python-е
Файлы из этого пакета представляют собой набор консольных утилит на Python-е, каждая из этих утилит дублирует свой метод VK API. Любой из этих файлов можно использовать в качетве модуля для Ваших программ. Соответствующие примеры как это делается будут даны ниже.
### Зависимости
0. Python 3.7
0. vk

Перед использванием установите зависимости командой:
```bash
pip3 install -r requirements.txt --local
```
## Список файлов с описанием
0. **auth_vk.py** - служит для авторизации приложения в ВК с помощью пароля или токена.
0. **get_cities.py** - возвращает список городов. Реализует метод VK API (https://vk.com/dev/database.getCities). 
0. **get_members.py** - возвращает список учаснников группы. Реализует метод VK API groups.getMembers (https://vk.com/dev/groups.getMembers).
0. **groups_get.py** - возвращает список групп указанного пользователя. Реализует метод VK API groups.get (https://vk.com/dev/groups.get).
0. **groups_search.py** - осуществляет поиск сообществ по заданной подстроке. Реализует метод VK API groups.search (https://vk.com/dev/groups.search). 
0. **json2csv.py** - конвертирует структуру json в csv.
0. **friends_get.py** - Возвращает список идентификаторов друзей пользователя или расширенную информацию о них. Реализует метод VK API friends.get (https://vk.com/dev/friends.get).
