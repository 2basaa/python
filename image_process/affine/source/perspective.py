#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
import numpy as np

#透視変換行列
try:
    img = cv2.imread("../original_image/Lenna.png")
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()

    #rows = img.shape[0], cols=img.shape[1]
    #list[始点:終点]
    rows, cols = img.shape[:2]
    #画像のサイズ[x0,x1]&[y0,y1]
    x0 = cols / 4
    x1 = (cols*3) / 4
    y0 = rows / 4
    y1 = (rows*3) / 4

    #np.float32では、単不動浮動小数点32桁
    #↓はリスト
    list_src = np.float32([[x0, y0],[x0, y1],[x1, y1],[x1, y0]])

    #pattern-0
    x_margin = cols/10
    y_margin = rows/10
    #list_dstsでは、出力画像の頂点の座標を指定
    #↓がそれぞれの頂点の座標となる
    #s[0]      s[3]
    #
    #s[1]      s[2]
    #↓ではlist_src[0],list_src[3]をlist_dsts[0],list_dsts[3]に変換
    list_dsts = np.float32([[x0+x_margin, y0+y_margin],list_src[1],
                list_src[2],[x1-x_margin, y0+y_margin]])

    #cv2.getPerspectiveTransform(入力座標の頂点, 出力座標の頂点)で透視行列変換を求める
    perspective_matrix = cv2.getPerspectiveTransform(list_src, list_dsts)
    #cv2.warpPerspectiveで頂点を変換(透視変換行列を実行)
    #cv2.warpPerspective(img, 透視変換行列, 画像のサイズ)
    dst = cv2.warpPerspective(img, perspective_matrix, (cols, rows))
     
    cv2.imwrite("../change_image/dst1.png", dst)

    #pattern-1
    x_margin = cols/8
    y_margin = rows/8
    #↓ではlist_src[2],list_src[3]をlist_dsts[2],list_dsts[3]に変換
    list_dsts = np.float32([list_src[0],list_src[1],
                [x1-x_margin, y1-y_margin],[x1-x_margin, y0+y_margin]])

    perspective_matrix = cv2.getPerspectiveTransform(list_src, list_dsts)
    dst = cv2.warpPerspective(img, perspective_matrix, (cols, rows))
     
    cv2.imwrite("../change_image/dst2.png", dst)

    #pattern-2
    x_margin = cols/6
    y_margin = rows/6
    #↓ではlist_src[0],list_src[2]をlist_dsts[0],list_dsts[2]に変換
    list_dsts = np.float32([[x0+x_margin, y0+y_margin],list_src[1],
                [x1-x_margin, y1-y_margin], list_src[3]])

    perspective_matrix = cv2.getPerspectiveTransform(list_src, list_dsts)
    dst = cv2.warpPerspective(img, perspective_matrix, (cols, rows))
     
    cv2.imwrite("../change_image/dst3.png", dst)

except:#例外処理を行う。
    import sys#sysとtracebackのエラーを実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))