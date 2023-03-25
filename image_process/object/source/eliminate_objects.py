#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
import numpy as np

try:
   
    lenna_img = cv2.imread("../original_image/Lenna.png")
    height = lenna_img.shape[0]#画像の高さ
    width = lenna_img.shape[1]#画像の横幅

    mask_img = np.zeros((height, width, 3), np.uint8)
    mask_img[:,:] = [0, 0, 0]
    #構文エラー
    if lenna_img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()


    """
    cascade = cv2.CascadeClassifier(urlオブジェクト検出用の学習ファイルを読み込む
    cascade.detectMultiScale(img)でimgからオブジェクトを検出する
    facerectは二重配列となる
    pt1は四角形の頂点(左上)
    pt2は反対側の四角形の頂点(右下)
    thicknessは線の太さs-1で塗りつぶし
    cv2.rectangle(img, pt1, pt2, thickness)
    """
    cascade_url = "../detect_folder/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_url)
    facerect = cascade.detectMultiScale(lenna_img)
    
    #tuple型は、()の形
    #下で、mask_imgの白色部分作成
    #mask_imgで、lenna_imgの一部を隠す
    if len(facerect) > 0:
        for rect in facerect:
            cv2.rectangle(mask_img ,tuple(rect[0:2]), 
            tuple(rect[0:2]+rect[2:4]), (255, 255, 255), thickness=-1)
    
    else:
        print("no face")
        
    cv2.imwrite("../original_image/mask.png", mask_img)
    #mask_dstで画像をGRAYSCALE化、1つの画素数を8ビット
    mask_dst = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
    
    """
    imgは入力画像
    inpaintMaskは、8ビットでシングルチャンネルの修復マスク画像(grayscale化)
    inpaintRadiusは修復される点周りの円形の近傍領域
    flagsは修復手法
    cv2.inpaint()で指定された画像内の領域を近傍画像から修復
    cv2.inpaint(img, inpaintMask, inpaintFadius, flags, dst)
    """
    dst = cv2.inpaint(lenna_img, mask_dst, 1, cv2.INPAINT_TELEA)
    cv2.imwrite("../change_image/eliminateFace.jpg", dst)
    
except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))