import cv2 as cv
import numpy as np


def fill_color_demo(image):
    copyImg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(copyImg, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copyImg)


def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, : ] = 255
    cv.imshow("fill_binary", image)

    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (100, 2, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary", image)

print("--------- Hello Python ---------")
#src = cv.imread("D:/vcprojects/images/demo.png")
src = cv.imread("rice.jpeg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
#fill_color_demo(src)
fill_binary()
"""
face = src[50:250, 100:300]
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
src[50:250, 100:300] = backface
cv.imshow("face", src)
"""
cv.waitKey(0)
cv.destroyAllWindows()
