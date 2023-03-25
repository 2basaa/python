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
    cv2.Canny(img, threshold1, threshold2)
    imgは8ビットの入力配列
    threshold1は1番目の閾値(minVal)
    threshold2は2番目の閾値(maxVal)
    ddepthは出力画像のビット深度(dtype)
    dtypeとは単浮動小数や整数となる(ビットの数)
    ddpeth=-1でimgと同じビット深度
    """
    """
    canny法とは、画像内に含まれる物体を検出
    画素値の微分値がthreshold2の値よりも大きいなら正しいエッジ
    画素値の微分値がthreshold1の値よりも小さいなら正しくないエッジ
    エッジ検出とは、画像内にある物体のエッジを見つけるために用いられる。
    また、明るいところと暗いところの境目を強調して、取り出す。
    それによって、画像内の物体の形状を調べる。
    """
    #y方向のカーネル(y微分画像を計算)
    dst = cv2.Canny(img, 40.0, 200.0)
    cv2.imwrite("../change_image/Canny.png", dst)
    
except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))