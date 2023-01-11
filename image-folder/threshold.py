import cv2

try:
    img = cv2.imread('image/Lenna.jpg')

    if img is None:
        print('ファイル×')
        import sys
        sys.exit()
 #cv2.threshold(img, 100, 200, cv2.THRESH_BINARY)で画像の輝度を変えられる。
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_BINARY)
    cv2.imwrite('image/threshold_THRESH_BINARY.jpg', dst)
    cv2.imshow('dst1', dst)

    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_BINARY_INV)
    cv2.imwrite('image/threshold_THRESH_BINARY_INV.jpg', dst)
    cv2.imshow('dst2', dst)

    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TRUNC)
    cv2.imwrite('image/threshold_THRESH_TRUNC.jpg', dst)
    cv2.imshow('dst3', dst)

    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TOZERO)
    cv2.imwrite('image/threshold_THRESH_TOZERO.jpg', dst)
    cv2.imshow('dst4', dst)

    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TOZERO_INV)
    cv2.imwrite('image/threshold_THRESH_TOZERO_INV.jpg', dst)
    cv2.imshow('dst5', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))