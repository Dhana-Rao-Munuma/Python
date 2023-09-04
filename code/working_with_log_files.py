
# import os
# import sys
import pytesseract  
from PIL import Image
# import subprocess
import re

pytesseract.pytesseract.tesseract_cmd = "C:/Users/30190137/AppData/Local/Programs/Tesseract-OCR/tesseract.exe" 
# your path may be different

log_png_file = "C:\Dhana\OneDrive - Conduent\Reading Materials\python\my_code\log_file.png"
log_text_file = "C:\Dhana\OneDrive - Conduent\Reading Materials\python\my_code\log_file_generated_by_python_from_image.txt"
f = open(log_text_file, "w")
text = str(pytesseract.image_to_string(Image.open(log_png_file)))
f.write(text)
f.close()

error = "CORE ERROR"
returned_errors = []
with open(log_text_file, 'r') as file:
    for log in  file.readlines():
      #print(log)
      error_patterns = [] #["error"]
      #for i in range(len(error.split(' '))):
      #  #error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      #  error_patterns.append(error.split(' ')[i].lower())
      for word in error.split(' '):
         #print("word ", word)
         error_patterns.append(word.lower())

      if all(re.search(error_pattern.lower(),log.lower()) for error_pattern in error.split(' ')):
         returned_errors.append(log)

for i in range(len(returned_errors)):
   print(returned_errors[i])