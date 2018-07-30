import cv2 as cv
import numpy as np


def template_demo():
    tpl = cv.imread("D:/javaopencv/tpl.png")
    target = cv.imread("D:/javaopencv/test1.png")
    cv.imshow("template image", tpl)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th);
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        #cv.imshow("match-"+np.str(md), target)
        cv.imshow("match-" + np.str(md), result)


print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
template_demo()
cv.waitKey(0)

cv.destroyAllWindows()
