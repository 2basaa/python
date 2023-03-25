#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    #grayscaleで読み込む
    img = cv2.imread("../original_image/Lenna.png")
    
    if img is None:
        print("ファイルを読み込めない")
        import sys
        sys.exit()

    #cv2.cvtColorでimgをgrayscale化
    dst = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("../change_image/grayscale2.png", dst)

except:
    #例外処理を行う。
    import sys#sysとtracebackのエラーを実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))