#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    img = cv2.imread("../original_image/Lenna.png")
    #構文エラー
    if img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    
    """
    ボックスフィルタのアルゴリズム
    J(出力画像)=σI(入力画像)/|Np|
               q(参照画素)~Np(参照画素の集合体)
    ↑の正方形の範囲の画素の平均を求めて、画像を平滑化させる。
    ddepthは、dtypeの深さ
    cv2.boxFilter(img, ddepth, カーネルサイズ(幅、高さ))
    """
    dst = cv2.boxFilter(img, -1, (5, 5))#(5,5)で平滑化
    cv2.imwrite("../change_image/boxFilter5.png", dst)

    dst = cv2.boxFilter(img, -1, (10, 10))#(10,10)で平滑化
    cv2.imwrite("../change_image/boxFilter10.png", dst)

    dst = cv2.boxFilter(img, -1, (25, 25))#(25,25)で平滑化
    cv2.imwrite("../change_image/boxFilter25.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))