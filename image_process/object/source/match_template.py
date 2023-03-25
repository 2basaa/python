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
    cascade_rulで目を検出
    """
    cascade_url = "../detect_folder/haarcascade_eye.xml"
    cascade = cv2.CascadeClassifier(cascade_url)
    facerect = cascade.detectMultiScale(lenna_img)

    #画像切り出し、img[top: bottom: left: right]
    #右目を検出する 
    if len(facerect) > 0:
        for rect in facerect:
            #座標をえる
            bottom = rect[1]
            right = rect[0]
            top = rect[3]
            left = rect[2]
    else:
        print("no hat")

    #右目を検出
    lenna_right_eye = lenna_img[top: bottom, left: right]
    #cv2.imwrite("../original_image/lennaEye.jpg", lenna_right_eye)

    """
    imgは探索対象となる画像
    templは探索されるテンプレート画像(探索対象となる画像より小さくする)
    methodは比較手法
    cv1.matchTemplate()で、テンプレートとそれに重なった画像領域を比較する
    cv2.matchTemplate(img, templ, method)
    cv2.minMaxLocで配列内の最小値及び最大値を求める
    cv2.minMaxLoc(img)imgは入力配列
    戻り値は、minVal, maxVal, minLoc, maxLocとなる。
    Locは保持する位置のこと
    """
    result = cv2.matchTemplate(lenna_img, lenna_right_eye, cv2.TM_CCOEFF_NORMED)
    mmr = cv2.minMaxLoc(result)
    pos = mmr[3]#maxLoc(最大値を保持する位置)

    dst = lenna_img.copy()#元の画像をコピーする
    #cv2.rectangle(img, 左上座標, 右下座標, 線の色, 線の太さ)
    cv2.rectangle(dst, pos, (pos[0] + lenna_right_eye.shape[1], pos[1] + lenna_right_eye.shape[0]),
        (0, 0, 255), 2)#赤色bg

    cv2.imwrite("../change_image/dst_match.jpg", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))