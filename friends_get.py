#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk
import sys
import auth_vk

INFO = """ 
Метод VK API groups.friends.get (https://vk.com/dev/friends.get). 
Возвращает список участников сообщества.

Python:
- 3.7

Usage:
python3 friends_get.py args [options]

args - строка: аргументы метода friends.get
Нампример: python3 friends_get.py 'fields=city,sex,relation'
"""


APP_ID = '6478436'
V = 9.95
VERSION = '1.0.00 (28.10.2019)'
AUTHOR = 'Deviur (https://github.com/deviur)'

session = auth_vk.login_by_token()
api = vk.API(session, v=V)


def do(request):
    return api.friends.get(**request)


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