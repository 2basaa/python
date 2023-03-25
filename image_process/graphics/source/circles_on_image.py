#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    img = cv2.imread("../original_image/Lenna.png")

    if img is None:
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    #cv2.circle(img, (中心座標), 円の半径, 画像の色, 線の太さ)
    #色は(青、緑、赤)
    cv2.circle(img, (100, 100), 80, (0, 255, 0), 2)#緑
    cv2.circle(img, (300, 300), 160, (255, 255, 0), 6)#水色
    cv2.circle(img, (400, 400), 100, (0, 255, 255), -1)#黄色
    
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