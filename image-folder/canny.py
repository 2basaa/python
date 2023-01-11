import cv2

try:
    img = cv2.imread('image/Lenna.jpg')
    if img is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()
#エッジ検出のためにcannyアルゴリズムを実行している。
    dst = cv2.Canny(img, 40.0, 200.0)
    cv2.imwrite('image/canny.jpg', dst)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))