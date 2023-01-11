import cv2
#cv2.IMREAD_GRAYSCALEでカラー画像をグレイスケイル画像に変換する。
try:
    img = cv2.imread('image/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print('ファイル読み込めない。')
        import sys
        sys.exit()
    
    cv2.imwrite('image/grayscale.jpg', img)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))