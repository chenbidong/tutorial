import cv2 as cv
import numpy as np


def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
    print("threshold value %s"%ret)
    cv.imshow("binary", binary)


def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("binary", binary)


def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])
    mean = m.sum() / (w*h)
    print("mean : ", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("binary", binary)


print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("D:/vcprojects/images/test.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
custom_threshold(src)
cv.waitKey(0)

cv.destroyAllWindows()
