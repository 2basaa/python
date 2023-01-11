import cv2
import numpy as np

try:
    img = cv2.imread('image/Lenna.jpg')
    if img is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()
#dialteで膨張処理を行う。
    kernel = np.ones((3,3), np.uint8)
    dst = cv2.dilate(img, kernel)
    cv2.imwrite('image/dilate.jpg', dst)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))