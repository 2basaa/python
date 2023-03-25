#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
import numpy as np

try:
   
    lenna_img = cv2.imread("../original_image/Lenna.png")

    #damage_imgでlenna画像に白い円を描く
    damage_lenna = cv2.circle(lenna_img, (200, 200), 100, (255, 255, 255), 1)
    damage_lenna = cv2.circle(lenna_img, (300, 300), 50, (255, 255, 255), 1)
    #構文エラー
    if lenna_img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()

    #ダメージを受けた画像を保存する
    cv2.imwrite("../original_image/damageLenna.png", damage_lenna)
    #maskでグレイスケール化
    mask = cv2.cvtColor(damage_lenna, cv2.COLOR_RGB2GRAY)

    #閾値１を240とし、閾値2を255と設定する
    """
    cv2.threshold関数で,
    ノイズが閾値1を閾値1を超えていたら閾値2の値にする
    閾値1以下なら０へ設定
    よって、閾値1以上なら、白色にし、それ以外なら、黒色に変更s
    """
    ret, mask = cv2.threshold(mask, 240, 255, cv2.THRESH_BINARY)

    #damage画像をコピー
    dst = damage_lenna.copy()
    #cv2.inpaintでdamage_lennaのダメージを除去
    #cv2.inpaintで指定された画像内の領域を近傍画像から修復
    #maskで除去する部分を設定する
    dst = cv2.inpaint(damage_lenna, mask, 1, cv2.INPAINT_TELEA)
    cv2.imwrite("../change_image/RepairImage.jpg", dst)
    
except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
