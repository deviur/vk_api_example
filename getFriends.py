#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO Получить список друзей из ВК
"""
Консольное приложение Python 3.5

Простой пример получения списка друзей из ВК
Предполагается использовать в качестве модуля для других примеров.
"""

import sys
import vk
import auth_vk

V = '9.95'

session = auth_vk.auth_vk_token()
api = vk.API(session, v=V)


def get_friends(user_id):
    return api.friends.get(user_id=user_id)['items']


def main():

    if len(sys.argv)>1:
        user_id = sys.argv[1]
    else:
        user_id = 0 # ID пользователя, который авторизовался в программе

    friends = get_friends(user_id)

    print('user_id')           # Выводим заголовок
    for friend in friends:
        print(friend)


if __name__ == "__main__":
    main()
