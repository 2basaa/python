#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    #grayscaleで読み込む
    img = cv2.imread("../original_image/Lenna.png", cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("ファイルを読み込めない")
        import sys
        sys.exit()

    #閾値未満の値ならば、dst(x,y)=0に変換
    #[0, 0, 0]で黒色
    #cv2.adaptiveThresholdで適応的閾値処理を行う
    #cv2.adaptiveThreshold(img, 最大値, 適応的閾値アルゴリズム, 閾値処理の種類, 近傍領域のサイズ, 出力画像のサイズ)
    #cv2.ADAPTIVE_THRESH_GAUSSIAN_Cは喜一処理で使用するアルゴリズム 
    #cv2.ADAPTIVE_THRESH_MEAN_Cは喜一処理で使用するアルゴリズム
    dst = cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 7, 8)
    #retは閾値,dstは変換後の画像
    cv2.imwrite("../change_image/adaptiveThresh.png", dst)

except:
    #例外処理を行う。
    import sys#sysとtracebackのエラーを実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))