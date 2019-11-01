#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
import json
from functools import reduce

INFO = """ 
Преобразует структуру JSON в csv

Python:
- 3.7

Usage:
python3 json2csv.py < python3 groups_search.py args [options]

args - строка: аргументы метода groups.search

Нампример: python3 json2csv.py < python3 groups_search.py 'q=Балашиха'
"""

VERSION = '1.0.00 (28.10.2019)'
AUTHOR = 'Deviur (https://github.com/deviur)'


def do(request):
    pass


def _get_keys(dictionary, parent_key=''):
    keys = []
    for key, value in dictionary.items():
        if type(value) is dict:
            keys.extend(_get_keys(value, key))
        else:
            keys.append(key if not parent_key else "%s->%s" % (parent_key, key))
    return keys


def main():
    input_str = sys.stdin.read()
    # TODO попробовать сделать преобразование строки в словарь с помощью eval() вместо json.loads()

    # Преобразуем строку словаря python к стандарту JSON
    # TODO/DONE Добавить замену False на false и True на true
    list_to_replace = [("\"", "\\\""), ("\'", "\""), ("False", "false"), ("True", "true")]  # поседовательность замен
    json_str = reduce(lambda s, r: s.replace(r[0], r[1]), list_to_replace, input_str)

    # Загружаем строку JSON в словарь Python
    json_dict = json.loads(json_str)

    if "items" in json_dict:  # json без items не обрабатываем

        # csv_list = json_dict["items"]

        # TODO/DONE Добавить обработку вложенных словарей
        # TODO Создать список словарей csv_table всех items, включая вложенные
        # Получаем список ключей всех items включая вложенные
        csv_keys = set()
        for item in json_dict['items']:
            if type(item) is dict:
                csv_keys |= set(_get_keys(item))
            else:
                csv_keys = ['id']

        csv_keys = list(csv_keys)

        # TODO Добавить обработку отсутствия ключа и данных словаря в списке (когда пользователь не указал)
        csv_list = []
        for item in json_dict['items']:
            csv_dict = {}.fromkeys(csv_keys, "")
            csv_dict.update()

        # output = csv.writer(sys.stdout, delimiter=';')   # TODO/DONE сделать разделитель столбцов ";" вместо ","
        # output.writerow(csv_list[0].keys())
        # for item in csv_list:
        #     output.writerow(item.values())

    # if len(sys.argv) > 1:
    #     itr = iter(sys.argv[1].replace("=", "&").split("&"))
    #     request = dict(zip(itr, itr))
    #     response = do(request)
    #     print(response)
    # else:
    #     print(INFO)


if __name__ == '__main__':
    main()
