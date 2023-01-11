import cv2

try:
    img_1 = cv2.imread('image/Lenna.jpg')
    img_2 = cv2.imread('image/apple.jpg')

    if img_1 is None or img_2 is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()
#cv2.matchTemplateでテンプレートと、それに重なった画像領域を比較する。
    result = cv2.matchTemplate(img_1, img_2, cv2.TM_CCOEFF_NORMED)
    mmr = cv2.minMaxLoc(result)
    pos = mmr[3]

    dst = img_1.copy()
    cv2.rectangle(dst, pos, (pos[0] + img_2.shape[1], pos[1] + img_2.shape[0]), (0, 0, 255), 2)

    cv2.imwrite('image/template.jpg', dst)
    cv2.imshow('dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))