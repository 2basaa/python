import cv2

try:
    img1 = cv2.imread('image/Lenna.jpg')
    img2 = cv2.imread('image/apple.jpg')

    if img1 is None or img2 is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()
#add関数で画像を合成する。
    dst = cv2.add(img1, img2)
    cv2.imwrite('image/add.jpg', dst) 
    cv2.imshow('dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))