#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
try:
    img = cv2.imread("../original_image/Lenna.png")
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()

    height = img.shape[0]
    width = img.shape[1]   

    #画像の幅と高さを指定
    #img[高さの範囲, 横幅の範囲]
    #画像の縦[0:80]と横[0:80]の範囲を除去
    dst = img[80: height, 80: width]  
    cv2.imwrite("../change_image/trimming.png", dst)

except:#例外処理を行う。
    import sys#sysとtracebackのエラーを実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))