import cv2

try:
    img = cv2.imread('image/Lenna.jpg', cv2.IMREAD_GRAYSCALE)

    if img is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()
#cv2.equalizeHist(img)で画像を平滑化することができる。
    dst = cv2.equalizeHist(img)
    cv2.imwrite('image/equalize.jpg', dst)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))