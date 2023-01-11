import cv2

try:
    img = cv2.imread('image/Lenna.jpg')

    if img is None:
        print('ファイルを読み込まない。')
        import sys
        sys.exit()
    #circle(画像, 中心, 半径, 色, 線の太さ)線の太さがマイナスのときは中を塗りつぶす。
    cv2.circle(img, (50, 50), 40, (0, 255, 0), 2)
    cv2.circle(img, (150, 150), 80, (255, 255, 0), 6)
    cv2.circle(img, (200, 200), 50, (0, 255, 255), -1)

    cv2.imwrite('image/CircleImage.jpg', img)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#'Error'の条件を除いている。
except:
    import sys
    print('Error', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))