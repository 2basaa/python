#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    img = cv2.imread("../original_image/Lenna.png")

    if img is None:#画像がないならば、プログラムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    #cv2.putTextで画像の上に文字を入力
    #cv2.putText(img, text, 始点の座標, フォントの種類, フォントのスケールファクタ, 画像の色, 線の太さ)
    #色は(青、緑、赤)
    cv2.putText(img, "Hello OpenCV", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (50, 60, 60), 2)

    cv2.imwrite("../change_image/CirclesOnImage.png", img)
    cv2.imshow("img", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    #例外処理を行う。
    import sys#sysとtracebackのエラーを実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))