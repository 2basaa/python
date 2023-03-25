#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe

import cv2
import numpy as np

try:
    img = cv2.imread("../original_image/Lenna.png")
    #構文エラー
    if img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    
    """
    np.ones((3, 3), np.uint8)で
    3×3の行列を作成→全ての値は1となる。
    1は全て8ビットの値となる。
    erodeは縮小処理
    cv2.erode(img, kernel)
    kernelは構造要素
    erodeは縮小処理より、物体の境界線を細くする処理
    """
    #uint8は符号なし8ビット
    kernel = np.ones((3, 3), np.uint8)
    dst = cv2.erode(img, kernel)#3×3で膨張処理
    cv2.imwrite("../change_image/erode.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))