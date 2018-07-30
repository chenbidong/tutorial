import cv2 as cv
import numpy as np


def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:cw+col]
            print(np.std(roi), np.mean(roi))
            dev = np.std(roi)
            if dev < 15:
                gray[row:row + ch, col:cw + col] = 255
            else:
                ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
                gray[row:row + ch, col:cw + col] = dst
    cv.imwrite("D:/vcprojects/result_binary.png", gray)


print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("D:/opencvPictures/morph02.png")
#cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
#cv.imshow("input image", src)
big_image_binary(src)
cv.waitKey(0)

cv.destroyAllWindows()
