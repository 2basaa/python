#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    
    capture = cv2.VideoCapture(0)
    cascade_url = "../detect_folder/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_url)
    
    while (True):
        """
        cascade = cv2.CascadeClassifier(urlオブジェクト検出用の学習ファイルを読み込む
        cascade.detectMultiScale(img)でimgからオブジェクトを検出する
        facerectは二重配列となる
        pt1は四角形の頂点
        pt2は反対側の四角形の頂点
        thicknessは線の太さs
        cv2.rectangle(img, pt1, pt2, thickness)
        ret, frame = capture.read()
        retはTrueかFalse
        frameで画面の情報を取得
        """
        ret, frame = capture.read()
        if ret == False:
            print("カメラを取得できませんでした")
            continue

        #facerect = cascade.detectMultiScale(frame)でframeからオブジェクトを検出する
        facerect = cascade.detectMultiScale(frame)
     
        #tuple型は、()の形
        if len(facerect) > 0:
            #facerectは二重配列であり、rectはその中の要素
            #facerectの中の4つの頂点をとりだす。
            for rect in facerect:
                cv2.rectangle(frame, tuple(rect[0:2]), 
                tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=2)
        
        cv2.imshow("f", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    capture.release()#captureを解放
    cv2.destroyAllWindows()
    print(facerect)#画面の中の頂点の座標を手に入れる
    
except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))