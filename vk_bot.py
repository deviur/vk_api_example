#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os

from auth_vk import *

APP_ID = '6478436'
V = 9.85
# LIST_TO_SEND = ['deleted', 'relation', 'status', 'deactivated']
INCLUDE = ['deleted', 'relation']    # Свойства пользователя, которые отслеживать
EXCLUDE = ['track_code', 'online', 'status_audio']  # Свойства пользователя, которые не отслеживать
USER_ID = 133147577
REPORT_TIME = datetime.datetime.now()

VERSION = '1.0.00 (08.01.2020)'
AUTHOR = 'Deviur (https://github.com/deviur)'


def main():
    print("\n", REPORT_TIME)
    print(os.getcwd())

    # Авторизация в ВК
    session = auth_vk_token()

    # Подключение к API
    api = vk.API(session, v=V)

    # # Проверка, удалась ли авторизация
    # try:
    #     user = api.users.get()[0]
    # except vk.exceptions.VkAPIError:
    #     print('Авторизация не удалась. Повторите попытку.\n')
    #     login_by_password()
    # else:
    #     print("Приветствую, {}!".format(user['first_name']))
    #     print("Авторизация прошла успешно!")

    friends_to_save = api.friends.get(user_id=0, fields='sex, bdate, city, relation, status')

    try:  # Проверяем наличие файла со списком друзей
        file = open("friends.ini", 'r')
    except IOError:
        file = open("friends.ini", 'w')
        file.writelines(str(friends_to_save) + '\n')
        return

    # Загружаем список друзей за предыдущий период из файла в словарь
    # file = open("friends.ini", 'r')
    old_friends = eval(file.read())

    # Создаём словарь текущих друзей
    keys, items = [f['id'] for f in friends_to_save['items']], [f for f in friends_to_save['items']]
    friends = dict(zip(keys, items))

    # Создаём словарь друзей предыдущего периода
    keys, items = [f['id'] for f in old_friends['items']], [f for f in old_friends['items']]
    old_friends = dict(zip(keys, items))

    deleted = [f for f in old_friends.keys() if not(f in friends.keys())]
    added = [f for f in friends.keys() if f not in old_friends.keys()]
    changed = []
    for id in friends.keys():
        if id not in added:
            for item in EXCLUDE:
                friends[id].pop(item, None)
                old_friends[id].pop(item, None)

            if friends[id] != old_friends[id]:
                changed.append(id)

    message = ''
    if len(deleted) > 0 and 'deleted' in INCLUDE:
        message += '\nПользовател(ь/и) удалил(ся/ись):\n'
        for d in deleted:
            message += f'http://vk.com/id{d}\n'

    print(deleted)
    print(added)
    print(changed)

    # Печать изменений
    message += '\nПользовател(ь/и) внес(ли) изменения:\n'
    for c in changed:
        print(f"Было:  {old_friends[c]}")
        print(f"Стало: {friends[c]}")
        for key in friends[c]:
            if key not in old_friends[c]:
                # print("Было:  ", key, ":  -")
                # print("Стало: ", key, ":", friends[c][key])
                if key in INCLUDE:
                    message += f'http://vk.com/id{c}\n'
                    message += f'Было:  {key}: -\n'
                    message += f'Стало: {key}: {friends[c][key]}\n'
            elif friends[c][key] != old_friends[c][key]:
                # print("Было:  ", key, ":", old_friends[c][key])
                # print("Стало: ", key, ":",  friends[c][key])
                if key in INCLUDE:
                    message += f'http://vk.com/id{c}\n'
                    message += f'Было:  {key}: {old_friends[c][key]}\n'
                    message += f'Стало: {key}: {friends[c][key]}\n'

    print(message)

    file = open("friends.ini", 'w')
    file.writelines(str(friends_to_save) + '\n')


if __name__ == "__main__":
    main()
