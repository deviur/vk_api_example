#!/usr/bin/env python
# -*- coding: utf-8 -*-

#TODO Авторизация в ВК
"""
Консольное приложение Python 3.5

Простой пример авторизации. Приложение использует access_token сохранённый в текстовом файле auth_vk.ini.
В случае если access_token отсутствует или не действует, используется авторизация с помощью логина и пароля.
После успешной авторизации access_token сохраняется в текстовом фале auth_vk.ini.
"""

APP_ID='6478436'
VERSION = '1.0.00 (07.05.2019)'
AUTHOR = 'Deviur (https://github.com/deviur)'

import vk
import getpass


def auth_vk_password():
    session = vk.AuthSession(app_id=APP_ID, user_login=input("VK user_login: "), user_password=getpass.getpass("VK user_password: "))
    file = open("auth_vk.ini", 'w')
    file.writelines(session.access_token)
    return session


def auth_vk_token():
    try:
        file = open("auth_vk.ini", 'r')
    except IOError as e:
        access_token = auth_vk_password().access_token
    else:
        access_token = file.readline()

    session = vk.Session(access_token=access_token)

    return session


def main():
    INFO = '''
    Программа проверки авторизации в ВК. 
    Используется всеми программами пакета vk_api_example в качестве библиотеки.
    Version: %s
    Author: %s

    -------- Результаты ------
    ''' % (VERSION, AUTHOR)

    print(INFO)
    session= auth_vk_token()

    if session:
        print('Авторизация прошла успешно!')
    else:
        print('Авторизация не удалась!')


if __name__ == "__main__":
    main()
