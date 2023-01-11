import cv2
import numpy as np

try:
    img1 = cv2.imread('image/Lenna.jpg')
    img2 = cv2.imread('image/apple.jpg')

    if img1 is None or img2 is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()

    height = img1.shape[0]
    width = img1.shape[1]

    img_mask = np.zeros((height, width), np.uint8)
    img_mask[height//4:height*3//4, width//4:width*3//4] = [255]
#maskは画像の中心部へ四角形を形成し、その範囲だけを加算対象とする。
    dst = cv2.add(img1, img2, mask = img_mask)
    cv2.imwrite('image/addMask1.jpg', dst)
    cv2.imshow('dst1', dst)

    dst = cv2.add(img1, img2, dst = img1,mask = img_mask)
    cv2.imwrite('image/addMask2.jpg', dst)
    cv2.imshow('dst2', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.ec_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))