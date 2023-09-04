#!/usr/bin/env python3

from PIL import Image
import os

directory_path = "/home/student-04-c54265e77edc/images/"
filenames = os.listdir(directory_path)

for filename in filenames:
    file_path = os.path.join(directory_path,filename)
    print(file_path)
    if filename.startswith("."):
        continue
    img = Image.open(file_path)
    img = img.convert('RGB')
    f, e = os.path.splitext(filename)
    print("f ", f, "e ", e)
    new_file_name = "/opt/icons/" + f + ".jpg"
    print("new_file_name ", new_file_name)
    #new_file_name = replace(filename, ".
    new_img = img.rotate(90)
    new_img_1 = img.resize((128,128))
    #new_img_1.save(new_file_name, format='JPEG')
    new_img_1.save(new_file_name)
    #img.rotate(90).resize((128,128)).save("/opt/icons/new_file_name")
    #img.rotate(90).resize((128,128)).save("/opt/icons/new_file_name")

