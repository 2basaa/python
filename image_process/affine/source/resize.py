#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
try:
    img = cv2.imread("../original_image/Lenna.png")
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()
        
    #cv2.flip(img, flipCode)
    #flipCode=0でx軸周りで反転(上下反転)
    #flipCode>0でy軸周りでの反転(左右反転)
    #flipCode<0で両軸周りでの反転

    scale1 = 0.5
    scale2 = 1.62
    height = img.shape[0]#縦が512
    width = img.shape[1]#横が512
    #cv2.resize(img, (横のスケール値　,縦のスケール値))
    dst = cv2.resize(img, (int(width*scale1), int(height*scale1)))
    cv2.imwrite("../change_image/resize0.5.png", dst)

    dst = cv2.resize(img, (int(width*scale2), int(height*scale2)))
    cv2.imwrite("../change_image/resize1.62.png", dst)

    dst = cv2.resize(img, (400, 200))
    cv2.imwrite("../change_image/resize400*200.png", dst)

except:#例外処理を行う。
    import sys#sysとtracebackのエラーを実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))