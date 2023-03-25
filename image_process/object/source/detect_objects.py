#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
   
    lenna_img = cv2.imread("../original_image/Lenna.png")
    
    #構文エラー
    if lenna_img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()

    """
    cascade = cv2.CascadeClassifier(urlオブジェクト検出用の学習ファイルを読み込む
    cascade.detectMultiScale(img)でimgからオブジェクトを検出する
    facerectは二重配列となる
    pt1は四角形の頂点
    pt2は反対側の四角形の頂点
    thicknessは線の太さs
    cv2.rectangle(img, pt1, pt2, thickness)
    """
    cascade_url = "../detect_folder/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_url)
    facerect = cascade.detectMultiScale(lenna_img)
   
    #tuple型は、()の形
    if len(facerect) > 0:
        for rect in facerect:
            cv2.rectangle(lenna_img ,tuple(rect[0:2]), 
            tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=2)
    
    else:
        print("no face")
        
    cv2.imwrite("../change_image/dobj.jpg", lenna_img)

    print(facerect)
    
except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))