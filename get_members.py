#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk
import sys
import auth_vk

INFO = """ 
Метод VK API groups.getMembers (https://vk.com/dev/groups.getMembers). 
Возвращает список участников сообщества.

Python:
- 3.7

Usage:
python3 get_members.py args [options]

args - строка: аргументы метода groups.getMembers
Нампример: python3 get_members.py 'group_id=157262974&count=10'
"""


APP_ID = '6478436'
V = 9.95
VERSION = '1.0.00 (28.10.2019)'
AUTHOR = 'Deviur (https://github.com/deviur)'

session = auth_vk.login_by_token()
api = vk.API(session, v=V)


def do(request):
    return api.groups.getMembers(**request)


def main():

    if len(sys.argv) > 1:
        itr = iter(sys.argv[1].replace("=", "&").split("&"))
        request = dict(zip(itr, itr))
        response = do(request)
        print(response)
    else:
        print(INFO)


if __name__ == '__main__':
    main()