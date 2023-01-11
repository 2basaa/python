import cv2

try:
#cv2.imreadで画像読み込み
    img = cv2.imread('c:/workspace/python/image-folder/image/Lenna.jpg')
    if img is None:
        print('ファイルは読み込めません。')
#sys.exit()でプログラムの終了を表す。
        import sys
        sys.exit()

#(50, 50), (50, 200)で(50, 50)から(50, 200)までという意味を表す。
    cv2.line(img, (50, 50), (300, 50), (255, 0, 0)) 
#最後の5は線の太さを表す。
    cv2.line(img, (50, 100), (200, 100), (0, 0, 255), 5) 
#cv2.imreadで画像保存
    cv2.imwrite('c:/workspace/python/image-folder/image/LinesOnImage.jpg', img)
#cv2.imshow('img', img)でimgを'img'という名前で表している。
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
