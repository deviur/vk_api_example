#!/usr/bin/env python
# -*- coding: utf-8 -*-

#TODO Получить список городов по ключевому слову в ВК
"""
Консольное приложение Python 3.5

Простой пример применения VK API для получения списка городов по ключевому слову.
Выдаёт список городов по ключевому слову в консоль в формате csv.
На входе будет ключевое слово keyword, а на выходе список городов в базе ВК
"""

VERSION = '1.0.00 (21.09.2019)'
AUTHOR = 'Deviur (https://github.com/deviur)'
v ='9.95'

import sys
import vk
import auth_vk


def main():
    INFO = '''
    Программа проверки авторизации в ВК. 
    Используется всеми программами пакета vk_api_example в качестве библиотеки.
    Version: %s
    Author: %s

    -------- Результаты ------
    ''' % (VERSION, AUTHOR)

    print(INFO)

    if len(sys.argv)>1:
        keyword = sys.argv[1]
    else:
        keyword = "Балашиха"

    session = auth_vk.auth_vk_token()
    api = vk.API(session, v=v)

    # Запрос списка городов России (Cities) по ключевому слову
    Cities = api.database.getCities(country_id=1, q=keyword)['items']

    #Выводим шапку списка городов
    print("id; title")

    # Выводим список городов по запросу на экран
    for city in Cities:
        print(city['id'], ";", city['title'])


if __name__ == "__main__":
    main()
