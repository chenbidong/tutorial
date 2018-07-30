import cv2 as cv
import numpy as np


def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15, 15))
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open-result", binary)


def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow("close_demo", binary)


print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("D:/vcprojects/images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
open_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
