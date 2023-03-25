#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    img = cv2.imread("../original_image/Lenna.png")
    #構文エラー
    if img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    
    #cv2.GaussianBlurでは、ガウシアンフィルターを用いてブラー処理を行う。
    #ガウシアンフィルターでは、ガウス分布に従ってカーネル内の重みを計算したフィルタ
    """
    ↓がガウス分布の数式
    f(x,y)=(1/2πσ^2)exp(-(x^2+y^2)/2σ^2)
    上記の式を用いて、ブラー処理を実行する。
    cv2.GaussianBlur(img, カーネルサイズ(幅、高さ), x方向のガウシアン, y方向のガウシアン)
    """
    dst = cv2.GaussianBlur(img, (13, 13), 10, 10)#(30,30)でブラー処理を行う。
    cv2.imwrite("../change_image/gaussianBlur1.png", dst)

    dst = cv2.GaussianBlur(img, (31, 5), 80, 5)#(30,30)でブラー処理を行う。
    cv2.imwrite("../change_image/gaussianBlur2.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))