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
    ∆(ラプラシアン)=∂^2/∂x^2+∂^2/∂y^2+∂^2/∂z^2
    cv2.Laplacian(img, ddepth)
    ddepthは出力画像のビット震度
    dtypeとは単浮動小数や整数となる(ビットの数)
    ddpeth=-1でimgと同じビット深度
    """
    """
    4近傍(ksize=1)      8近傍
    [0, 1, 0]           [1, 1, 1]
    [1, -4, 1]          [1, -8, 1]
    [0, 1, 0]           [1, 1, 1]
    ↑のフィルタを使用することで、エッジの検出を行うことができる。
    エッジ検出により、3×3の(2,2)の場所の値を変換させる。
    """
    dst = cv2.Laplacian(img, -1)#(30,30)でブラー処理を行う。
    cv2.imwrite("../change_image/Laplacian.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))