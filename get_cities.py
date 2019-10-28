#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk
import sys
import auth_vk

INFO = """ 
Метод VK API database.getCity (https://vk.com/dev/database.getCities). 
Возвращает список городов.

Python:
- 3.7

Usage:
python3 get_cities.py args [options]

args - строка: аргументы метода database.getCity
Нампример: python3 get_cities.py 'country_id=1&q=Балашиха&v=5.95'
"""


APP_ID = '6478436'
V = 9.95
VERSION = '1.0.00 (27.10.2019)'
AUTHOR = 'Deviur (https://github.com/deviur)'

session = auth_vk.login_by_token()
api = vk.API(session, v=V)


def do(request):
    return api.database.getCities(**request)


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