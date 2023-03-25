#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
import numpy as np

try:
    lenna_img = cv2.imread("../original_image/Lenna.jpg")
    parrots_img = cv2.imread("../original_image/Parrots.jpg")
    #構文エラー
    lenna_height = lenna_img.shape[0]#レナ画像の高さ
    lenna_width = lenna_img.shape[1]#レナ画像の横幅
    if lenna_img is None or parrots_img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    
    #画像を拡大させる
    lenna_dst = lenna_img.copy()#lenna_imgをコピー
    parrots_dst = cv2.resize(parrots_img, (lenna_width, lenna_height), cv2.INTER_NEAREST)
    lenna_img_roi = lenna_img[lenna_height//4:lenna_height*3//4, 
        lenna_width//4:lenna_width*3//4]#[高さの範囲:幅の範囲]
    parrots_img_roi = parrots_dst[lenna_height//4:lenna_height*3//4, 
        lenna_width//4:lenna_width*3//4]
    lenna_dst_roi = lenna_dst[lenna_height//4:lenna_height*3//4, 
        lenna_width//4:lenna_width*3//4]

    #cv2.addで255以上担うと値は255となる
    #cv2.addでは2つの画像のサイズが同じでないといけない
    #cv2.add(img1, img2, dst)
    #img_maskの範囲だけ画像の合成を実行する
    #指定された範囲の合成を行われる
    #3つ目の引数で同じサイズの画像を出力
    dst = cv2.add(lenna_img_roi, parrots_img_roi, lenna_dst_roi)
    cv2.imwrite("../change_image/dst.png", dst)
    
except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))