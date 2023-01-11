import cv2

try:
    img = cv2.imread('image/Lenna.jpg')

    if img is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()
#splitで画像の色成分を抜き出すことができる。
    rgb = cv2.split(img)
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]

    cv2.imwrite('image/blue.jpg', blue)
    cv2.imwrite('image/green.jpg', green)
    cv2.imwrite('image/red.jpg', red)

    cv2.imshow('image/red.jpg', blue)
    cv2.imshow('image/red.jpg', green)
    cv2.imshow('image/red.jpg', red)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))