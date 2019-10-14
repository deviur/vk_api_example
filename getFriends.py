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


def get_friends_from(user_id, city_id):
    friends_from = []
    friends = api.friends.get(user_id=user_id, fields='city')['items']
    for friend in friends:
        if 'city' in friend and friend['city']['id'] == city_id:
            friends_from.append(friend['id'])
    return friends_from


def main():

    if len(sys.argv)>1:
        user_id = sys.argv[1]
    else:
        user_id = 0 # ID пользователя, который авторизовался в программе

    friends = get_friends(user_id)

    print('user_id')           # Выводим заголовок
    for friend in friends:
        print(friend)

    friends = get_friends_from(user_id, 1)
    print('user_id')           # Выводим заголовок
    for friend in friends:
        print(friend)
    pass


if __name__ == "__main__":
    main()
