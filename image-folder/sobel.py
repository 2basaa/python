import cv2

try:
    img = cv2.imread('image/Lenna.jpg')
    if img is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()
#Sobel演算子で一次、二次、三次または混合時数の微分画像を計算する。
    dst = cv2.Sobel(img, -1, 0, 1)
    cv2.imwrite('image/sobel.jpg', dst)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))