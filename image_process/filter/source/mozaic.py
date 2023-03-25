#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    img = cv2.imread("../original_image/Lenna.png")
    #構文エラー
    if img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    
    """
    cv2.resize(img, (幅, 高さ), interpolation)
    (幅, 高さ)を指定して出力画像をそのサイズに変更
    interpolationでリサイズ時の補間方法を指定
    画像を縮小してから、拡大することによってモザイク処理をすることができる
    """
    scale = 0.1
    height = img.shape[0]#画像の高さ
    width = img.shape[1]#画像の幅

    #画像を縮小させる
    dst = cv2.resize(img, (round(width*scale), 
       round(height*scale)), interpolation= cv2.INTER_NEAREST)#(5,5)で平滑化

    #元のサイズに戻す
    dst = cv2.resize(dst, (width, height), interpolation= cv2.INTER_NEAREST)#(5,5)で平滑化
    cv2.imwrite("../change_image/mozaic.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))