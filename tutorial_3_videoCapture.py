import  cv2 as cv
import numpy as np
"""
def extrace_object_demo():
    capture = cv.VideoCapture("D:/Video.mp4")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break;
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77,255,255])
        cv.inRange(hsv, lower= lower_hsv, upper=upper_hsv)
        c = cv.waitKey(40)
        if c == 27:
            break
"""
def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb", Ycrcb)

print("--------------hello python------------------")
src = cv.imread("D:/opencvPictures/coins.jpg")
cv.namedWindow("input-image", cv.WINDOW_AUTOSIZE)
cv.imshow("input-image", src)
#extrace_object_demo()
color_space_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

