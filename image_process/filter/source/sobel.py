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
    cv2.Sobel(img, ddepth, dx, dy)
    dxはx方向の微分次数
    dyはy方向の微分次数
    ddepthは出力画像のビット深度(dtype)
    dtypeとは単浮動小数や整数となる(ビットの数)
    ddpeth=-1でimgと同じビット深度
    """
    """
    Sobelカーネル(1次微分フィルタ)
    x方向のカーネル      y方向のカーネル
    (dx=1, dy=0)        (dx=0, dy=1)
    [-1, 0, 1]          [-1, -2, -1]
    [-2, 0, 2]          [0, 0, 0]
    [-1, 0, 1]          [1, 2, 1]
    ↑のフィルタを使用することで、エッジの検出を行うことができる。
    エッジ検出により、3×3の(2,2)の場所の値を変換させる。
    """
    #y方向のカーネル(y微分画像を計算)
    dst = cv2.Sobel(img, -1, 0, 1)
    cv2.imwrite("../change_image/Sobel_y.png", dst)
    #x方向のカーネル(x微分画像を計算)
    dst = cv2.Sobel(img, -1, 1, 0)
    cv2.imwrite("../change_image/Sobel_x.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))