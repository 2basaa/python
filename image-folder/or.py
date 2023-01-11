import cv2
#スカラー値の論理和を求める。
try:
    img1 = cv2.imread('image/Lenna.jpg')
    img2 = cv2.imread('image/apple.jpg')

    if img1 is None or img2 is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()

    dst = cv2.bitwise_or(img1, img2)
    cv2.imwrite('image/or.jpg', dst)
    cv2.imshow('dst1', dst)

    img_mask = cv2.imread('image/mask.bmp', cv2.IMREAD_GRAYSCALE)
    dst = cv2.bitwise_or(img1, img2, img1, img_mask)
    cv2.imwrite('image/orMask.jpg', dst)
    cv2.imshow('dst2', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))