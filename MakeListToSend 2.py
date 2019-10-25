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
    #     print("""<!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <title>Список для рассылки сообщений</title>
    # </head>
    # <body>
    # <h1>Список для рассылки сообшщений</h1>
    # <h2>Список попечителей из Москвы</h2><table>""")
    #
    #     members_1 = getMembers.get_all_members_from(GROUP_IDS[0], 1)
    #     num = 1
    #     for member in members_1:
    #         print(
    #             "<tr><td>" + str(num) + "</td><td>" + member['first_name'] + "</td><td>" + member['city']['title'] +
    #             "</td><td><a href=https://vk.com/write" + str(member['id']) +
    #             " target='blank'>Написать сообщение...</a></td></tr>")
    #         num += 1
    #
    #     print("</table><h2>Список участников группы из Москвы</h2><table>")
    #
    #     members_2 = getMembers.get_all_members_from(GROUP_IDS[1], 1)
    #
    #     # Убираем из списка друзей попечителей друзей. У нас получается список кому отправлять сообщения
    #     for member in members_1:
    #         if member in members_2:
    #             members_2.remove(member)
    #
    #     num = 1
    #     for member in members_2:
    #         print(
    #             "<tr><td>" + str(num) + "</td><td>" + member['first_name'] + "</td><td>" + member['city']['title'] +
    #             "</td><td><a href=https://vk.com/write" + str(member['id']) +
    #             " target='blank'>Написать сообщение...</a></td></tr>")
    #         num += 1
    #
    #     print("</table></body></html>")

    protectors = getMembers.get_all_members_3(GROUP_IDS[0])
    members = getMembers.get_all_members_3(GROUP_IDS[1])
    print("id;first_name;last_name;city;url")
    num = 1
    for member in members:
        if member in protectors:
            continue
        if "city" in member:
            city = member["city"]["title"]
        else:
            city = "-"
        print(str(member["id"]) + ";" +
              member["first_name"] + ";" +
              member["last_name"] + ";" +
              city + ";" +
              "https://vk.com/write" + str(member['id']))
        num += 1
    print(str(num))


if __name__ == "__main__":
    main()
