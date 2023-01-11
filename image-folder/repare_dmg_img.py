import cv2
import numpy as np
#
try:
    img = cv2.imread('image/Lenna.jpg')

    if img is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()

    msk = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, mask = cv2.threshold(msk, 240, 255, cv2.THRESH_BINARY)
   #マスクの保存
    cv2.imwrite('image/msk.jpg', msk)
    kernel = np.ones((3,3), np.uint8)
    msk = cv2.dilate(msk, kernel)
    cv2.imwrite('image/msk_dilate.jpg', msk)
    dst = img.copy()
#cv2.inpaintで指定された画像内の領域を近傍画像から修復する。
    dst = cv2.inpaint(img, mask, 1, cv2.INPAINT_TELEA)

    cv2.imwrite('image/repare.jpg', dst)
    cv2.imshow('dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))