#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO Получить ссылки на профили пользователей
"""
Консольное приложение Python 3.5

Задача такая:
Есть две группы ВК. Нужно получить список пользователей из нашего региона. Москва и Московская область.

Алкоритм следующий:
1. Получаем список пользователей первой группы с полями fields=city,country
2. Удаляем из списка пользователей не из Москвы или Московской области
3. Выводим список на экран/в файл

"""

import vk
import auth_vk
import getMembers

V = '9.95'
USER_ID = '0'
GROUP_IDS = [157262974, 111105089]
CITY_ID = 1

session = auth_vk.auth_vk_token()
api = vk.API(session, v=V)


def main():

    members_from = []

    # Получаем ID пользователей первой группы
    members = getMembers.get_all_members(GROUP_IDS[0], "city,country")

    for member in members:
        if 'city' in member and member['city']['id'] == CITY_ID:
            members_from.append(member)

    print(members_from)


if __name__ == "__main__":
    main()
