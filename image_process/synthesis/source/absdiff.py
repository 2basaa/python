#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
import numpy as np

try:
    lenna_img = cv2.imread("../original_image/Lenna.jpg")
    parrots_img = cv2.imread("../original_image/Parrots.jpg")
    #構文エラー
    if lenna_img is None or parrots_img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    
    #|lenna_img-parrots_img|
    abs_dst = cv2.absdiff(lenna_img, parrots_img)
    cv2.imwrite("../change_image/absdiff.jpg", abs_dst)

    height = lenna_img.shape[0]#レナ画像の高さ
    width = lenna_img.shape[1]#レナ画像の横幅
    blue = np.zeros((height, width, 3), np.uint8)#np.uint8は符号なし8ビット
    blue[:,:] = [128, 0, 0]#青色を作成

    #cv2.absdiff(img1, img2) = |img1-img2|
    #absdiffで差を求める
    #Lenna.pngからblueの差の絶対値の結果として、背景色は黄色となった。
    blue_lenna = cv2.absdiff(lenna_img, blue)
    cv2.imwrite("../change_image/absdiffScalar.jpg", blue_lenna)
    
except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))