import cv2

try:
    capture = cv2.VideoCapture(0)

    while(True):
        ret, frame = capture.read()

        if ret == False:
            print('カメラを読み込めない。')
            break
#canny処理をした後に、周りの背景画を白色にする。
        dst = cv2.Canny(frame, 40.0, 200.0)
        dst = cv2.bitwise_not(dst)
        cv2.imshow('f', dst)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))