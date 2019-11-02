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


def _get_sub_keys(dictionary, parent_key=''):
    keys = []
    for key, value in dictionary.items():
        if type(value) is dict:
            keys.extend(_get_sub_keys(value, key))
        else:
            keys.append(key if not parent_key else "%s->%s" % (parent_key, key))
    return keys


def _get_sub_items(items: dict, parent_key: str = "") -> dict:
    sub_items = {}
    for key, value in items.items():
        if type(value) is dict:
            sub_items.update(_get_sub_items(value, key))
        else:
            sub_items.update({key if not parent_key else "%s->%s" % (parent_key, key): value})
    return sub_items


def main():
    input_str = sys.stdin.read()
    # DONE попробовать сделать преобразование строки в словарь с помощью eval() вместо json.loads()
    json_dict = eval(input_str)
    # Преобразуем строку словаря python к стандарту JSON
    # DONE Добавить замену False на false и True на true. ПРИМЕР: Множественная замена
    # list_to_replace = [("\"", "\\\""), ("\'", "\""), ("False", "false"), ("True", "true")]  # поседовательность замен
    # json_str = reduce(lambda s, r: s.replace(r[0], r[1]), list_to_replace, input_str)
    #
    # # Загружаем строку JSON в словарь Python
    # json_dict = json.loads(json_str)

    if "items" in json_dict:  # json без items не обрабатываем

        # DONE Добавить обработку вложенных словарей
        # DONE Создать список словарей csv_table всех items, включая вложенные
        # Получаем список ключей всех items включая вложенные
        csv_head = []
        csv_table = []
        for item in json_dict['items']:
            if type(item) is dict:
                csv_row = _get_sub_items(item)
            else:
                csv_row = {'id': item}

            csv_head.extend([key for key in csv_row.keys() if key not in csv_head])
            csv_table.append(csv_row)  # Добавляем строку в таблицу csv_table

        # DONE Добавить обработку отсутствия ключа и данных словаря в списке (когда пользователь не указал)
        csv_result = []
        for row in csv_table:
            csv_row = {}.fromkeys(csv_head, "")
            csv_row.update(row)
            csv_result.append(csv_row)

        # print(csv_result)
        output = csv.writer(sys.stdout, delimiter=';')   # DONE сделать разделитель столбцов ";" вместо ","
        output.writerow(csv_head)
        for item in csv_result:
            output.writerow(item.values())


if __name__ == '__main__':
    main()
