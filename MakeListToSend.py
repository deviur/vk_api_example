#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO Получить список друзей из ВК
"""
Консольное приложение Python 3.5

Простой пример получения списка друзей из ВК
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
    friends = getFriends.get_friends(USER_ID)
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
