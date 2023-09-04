#!/usr/bin/env python3

import os
import requests
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

url = "http://34.133.92.194/fruits/"

txt_file_path = "~/supplier-data/descriptions/"

txt_file_full_path=os.path.expanduser(txt_file_path)

txt_files = os.listdir(txt_file_full_path)

for txt_file in txt_files:
    if txt_file.lower().endswith('.txt'):
        print(txt_file)

        fruit = {}

        text_file_with_full_path = os.path.join(txt_file_full_path, txt_file)
        with open(text_file_with_full_path,"r") as file:
            line_no = 0
            for line in file.readlines():

                line = line.strip()

                line_no += 1

                if line_no == 1:
                    fruit["name"] = line
                if line_no == 2:
                    fruit["weight"] = int(line.replace(" lbs",""))
                if line_no == 3:
                    fruit["description"] = line

                #image_file = text_file_with_full_path.replace('.txt','.jpeg')
                #fruit["image_name"] = image_file
                image_file = txt_file.replace('.txt','.jpeg')
                fruit["image_name"] = image_file

        r = requests.post(url, data=fruit)


        for key, value in fruit.items():
            print("-",key,"-",value,"-")


