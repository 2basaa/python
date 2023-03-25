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

        #grayscale化
        gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
        #内部カメラを表示
        cv2.imshow("f", gray)

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
