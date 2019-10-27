#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Авторизация в ВК с помощю пароля

Приложение использует access_token сохранённый в текстовом файле auth_vk.ini.
В случае если access_token отсутствует, используется авторизация с помощью логина и пароля.
После успешной авторизации access_token сохраняется в текстовом фале auth_vk.ini.

Python:
- 3.7

Usage:
python3 auth_vk.py

"""

import getpass

import vk

APP_ID = '6478436'
V = 9.95
VERSION = '2.0.00 (26.10.2019)'
AUTHOR = 'Deviur (https://github.com/deviur)'


def login_by_password():
    try:
        session = vk.AuthSession(app_id=APP_ID, user_login=input("VK user_login: "),
                                 user_password=getpass.getpass("VK user_password: "))
    except vk.exceptions.VkAPIError:
        print('Авторизация не удалась. Проверьте логин или пароль.\n')
        return None
    else:
        file = open("auth_vk.ini", 'w')
        file.writelines(session.access_token)
        return session


def login_by_token():
    try:    # Проверяем наличие файла с token-ом
        file = open("auth_vk.ini", 'r')
    except IOError:
        session = login_by_password()
        return session
    else:
        access_token = file.readline()
        session = vk.Session(access_token=access_token)

    api = vk.API(session, v=V)
    try:
        api.users.get()
    except vk.exceptions.VkAPIError:
        session = login_by_password()
    return session


def main():
    session = login_by_token()
    api = vk.API(session, v=V)
    try:
        user = api.users.get()[0]
    except vk.exceptions.VkAPIError:
        print('Авторизация не удалась. Повторите попытку.\n')
        login_by_password()
    else:
        print("Приветствую, {}!".format(user['first_name']))
        print("Авторизация прошла успешно!")


if __name__ == "__main__":
    main()
