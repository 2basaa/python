#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    #grayscaleで読み込む
    img = cv2.imread("../original_image/Lenna.png")
    
    if img is None:#ファイルはない場合に、システムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()

    #cv2.split(img)で色の成分を分割
    #その色の成分が存在しないと黒色(輝度が低い)となる
    #その色の成分が存在すると白色(輝度が高い)となる
    rgb = cv2.split(img)#cv2.splitでカラー画像を分離
    blue = rgb[0]#青色の成分へ分離
    green = rgb[1]#緑色の成分へ分離
    red = rgb[2]#赤色の成分へ分離

    cv2.imwrite("../change_image/blue.png", blue)#青色の要素のsplit
    cv2.imwrite("../change_image/green.png", green)#緑色の要素のsplit
    cv2.imwrite("../change_image/red.png", red)#赤色の要素のsplit

except:
    #例外処理を行う。
    import sys#sysとtracebackのエラーを実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))