import cv2 as cv
import numpy as np


def hat_gray_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    cimage = np.array(gray.shape, np.uint8)
    cimage = 120;
    dst = cv.add(dst, cimage)
    cv.imshow("tophat", dst)


def hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("tophat", dst)


def hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
    cv.imshow("tophat", dst)


def gradient2_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dm = cv.dilate(image, kernel)
    em = cv.erode(image, kernel)
    dst1 = cv.subtract(image, em) # internal gradient
    dst2 = cv.subtract(dm, image) # external gradient
    cv.imshow("internal", dst1)
    cv.imshow("external", dst2)


print("--------- Python OpenCV Tutorial ---------")
#the path of the pic
src = cv.imread("D:/tutorial_1/rice.jpeg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
gradient2_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
