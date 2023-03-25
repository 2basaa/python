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
    center = (int(width/2), int(height/2))

    """
    アフィン変換
    原点を(Xa, Ya)とする。              
    affine_trans = |cosθ  -sinθ  Xa| 
                   |sinθ   cosθ  Ya|
    (x, y)は変換前の座標
    新しい座標(X,Y)は、任意の点(Xa, Ya)を中心に(x, y)をθだけ回転
    |X|= |cosθ  -sinθ  Xa| |x - Xa| 
    |Y|  |sinθ   cosθ  Ya| |y - Ya|
                           |scale |
    アフィン変換では、反時計回りにθ回転(-θ回転)行う。
    X = (x-Xa)cos(-θ)-(y-Ya)sin(-θ)+scale*Xa
    Y = (x-Xa)sin(-θ)+(y-Ya)cos(-θ)+scale*Ya
    """

    #cv2.getRotationMatrix2D(回転の中心座標, 回転角度, スケーリング値)
    #↑で画像回転に使用する2×3の2次元行列のアフィン変換行列を計算
    affin_trans = cv2.getRotationMatrix2D(center, 33.0, 1.0)#33ド
    #cv2.warpAffine(img, affin_transの値, 出力画像のサイズ)
    dst = cv2.warpAffine(img, affin_trans, (width, height))
    cv2.imwrite("../change_image/rotate33.png", dst)

    #scale=1.2よりズームして出力
    affin_trans = cv2.getRotationMatrix2D(center, 110.0, 1.2)#110度
    dst = cv2.warpAffine(img, affin_trans, (width, height))
    cv2.imwrite("../change_image/rotate110.png", dst)

    #scale=0.5より縮小して出力
    affin_trans = cv2.getRotationMatrix2D(center, 90.0, 0.5)#90度
    dst = cv2.warpAffine(img, affin_trans, (width, height))
    cv2.imwrite("../change_image/rotate90.png", dst)

except:#例外処理を行う。
    import sys#sysとtracebackのエラーを実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))