#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk
import sys
import auth_vk

INFO = """ Метод VK API database.getCity (https://vk.com/dev/database.getCities)

4Приложение использует access_token сохранённый в текстовом файле auth_vk.ini.
В случае если access_token отсутствует, используется авторизация с помощью логина и пароля.
После успешной авторизации access_token сохраняется в текстовом фале auth_vk.ini.
4
Python:
- 3.7

Usage:
python3 get_city.py args [options]

args - строка: аргументы метода database.getCity
Нампример: python3 get_city.py 'country_id=1&q=Балашиха&v=5.95'
"""


APP_ID = '6478436'
V = 9.95
VERSION = '1.0.00 (27.10.2019)'
AUTHOR = 'Deviur (https://github.com/deviur)'

session = auth_vk.login_by_token()
api = vk.API(session, v=V)


def query(request):
    return api.database.getCity(country_id=1)


def main():

    if len(sys.argv) > 1:
        itr = iter(sys.argv[1].replace("=", "&").split("&"))
        request = dict(zip(itr, itr))
        response = query(request)
        print(response)
    else:
        print(INFO)


if __name__ == '__main__':
    main()