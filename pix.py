import cv2
from PIL import Image

img = cv2.imread("win.png")
print(img[1][2])

cv2.imwrite("pxwin.png",img[1][2])

pixel = Image.open("pxwin.png")

pixel.show()
