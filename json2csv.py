#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
import json

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
    # print(request)
    return api.groups.search(**request)


def main():
    json_str = sys.stdin.read().replace("\"", "\\\"").replace("\'", "\"")
    # print(json_str)
    request = json.loads(json_str)
    # print(request)
    if "items" in request:
        output = csv.writer(sys.stdout)
        output.writerow(request["items"][0].keys())
        for item in request["items"]:
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
