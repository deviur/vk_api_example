#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO Получить список членов группы из ВК
"""
Консольное приложение Python 3.5

Простой пример получения списка членов группы ВК

Может использоваться в качестве модуля для других примеров.
"""

import sys
import time
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


#    Функция get_all_members_2(group_id)
#    Возвращает user_id пользвателей группы group_id методом execute
def get_all_members_2(group_id):

    code = """
var members = API.groups.getMembers({"group_id":Args.group_id});
var count = members.count;
var offset = 1000;

members = members.items;
while (offset < count){
  members = members + API.groups.getMembers({"group_id":Args.group_id, "count":1000, "offset":offset}).items;
  offset = offset + 1000;
}
return members;"""
    pass


def get_all_members_3(group_id):
    # Возвращает членов группы с городами
    members = api.groups.getMembers(group_id=group_id, fields='city')
    count = members['count']
    offset = 1000
    members = members['items']
    while offset < count:
        members.extend(api.groups.getMembers(group_id=group_id, fields='city', count=1000, offset=offset)['items'])
        offset += 1000
    return members


def get_all_members_from(group_id, city_id):

    members = api.groups.getMembers(group_id=group_id, fields='city')
    count = members['count']
    offset = 1000
    members = members['items']

    while offset < count:
        members.extend(api.groups.getMembers(group_id=group_id, fields='city', count=1000, offset=offset)['items'])
        offset += 1000
        time.sleep(5)  # иначе даёт ошибку, слишком много запросов. TODO: сделать запрос через Хранимую процедуру

    members_from = []
    for member in members:
        if 'city' in member and member['city']['id'] == city_id:
            members_from.append(member)

    return members_from


def main():

    if len(sys.argv)>1:
        group_id = sys.argv[1]
    else:
        group_id = '157262974'  # ID группы попечителей Школы Граня

    # members = get_members(group_id)
    #
    # print('group_id')           # Выводим заголовок
    # for member in members:
    #     print(member)
    #
    # members = get_all_members(group_id)
    # for member in members:
    #     print(member)

    members = get_all_members_3(157262974)
    for member in members:
        print(member)


if __name__ == "__main__":
    main()