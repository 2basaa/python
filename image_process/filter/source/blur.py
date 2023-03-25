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
    #ksizeはブラー処理に使用すrカラーサイズ(幅、高さ)
    #ブラー処理は平滑化を行う。(指定したカーネルサイズ)
    #この時、サイズ領域の平均値は3となる。
    #処理対象画素は3に変換
    #30×30の平均値を求め、一定範囲内の値を平滑化
    dst = cv2.blur(img, (30, 30))#(30,30)でブラー処理を行う。
    cv2.imwrite("../change_image/blur.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))