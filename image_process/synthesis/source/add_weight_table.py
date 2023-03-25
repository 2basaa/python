#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
import math
import numpy as np

try:

    def create_cos(rows, cols):
        #weightで一つの座標に[0, 0, 0]のrows×colsを作成
        #0は32ビットの単浮動小数とする
        weight = np.zeros((rows, cols, 3), np.float32)
        #centerは、中心座標(x,y)
        center = (rows/2, cols/2)
        #radiusは半径, radius=x^2+y^2
        radius = math.sqrt(pow(center[0], 2) + pow(center[1], 2))

        for row in range(rows):#行のそれぞれの要素
            for col in range(cols):#列のそれぞれの要素
                #distance from center
                distance = math.sqrt(pow(center[0]-row, 2)
                        + pow(center[1]-col, 2))

                #radius=π,current radian
                #radian is arc
                #rad = この長さ(distance*pi)/(円の半径)
                radian = (distance / radius) * math.pi

                #cosθ, normalize -1.0~1.0 to 0~1.0
                y = (math.cos(radian) + 1.0) / 2.0
                #それぞれの座標の色の重みをyに変換
                weight[row, col] = [y, y, y]

        return weight

    #白(255, 255, 255), 黒(0, 0, 0)
    lenna_img = cv2.imread("../original_image/Lenna.jpg").astype(np.float32) / 255
    parrots_img = cv2.imread("../original_image/Parrots.jpg").astype(np.float32) / 255
    
    #構文エラー
    if lenna_img is None or parrots_img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    
    #lenna_img[0], lenna_img[1] = lenna_img[:2]
    #行と列の要素数
    rows, cols = lenna_img.shape[:2]
    
    #weightを作成
    #真ん中の円が白色
    weight = create_cos(rows, cols)
    #1-weightの値を取得
    #真ん中の円が黒色
    i_weight = 1 - weight

    #cv2.multiply(img1, img2)でimg1×img2の乗算を求める
    int_lenna = cv2.multiply(lenna_img, weight)#画像の外側を黒色に
    int_parrots = cv2.multiply(parrots_img, i_weight)#中心の円を黒色に
    add_dst = cv2.add(int_lenna, int_parrots)

    cv2.imwrite("../change_image/intLenna.png", int_lenna * 255)
    cv2.imwrite("../change_image/intParrots.png", int_parrots * 255)
    cv2.imwrite("../change_image/intAdd.png", add_dst * 255)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))