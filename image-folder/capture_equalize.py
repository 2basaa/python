import cv2

try:
    capture = cv2.VideoCapture(0)
    while(True):
        ret, flame = capture.read()

        if ret == False:
            print('カメラを読み込めない。')
            break

        gray = cv2.cvtColor(flame, cv2.COLOR_BGR2GRAY)
#14行目から輝度平滑化を行う。
        dst = cv2.equalizeHist(gray)
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