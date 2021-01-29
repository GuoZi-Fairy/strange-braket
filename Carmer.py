from typing import NoReturn
import numpy as np
import cv2 as cv
frontface_cascPath = "haarcascades\haarcascade_frontalface_default.xml"
profileface_cascPath = "haarcascades\haarcascade_profileface.xml"
frontfaceCascade_frontface = cv.CascadeClassifier(frontface_cascPath) 
profilefaceCascade_frontface = cv.CascadeClassifier(profileface_cascPath)
# 人脸数据

def video_demo():
#0是代表摄像头编号，只有一个的话默认为0
    capture=cv.VideoCapture(0) 
    while(True):
        ref,frame=capture.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) ## 灰度转化
        front_faces = frontfaceCascade_frontface.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        )
        pf_faces1 = profilefaceCascade_frontface.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        )
        pf_faces2 = profilefaceCascade_frontface.detectMultiScale(
        cv.flip(gray,1),
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        )
        if front_faces != ():
            (x1, y1, w1, h1) = front_faces[0]
            print("正脸")
            cv.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
        elif pf_faces1 != ():
            (x1, y1, w1, h1) = pf_faces1[0]
            print("向左侧")
            cv.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
        elif pf_faces2 != (): 
            (x1, y1, w1, h1) = pf_faces2[0]
            print("向右侧")
            cv.rectangle(frame,(x1, y1), (w1 - x1, y1 + h1), (0, 255, 0), 2)
        cv.imshow("test",frame)
        c= cv.waitKey(1) & 0xff  #等待30ms显示图像，若过程中按“Esc”退出?
        if c==27:
            capture.release()
            break
            
video_demo()
cv.waitKey()
cv.destroyAllWindows()