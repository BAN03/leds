import cv2
from PIL import Image

img = cv2.imread("win.png",3)

def showImage():
    pixel = Image.open("pxwin.png")
    pixel.show()

def writePixel(height:int, width:int=None):
    if num2:
        cv2.imwrite("pxwin.png",img[height][width])
        showImage()
        return height, width
    else:
        cv2.imwrite("pxwin.png",img[height])
        showImage()
        return height



#print(img[writePixel(1,2)])
print(img[5][5])
cv2.imwrite("pxwin.png",img)
showImage()
