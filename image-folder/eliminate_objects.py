import cv2
#入力した画像とオブジェクトが除去された部分を拡大して示している。
try:
    img = cv2.imread('image/Lenna.jpg')
    msk = cv2.imread('image/apple.jpg', cv2.IMREAD_GRAYSCALE)

    if img is None or msk is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()

    dst = cv2.inpaint(img, msk, 1, cv2.INPAINT_TELEA)

    cv2.imwrite('image/eliminate.jpg', dst)
    cv2.imshow('dst.jpg', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))