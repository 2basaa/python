import cv2
#try,exceptにより、コードの実行で正しいものと、例外なものを分けることができる。
try:
    img = cv2.imread('image/Lenna.jpg')

    if img is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()
#cv2.blur(img, (15, 15))でblur関数処理を行う。また、blur処理とは画像を平滑化させる役割を持つ。
    dst = cv2.blur(img, (15, 15))

    cv2.imwrite('image/blur.jpg', dst)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))