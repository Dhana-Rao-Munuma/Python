#!/usr/bin/env python3

import re
import pytesseract
from PIL import Image

error_file = 'C:\Dhana\OneDrive - Conduent\Reading Materials\python\my_code\syslog_error.txt'

"""
input_files = [
               'C:\Dhana\OneDrive - Conduent\Reading Materials\python\my_code\syslog.png',
               'C:\Dhana\OneDrive - Conduent\Reading Materials\python\my_code\syslog_1.png',
               'C:\Dhana\OneDrive - Conduent\Reading Materials\python\my_code\syslog_2.png'
               ]

custom_config = r'--oem 3 --psm 6'
pytesseract.pytesseract.tesseract_cmd = "C:/Users/30190137/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

with open(error_file, "w+") as file:
    for input_file in input_files:
        string = pytesseract.image_to_string(Image.open(input_file), lang='eng', config=custom_config)
        #print("string ", string)
        file.write(string)
"""

#pattern = r"ERROR ([\w ]*)\(([\w])\)"
pattern = r"ticky: (INFO|ERROR) ([\w' ]*)(\[#[0-9]*\])? \(([\w.]*)\)"  # \(([\w]*)\)"

error = {}
user = {}

with open(error_file, "r") as file:
    for each_line in file:
        error_string = re.search(pattern, each_line)
        #print(error_string)
        string_1 = ""
        string_2 = ""
        string_3 = ""
        string_4 = ""
        if error_string:
            if error_string.group(1):
                string_1 = error_string.group(1)
            if error_string.group(2):
                string_2 = error_string.group(2)
            if error_string.group(3):
                string_3 = error_string.group(3)
            if error_string.group(4):
                string_4 = error_string.group(4)

                #error[error_string.group(1)] = error_string.group(2)
            print(string_1, "-", string_2, "-", string_4) #, "-", string_4)
            if string_1 == "INFO":
                if
                user[string_4]["INFO"] += 1
            if string_1 == "ERROR":
                user[string_4]["ERROR"] += 1
