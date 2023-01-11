import cv2

try:
    img = cv2.imread('image/Lenna.jpg')

    if img is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()

    height = img.shape[0]
    width = img.shape[1]
    center = (int(width / 2), int(height / 2))
    #cv2.getRotationMatrix2Dで回転の原点、回転角度、スケーリング値を指定する。
    affin_trans = cv2.getRotationMatrix2D(center, 33.0, 1.0)
    #cv2.warpAffineは画像の回転を表す。また、これは2掛ける3の行列計算をしている。
    dst = cv2.warpAffine(img, affin_trans, (width, height))
    cv2.imwrite('image/rotate_033.jpg', dst)
    cv2.imshow('dst1', dst)

    affin_trans = cv2.getRotationMatrix2D(center, 111.0, 1.0)
    dst = cv2.warpAffine(img, affin_trans, (width, height), flags=cv2.INTER_CUBIC)
    cv2.imwrite('image/rotate_110.jpg', dst)
    cv2.imshow('dst2', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))