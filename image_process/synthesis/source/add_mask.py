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
    parrots_dst = cv2.resize(parrots_img, (lenna_width, lenna_height), cv2.INTER_NEAREST)
    #np.zeros((高さ, 幅), bitの種類)
    #512×512の行列
    img_mask = np.zeros((lenna_height, lenna_width), np.uint8)
    #0の部分が黒色で表示される
    #↓の255となる部分が、色が表示される部分である。
    img_mask[lenna_height//4:lenna_height*3//4, 
        lenna_width//4:lenna_width*3//4] = [255]
    #cv2.addでは2つの画像のサイズが同じでないといけない
    #cv2.add(img1, img2)
    #img_maskの範囲だけ画像の合成を実行する
    dst = cv2.add(lenna_img, parrots_dst, mask= img_mask)#2つの画像を加算する
    cv2.imwrite("../change_image/addMask1.png", dst)
    #dst=で出力画像を表す
    dst = cv2.add(lenna_img, parrots_dst, dst= lenna_img,mask= img_mask)#2つの画像を加算する
    cv2.imwrite("../change_image/addMask2.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))