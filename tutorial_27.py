import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess
"""
 Python验证码识别功能：
    环境搭建---
              安装Pillow、tesseract-ocr与pytesseract模块的安装以及错误解决
    Git下载数据集：
        
    参考博文--
            https://blog.csdn.net/sioon_xux/article/details/78617160
    
"""

def recognize_text():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 1))
    open_out = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow("binary-image", open_out)

    cv.bitwise_not(open_out, open_out)
    textImage = Image.fromarray(open_out)
    text = tess.image_to_string(textImage)
    print("识别结果: %s"%text)


print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("G:/timg.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
recognize_text()
cv.waitKey(0)

cv.destroyAllWindows()
