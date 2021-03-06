#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO Получить список друзей из ВК
"""
Консольное приложение Python 3.5

Пример построения списка в формате html-файла для отправки сообщений друзьям.

Требуется отправить сообщения тем друзьям, которые не состоят в клубе попечителей.
Программа формирует список таких друзей и ссылки для отправки сообщений.

"""

import vk
import auth_vk
import getFriends
import getMembers

V = '9.95'
USER_ID = '0'
GROUP_ID = '157262974'

session = auth_vk.auth_vk_token()
api = vk.API(session, v=V)


def main():
    # Получаем ID списки друзей и друзей попечителей Школы Граня
    friends = getFriends.get_friends_from(USER_ID, 1)
    members = getMembers.get_members(GROUP_ID)  # Попечители школы, те, что в друзьях

    # Убираем из списка друзей попечителей друзей. У нас получается список кому отправлять сообщения
    for member in members:
        if member in friends:
            friends.remove(member)

    print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ссылки для сообщений</title>
</head>
<body>
<h1>Ссылки для рассылки сообщений</h1>""")
    n = 1
    for friend in friends:
        print("<p>" + str(n) + ". <a href=https://vk.com/write" + str(friend) + " target='blank'>"
              + "https://vk.com/write" + str(friend) + "</a></p>")
        n += 1

    print("""</body>
</html>""")


if __name__ == '__main__':
    main()
