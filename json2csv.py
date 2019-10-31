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


def main():
    # TODO/DONE Добавить замену False на false и True на true
    # Преобразуем JSON-python к JSON-standart
    repl_list = [("\"", "\\\""), ("\'", "\""), ("False", "false"), ("True", "true")]  # поседовательность замен
    input_str = sys.stdin.read()
    json_str = reduce(lambda s, r: s.replace(r[0], r[1]), repl_list, input_str)

    # Загружаем строку JSON в словарь Python
    json_dict = json.loads(json_str)

    # TODO Добавить обработку вложенных словарей
    # TODO Добавить обработку отсутствия ключа и данных словаря в списке (когда пользователь не указал)
    # TODO/DONE сделать разделитель столбцов ";" вместо ","
    if "items" in json_dict:
        csv_dict = json_dict["items"]
        output = csv.writer(sys.stdout, delimiter=';')
        output.writerow(csv_dict[0].keys())
        for item in csv_dict:
            output.writerow(item.values())

    # if len(sys.argv) > 1:
    #     itr = iter(sys.argv[1].replace("=", "&").split("&"))
    #     request = dict(zip(itr, itr))
    #     response = do(request)
    #     print(response)
    # else:
    #     print(INFO)


if __name__ == '__main__':
    main()
