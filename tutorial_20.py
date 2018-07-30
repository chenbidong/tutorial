import cv2 as cv
import numpy as np


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # X Gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # Y Gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    #edge
    #edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    edge_output = cv.Canny(gray, 30, 100)
    cv.imshow("Canny Edge", edge_output)
    return edge_output


def contours_demo(image):
    """dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image", binary)"""
    binary = edge_demo(image)

    cloneImage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)
        approxCurve = cv.approxPolyDP(contour, 4, True)
        if approxCurve.shape[0] > 6:
            cv.drawContours(image, contours, i, (0, 255, 255), 2)
        if approxCurve.shape[0] == 4:
            cv.drawContours(image, contours, i, (255, 255, 0), 2)
        print(approxCurve.shape[0])
        print(i)
    cv.imshow("detect contours", image)


print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("D:/vcprojects/images/blob.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
contours_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
