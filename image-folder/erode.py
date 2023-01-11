import cv2
import numpy as np

try:
    img = cv2.imread('image/Lenna.jpg')
    if img is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()
#erode処理で画像の収縮処理を行う。
    kernel = np.ones((3, 3), np.uint8)
    dst = cv2.erode(img, kernel)
    cv2.imwrite('image/erode.jpg', dst)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))