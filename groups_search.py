#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk
import sys
import auth_vk

INFO = """ 
Метод VK API groups.search (https://vk.com/dev/groups.get). 
Возвращает список сообществ указанного пользователя.

Python:
- 3.7

Usage:
python3 groups_search.py args [options]

args - строка: аргументы метода groups.search

Нампример: python3 groups_search.py 'q=Балашиха'
"""


APP_ID = '6478436'
V = 9.95
VERSION = '1.0.00 (28.10.2019)'
AUTHOR = 'Deviur (https://github.com/deviur)'

session = auth_vk.login_by_token()
api = vk.API(session, v=V)


def do(request):
    # print(request)
    return api.groups.search(**request)


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