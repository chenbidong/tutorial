import cv2 as cv
import numpy as np

print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("D:/opencvPictures/contours.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
cv.waitKey(0)

cv.destroyAllWindows()
