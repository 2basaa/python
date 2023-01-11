import cv2
import sys

try:
#sys.argvはコマンドラインのリスト
#コマンドラインでは下のターミナルで読み込むファイル名を書く。
    if (len(sys.argv) != 2):
        print("引数に読み込む画像はありません。")
        sys.exit()

#cv2.imreadで画像読み込み
    img = cv2.imread(sys.argv[1])        #画像ファイルの読み込み 
    if img is None:
        print('ファイルを読み込めません。')
#sys.exit()でプログラムの終了を表す。
        import sys
        sys.exit()

#(50, 50), (50, 200)で(50, 50)から(50, 200)までという意味を表す。
    cv2.line(img, (50, 50), (50, 200), (255, 0, 0)) 
#最後の5は線の太さを表す。
    cv2.line(img, (50, 100), (200, 100), (0, 0, 255), 5) 
#cv2.imreadで画像保存
#相対パスでは下のように's:/~'を抜いて、'image'からかける。
    cv2.imwrite('image/LinesOnImage2.jpg', img)
#cv2.imshow('img', img)でimgを'img'という名前で表している。
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
