import cv2

try:
    capture = cv2.VideoCapture(0)
    while(True):
        ret, flame = capture.read()

        if ret == False:
            print('ファイルを読み込めない。')
            break
#動画をグレイスケール（灰色）にする。
        gray = cv2.cvtColor(flame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('f', gray)

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