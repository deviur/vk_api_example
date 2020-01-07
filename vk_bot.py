import getpass
import time
import vk

APP_ID = '6478436'
V = 9.85
# LIST_TO_SEND = ['deleted', 'relation', 'status', 'deactivated']
LIST_TO_SEND = ['deleted', 'relation', 'deactivated']
USER_ID = 133147577
VERSION = '1.0.00 (08.01.2020)'
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
    try:  # Проверяем наличие файла с token-ом
        file = open("auth_vk.ini", 'r')
    except IOError:
        session = login_by_password()
        return session
    else:
        access_token = file.readline()
        session = vk.Session(access_token=access_token)

    api = vk.API(session, scope='messages', v=V)
    try:
        api.users.get()
    except vk.exceptions.VkAPIError:
        session = login_by_password()
    return session


def main():
    # Авторизация в ВК
    session = login_by_token()

    # Подключение к API
    api = vk.API(session, v=V)

    # Проверка, удалась ли авторизация
    try:
        user = api.users.get()[0]
    except vk.exceptions.VkAPIError:
        print('Авторизация не удалась. Повторите попытку.\n')
        login_by_password()
    else:
        print("Приветствую, {}!".format(user['first_name']))
        print("Авторизация прошла успешно!")

    friends = api.friends.get(user_id=0, fields='sex, bdate, city, relation, status')

    try:  # Проверяем наличие файла со списком друзей
        file = open("friends.ini", 'r')
    except IOError:
        file = open("friends.ini", 'w')
        file.writelines(str(friends) + '\n')
        return

    # Загружаем список друзей за предыдущий период из файла в словарь
    file = open("friends.ini", 'r')
    old_friends = eval(file.read())

    # Создаём словарь текущих друзей
    keys, items = [f['id'] for f in friends['items']], [f for f in friends['items']]
    friends = dict(zip(keys, items))

    # Создаём словарь друзей предыдущего периода
    keys, items = [f['id'] for f in old_friends['items']], [f for f in old_friends['items']]
    old_friends = dict(zip(keys, items))

    deleted = [f for f in old_friends.keys() if not(f in friends.keys())]
    added = [f for f in friends.keys() if f not in old_friends.keys()]
    changed = []
    for f in friends.keys():
        if f not in added:
            friends[f].pop('track_code')
            old_friends[f].pop('track_code')
            friends[f].pop('online')
            old_friends[f].pop('online')

            if friends[f] != old_friends[f]:
                changed.append(f)

    message = ''
    for d in deleted:
        if 'deleted' in LIST_TO_SEND:
            message += '\nПользовател(ь/и) удалил(ся/ись):\n'
            message += f'http://vk.com/id{d}\n'

    print(deleted)
    print(added)
    print(changed)

    # Печать изменений
    message += '\nПользовател(ь/и) внес(ли) изменения:\n'
    for c in changed:
        print("Изменения:", c)
        for key in friends[c]:
            if key not in old_friends[c]:
                print("Было:  ", key, ":  -")
                print("Стало: ", key, ":", friends[c][key])
                if key in LIST_TO_SEND:
                    message += f'http://vk.com/id{c}\n'
                    message += f'Было:  {key}: -\n'
                    message += f'Стало: {key}: {friends[c][key]}\n'
            elif friends[c][key] != old_friends[c][key]:
                print("Было:  ", key, ":", old_friends[c][key])
                print("Стало: ", key, ":",  friends[c][key])
                if key in LIST_TO_SEND:
                    message += f'http://vk.com/id{c}\n'
                    message += f'Было:  {key}: {old_friends[c][key]}\n'
                    message += f'Стало: {key}: {friends[c][key]}\n'
    print(message)


if __name__ == "__main__":
    main()
