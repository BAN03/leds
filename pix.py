import json
from json import JSONEncoder
import cv2
from PIL import Image
import numpy as np

img = cv2.imread("win.png",3)

def showImage():
    pixel = Image.open("pxwin.png")
    pixel.show()

npjson = {"nparray":img.tolist()}

with open("img.json", "w") as file:
    json.dump(npjson, file)

with open("img.json", "r") as target:
    img_to_leds = np.asarray(json.load(target)["nparray"])


print(img_to_leds[5,5])
