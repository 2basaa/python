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
    #得られた画面の中心座標
    center = (width//2, height//2)
    degree = 0.0

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
        """
        retval = cv2.getRotationMatrix2D(中心座標, 回転角度, スケーリング係数)
        ↑で、中心座標を中心に、反時計回りに回転角度の大きさだけ回転
        そのためのアフィン変換を行うための2×3の行列式を計算する
        cv2.warpAffine(img, retval, 出力サイズ)
        ↑を使用することによって、中心座標を中心に、反時計回りに回転角度の大きさだけ回転
        """
        affin_trans = cv2.getRotationMatrix2D(center, degree, 1.0)
        dst = cv2.warpAffine(frame, affin_trans, (width, height))
        degree += 1.0

        cv2.imshow("f", dst)

        #↓のifでは、キーボード上でqを押すと、
        #while処理が終了
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        time.sleep(0.1)

    #動画ファイルを閉じる
    capture.release()
    cv2.destroyAllWindows()

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
