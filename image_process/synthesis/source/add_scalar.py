#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
import numpy as np

try:
    img = cv2.imread("../original_image/Lenna.jpg")
    #構文エラー
    height = img.shape[0]#レナ画像の高さ
    width = img.shape[1]#レナ画像の横幅
    if img is None :#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    
    """
    np.zeros((行(row), 列(column),bit))
    ぞれぞれの座標にbit数分だけ作る
    今回の場合では、3
    """
    blue = np.zeros((height, width, 3), np.uint8)
    blue[:,:] = [128, 0, 0]#[青, 緑, 赤]
    #cv2.addでは2つの画像のサイズが同じでないといけない
    #cv2.add(img1, img2)
    dst = cv2.add(img, blue)#2つの画像を加算する
    #元のサイズに戻す
    cv2.imwrite("../change_image/addScalar.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))