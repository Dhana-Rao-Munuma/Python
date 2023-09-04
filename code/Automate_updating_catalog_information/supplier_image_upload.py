#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

input_image_path = "~/supplier-data/images/"

input_image_full_path = os.path.expanduser(input_image_path)

print(input_image_full_path)

input_image_files = os.listdir(input_image_full_path)

for image_file_name in input_image_files:
    if image_file_name.lower().endswith('.jpeg'):
        image_file = os.path.join(input_image_full_path, image_file_name)

        print(image_file)

        with open(image_file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

