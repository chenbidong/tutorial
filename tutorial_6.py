import cv2 as cv
import numpy as np


def blur_demo(image):
    dst = cv.blur(image, (5, 5))
    cv.imshow("blur_demo", dst)


def median_blur_demo(image):
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur_demo", dst)


def custom_blur_demo(image):
    #kernel = np.ones([5, 5], np.float32)/25
    kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]], np.float32)
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("custom_blur_demo", dst)


print("--------- Hello Python ---------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
custom_blur_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()