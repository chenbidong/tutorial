import cv2 as cv
import numpy as np


#从摄像头上实时获取数据
cap = cv.VideoCapture(0)
fourcc = cv.CV_FOURCC(*'XVID')
#opencv3的话用:fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))#保存视频
while True:
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    out.write(frame)#写入视频
    cv.imshow('frame',frame)#一个窗口用以显示原视频
    cv.imshow('gray',gray)#另一窗口显示处理视频
    #27ASCII是ESC退出键
    if cv.waitKey(1) &0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()
