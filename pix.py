import cv2
from PIL import Image
import random
import numpy as np

img = cv2.imread("win.png",3)

def ran():
    return random.randint(0,255)

def showImage():
    pixel = Image.open("pxwin.png")
    pixel.show()

def writePixel(height:int, width:int=None):
    if num2:
        cv2.imwrite("pxwin.png",img[height, width])
        showImage()
        return height, width
    else:
        cv2.imwrite("pxwin.png",img[height])
        showImage()
        return height

img_to_leds = np.ndarray((16, 16, 3), dtype = int)
print(img_to_leds)

for i in range(16):
    for j in range(16):
        img_to_leds[i,j] = img[i,j]
"""
img_to_leds = [[[0,0,0] for i in range(16)] for i in range(16)]
print(type(img), type(img_to_leds))
img_to_leds[5,5] = img[5,5]
#print(img[writePixel(1,2)])
print(img[6:8, 3])
img[5, 5] = [14, 201, 25]
#img[6:8] = [[ran(),ran(),ran()] for i in range(16)]
img[6:8, 3] = [[25, 67, 240],[83, 94, 0]]
"""
cv2.imwrite("pxwin.png",img_to_leds)
showImage()
