#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    #captureでパソコンのカメラを取得
    capture = cv2.VideoCapture(0)
    
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

        #canny処理を行い、エッジ検出を行う。
        #dst = cv2.Canny(img, threshold1, threshold2)
        """
        canny法とは、画像内に含まれる物体を検出
        画素値の微分値がthreshold2の値よりも大きいなら正しいエッジ
        画素値の微分値がthreshold1の値よりも小さいなら正しくないエッジ
        エッジ検出とは、画像内にある物体のエッジを見つけるために用いられる。
        また、明るいところと暗いところの境目を強調して、取り出す。
        それによって、画像内の物体の形状を調べる。
        """
        #色の境界線の色は、白色となる。
        dst = cv2.Canny(frame, 40.0, 200.0)
        cv2.imshow("f", dst)

        #↓のifでは、キーボード上でqを押すと、
        #while処理が狩猟
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    #動画ファイルを閉じる
    capture.release()
    cv2.destroyAllWindows()

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
