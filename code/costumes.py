import sys
from PIL import Image
images = []

for arg in sys.argv[1:]:
    print(arg)
    image = Image.open(arg)
    images.append(image)

images[0].save("cat.gif",save_all=True,append_images=[images[1],images[2]],duration=200,loop=0)