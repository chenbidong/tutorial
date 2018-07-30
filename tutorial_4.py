import cv2 as cv
import numpy as np

def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)

def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)

def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)

def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)

def logic_demo(m1, m2):
    #dst = cv.bitwise_and(m1, m2)
    #dst = cv.bitwise_or(m1, m2)
    image = cv.imread("D:/rice.png")
    cv.imshow("image1", image)
    dst = cv.bitwise_not(image)
    cv.imshow("logic_demo", dst)

# 图像增强，增加对比度的方法
def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("con-bri-demo", dst)

def others(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]

    print(M1)
    print(M2)

    print(dev1)
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)

print("--------- Hello Python ---------")
#src1 = cv.imread("D:/vcprojects/images/LinuxLogo.jpg")
#src2 = cv.imread("D:/vcprojects/images/WindowsLogo.jpg")
src1 = cv.imread("D:/rice.png")
src2 = cv.imread("D:/rice2.png")

print(src1.shape)
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)
src = cv.imread("D:/rice.png")
cv.imshow("image2", src)
# src是原始数据    1.5是增强的倍数   0是亮度调整
contrast_brightness_demo(src, 1.2, 30)
#add_demo(src1, src2)0
#subtract_demo(src1, src2)
#divide_demo(src1, src2)
#others(src1, src2)
#logic_demo(src1, src2)
cv.waitKey(0)

cv.destroyAllWindows()
