# TODO ПРИМЕР РАБОТЫ С VK API

""" Консольное приложения на Python 3.5

Простой пример, как использовать VK API для поиска групп в городе по ключевому запросу.
Результат выводится в файлы csv.

Параметры для программы задаются внутри кода:
    access_token - нужно предварительно запросить. Ниже указан запрос, который нужно вставить в адресную строку браузера
    v - версия VK API
    keyword_city - ключевое слово для города, в котором требуется найти группы
    keywords_groups - ключевые слова, по которым требуется найти группы

В примере используются следующие методы VK API:

    database.getCities - https://vk.com/dev/database.getCities
    (Используется для получения списка городов по ключевому слову)

    groups.search - https://vk.com/dev/groups.search
    (Используется для получения списка id групп соответствующих запросу.
    Группы сортируются по отношению дневной посещаемости к количеству пользователей.)

    groups.getById - https://vk.com/dev/groups.getById
    (Используется для получения дополнительной информации из групп
"""

import vk
import csv

# Как получить access_token:
# https://oauth.vk.com/authorize?client_id=6478436&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.95

# Параметры:
access_token = '3716eefa82841782e8d1093e01fb1eb89a00eaf089e849172a169d073b8e16565ab38edb43fe41d68dbad'
v = '5.95'
keyword_city = "Балашиха"
keywords_groups = ['ремонт', 'потолки', 'мебель', 'двери']

# Подключение к VK API
session = vk.Session(access_token=access_token)
api = vk.API(session, v=v)

# Запрос списка городов России (Cities) по ключевому слову
Cities = api.database.getCities(country_id=1, q=keyword_city)['items']

# Выводим список городов по запросу на экран
for city in Cities:
    print(city['id'], "\t", city['region'], city['title'], city['area'])

# Поиск групп будет осуществляться только по первому городу из списка
city_id = Cities[0]['id']
city_name = Cities[0]['title']

# Начинамем поиск по каждому ключевому слову по очереди
for keyword in keywords_groups:

    # Получаем список IDs групп города удовлетворяющих ключевому слову
    group_ids = [g['id'] for g in api.groups.search(city_id=city_id, q=keyword, sort=2, count=500)['items']]

    # Получаем список групп города удовлетворяющих ключевому слову
    Groups = api.groups.getById(fields='members_count,contacts', group_ids=group_ids)

    # Создаём csv-файл с группами 'Город - ключевое_слово.csv'
    filename = city_name + " - " + keyword + ".csv"
    f = open(filename, 'w')

    # Задаём заголовок csv-файла
    fieldnames = ['sort2', 'id', 'type', 'is_closed', 'screen_name', 'name', 'members_count', 'contacts', 'photo_50', 'photo_100', 'photo_200']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    # Сохраняем список групп в соответствующий запросу csv-файл
    i = 1
    for group in Groups:
        # Сохраняем порядок сортировки по отношению дневной посещаемости к количеству пользователей
        group['sort2'] = i
        writer.writerow(group)
        i+=1

    #print(Groups)
