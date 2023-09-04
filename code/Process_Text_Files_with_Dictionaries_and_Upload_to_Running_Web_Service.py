#!/usr/bin/env python3


import os

import sys

import requests
import json

input_file_path = '/data/feedback/'

comment = {}

for each_file in os.listdir(input_file_path):
    each_full_file = input_file_path + each_file
    print(each_file)
    print(each_full_file)

    with open(each_full_file, "r") as i_file:
        comment = {}
        for line_no,each_line in enumerate(i_file):
            print("each_file:", each_file, "line_no:", line_no, "each_line:", each_line);
            if line_no == 0:
                key = 'title'
            elif line_no == 1:
                key = 'name'
            elif line_no == 2:
                key = 'date'
            elif line_no == 3:
                key = 'feedback'

            comment[key] = each_line.strip()

        for key1, value1 in comment.items():
            print("key1:", key1, "value1:", value1)

        try:
            #response = requests.post("http://34.23.233.9/feedback/", data=comment)
            response = requests.post("http://34.23.233.9/feedback/", json=comment)

            print(response)
            print(response.status_code)
            print(response.request.url)
            print(response.request.body)
            #print(response.content)

        except requests.exceptions.RequestException as exc:
            print()
            print()
            print()
            print("excccccccccccccccccccccccc:", exc)
            print()
            print()
            print()
