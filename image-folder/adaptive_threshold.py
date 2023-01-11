import cv2

try:
    img = cv2.imread('image/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print('ファイル読み込めない。')
        import sys
        sys.exit()
# cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 8)でアダプディスレッショルド処理を行う。
    dst = cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 8)
    cv2.imwrite('image/adaptiveThreshold.jpg', dst)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))