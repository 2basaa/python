#元の画像の上部分と左部分の40ピクセルを処理する。
import cv2

try:
    img = cv2.imread('image/Lenna.jpg')

    if img is None:
        print('ファイル読み込めない。')
        import sys
        sys.exit()

    height = img.shape[0]
    width = img.shape[1]

    dst = img[40:height, 40:width]
    cv2.imwrite('image/Trimming.jpg', dst)
    cv2.imshow('dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllwindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))