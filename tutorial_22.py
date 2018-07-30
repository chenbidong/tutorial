import cv2 as cv
import numpy as np


def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.erode(binary, kernel)
    cv.imshow("erode_demo", dst)


def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.dilate(binary, kernel)
    cv.imshow("dilate_demo", dst)


print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
#erode_demo(src)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
dst = cv.erode(src, kernel)
cv.imshow("result", dst)
cv.waitKey(0)

cv.destroyAllWindows()
