#! /bin/sh
"""true"
if command -v python3 > /dev/null; then
  exec python3 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?

Это консольное приложение для авторизации ВКонтакте
>>> get_user(1)
[{'id': 1, 'first_name': 'Павел', 'last_name': 'Дуров', 'is_closed': False, 'can_access_closed': True}]
"""

import vk
import getpass

APP_ID = '6478436'
V = '9.85'
VERSION = '1.0.01 (10.02.2020)'
AUTHOR = 'Deviur (https://github.com/deviur)'


def auth_vk_password():
    session = vk.AuthSession(app_id=APP_ID, user_login=input("VK user_login: "),
                             user_password=getpass.getpass("VK user_password: "))
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
    api = vk.API(session, v=V)

    try:
        api.users.get(user_ids=1)
    except vk.exceptions.VkAPIError as e:
        access_token = auth_vk_password().access_token
        session = vk.Session(access_token=access_token)

    return session


def get_user(user_ids):
    session = auth_vk_token()
    api = vk.API(session, v=V)
    return api.users.get(user_ids=user_ids)


if __name__ == "__main__":
    import doctest
    doctest.testmod()