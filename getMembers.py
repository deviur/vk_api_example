#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO Получить список членов группы из ВК
"""
Консольное приложение Python 3.5

Простой пример получения списка членов группы ВК

Может использоваться в качестве модуля для других примеров.
"""

import sys
import vk
import auth_vk

V = '9.95' # Версия VK API

session = auth_vk.auth_vk_token()
api = vk.API(session, v=V)


def get_members(group_id, fil=""):
    return api.groups.getMembers(group_id=group_id, filter=fil)['items']


def get_all_members(group_id):
    members = api.groups.getMembers(group_id=group_id)
    count = members['count']
    offset = 1000
    members = members['items']
    while offset < count:
        members.extend(api.groups.getMembers(group_id=group_id, count=1000, offset=offset)['items'])
        offset += 1000
    return members


def main():

    if len(sys.argv)>1:
        group_id = sys.argv[1]
    else:
        group_id = '157262974'  # ID группы попечителей Школы Граня

    members = get_members(group_id)

    print('group_id')           # Выводим заголовок
    # for member in members:
    #     print(member)

    members = get_all_members(group_id)
    for member in members:
        print(member)


if __name__ == "__main__":
    main()