import cv2
import numpy as np
#動画の画面をシャッフルする。
try:
    capture = cv2.VideoCapture(0)
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    roi_target = [0, 1, 2, 3]
    counter = 60

    while(True):
        ret, frame = capture.read()

        if ret == False:
            print('カメラを読み込めない。')
            break

        dst = np.zeros((height, width, 3), np.uint8)

        y1 = [0, height//2, height//2, 0]
        y2 = [height//2, height, height, height//2]
        x1 = [0, 0, width//2, width//2]
        x2 = [width//2, width//2, width, width]

        for number in range(0, 4):
            dst[y1[number]:y2[number], x1[number]:x2[number]] = \
            frame[y1[roi_target[number]]:y2[roi_target[number]], x1[roi_target[number]]:x2[roi_target[number]]]
#roi_targetを指定することで映像をシャッフルすることができる。
        counter -= 1
        if counter < 0:
            counter = 60
            for number in range(0, 4):
                roi_target[number] += 1
                if roi_target[number] == 4:
                    roi_target[number] = 0

        cv2.imshow('f', dst)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            bread

    capture.release()
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))