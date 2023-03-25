#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
import numpy as np
import time

try:
    #captureでパソコンのカメラを取得
    capture = cv2.VideoCapture(0)
    #パソコンの画面の高さを指定
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #パソコンの画面の横幅を指定
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    #roi_targetで4つの領域に分割
    roi_target = [0, 1, 2, 3]

    while(True):
        #retはカメラを取得できたかどうか
        #すなわち、TrueかFalse
        #frameでは、captureのそれぞれの座標の色のデータを取得
        #frameでは、(x,y)のそれぞれの色の要素を取得
        ret, frame = capture.read()

        #カメラを取得できなかった。
        if ret == False:
            print("カメラを取得できませんでした")
            break
        #それぞれの座標に[赤、緑、青]の値を[0,0,0]とする。
        dst = np.zeros((height, width, 3), np.uint8)

        """
        ________________
        |i = 0 | i = 3 |
        |______|_______|
        |i = 1 | i = 2 |
        |______|_______|
        図.roiの各要素が管理する座標

        ↓がそれぞれの領域の要素を配列にして格納
        x1,y1は、x,yの値が小さい座標
        x2,y2は、x,yの値が大きい座標
        """
        y1 = [0, height//2, height//2, 0]
        y2 = [height//2, height, height, height//2]
        x1 = [0, 0, width//2, width//2]
        x2 = [width//2, width//2, width, width]

        for i in range(0, 4):
            #dst[i]をそれぞれframe[i]の領域とする
            dst[y1[i]:y2[i], x1[i]:x2[i]] = \
                frame[y1[roi_target[i]]:y2[roi_target[i]],
                    x1[roi_target[i]]:x2[roi_target[i]]]
    
        #roi_target[number]のそれぞれの要素の値に1加算する
        #加算することによって、得られた画像が出力される領域が変更する
        for number in range(0, 4):
            roi_target[number] += 1
            if roi_target[number] == 4:
                roi_target[number] = 0

        cv2.imshow("f", dst)

        #↓のifでは、キーボード上でqを押すと、
        #while処理が狩猟
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        time.sleep(0.5)

    #動画ファイルを閉じる
    capture.release()
    cv2.destroyAllWindows()

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
