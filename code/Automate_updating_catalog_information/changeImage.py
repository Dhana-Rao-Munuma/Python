#!/usr/bin/env python3

import os
import sys
from PIL import Image

input_image_path = os.path.expanduser("~/supplier-data/images")

print("input_image_path:", input_image_path)

input_image_files = os.listdir(input_image_path)

for image_file in input_image_files:
    if image_file.lower().endswith('.tiff'):
        print(image_file)
        image_full_path = os.path.join(input_image_path,image_file)
        print(image_full_path)

        with Image.open(image_full_path) as img:
            #img.show()
            rgb_image = img.convert("RGB").resize((600,400))
            output_image_path = image_full_path.replace(".tiff",".jpeg")
            rgb_image.save(output_image_path,"JPEG")

        rgb_image.close()

#print(input_image_files)
