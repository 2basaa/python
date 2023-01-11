import cv2

try:
    img = cv2.imread('image/Lenna.jpg')

    if img is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()

#putText(画像, 文字列, 座標, 文字サイズ, 文字の尺度, 文字の色, 線の太さ)
    cv2.putText(img, 'Hello OpenCV', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 60, 80), 2)
    cv2.imwrite('image/putText.jpg', img)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
