#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    img = cv2.imread("../original_image/Lenna.png")
    #構文エラー
    if img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    
    #cv2.blur(img, ksize)
    #ksizeはブラー処理に使用するカラーサイズ(幅、高さ)
    #メディアンブラー処理は平滑化を行う。(指定したカーネルサイズ)
    #メディアンブラー処理では、処理対象画素を中央値に変更する
    #11×11の中央値を求め、一定範囲内の値を平滑化
    dst = cv2.medianBlur(img, 11)#11はカーネルサイズ(11×11)となる。
    cv2.imwrite("../change_image/medianBlur11.png", dst)

    #33×33の中央値を求め、一定範囲内の値を平滑化
    dst = cv2.medianBlur(img, 33)#33はカーネルサイズとなる。
    cv2.imwrite("../change_image/medianBlur33.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))