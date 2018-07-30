import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


print("--------- Hello Python ---------")
src = cv.imread("F:/opencvPictures/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite("F:/result.png", gray)
cv.waitKey(0)

cv.destroyAllWindows()
