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
    dst = cv2.flip(img, 0)#上下反転  
    cv2.imwrite("../change_image/flip0.png", dst)

    dst = cv2.flip(img, 1)#左右反転
    cv2.imwrite("../change_image/flip1.png", dst)

    dst = cv2.flip(img, -1)#左右、上下で反転    
    cv2.imwrite("../change_image/flip2.png", dst)

except:#例外処理を行う。
    import sys#sysとtracebackのエラーを実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))