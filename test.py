import  cv2

if __name__ == '__main__':
    video = cv2.VideoCapture("D:\科技部\情暖宣传视频\main_1.mp4")
    ok, frame = video.read()
    if ok:
        cv2.imshow("tracker", frame)
    while True:
        ok, frame = video.read()
        if ok:
            cv2.imshow("tracker",frame)
            k = cv2.waitKey(1) & 0xff
            if k == 27:
                break