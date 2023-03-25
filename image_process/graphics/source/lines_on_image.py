#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    img = cv2.imread("../original_image/Lenna.png")
    #構文エラー
    if img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    #cv2.line(img, 始点, 終点, 線の色, 線の太さ)
    cv2.line(img, (100, 100), (400, 100), (255, 0, 0))
#座標は教科書の2倍くらいの値にする
    cv2.line(img, (100, 200), (400, 200), (255, 0, 0), 5)

    cv2.imshow("img", img)
    cv2.imwrite("../change_image/LinesOnImage.png", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))