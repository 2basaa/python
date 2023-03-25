#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    lenna_img = cv2.imread("../original_image/Lenna.jpg")
    parrots_img = cv2.imread("../original_image/Parrots.jpg")
    #構文エラー
    lenna_height = lenna_img.shape[0]#レナ画像の高さ
    lenna_width = lenna_img.shape[1]#レナ画像の横幅
    if lenna_img is None or parrots_img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    
    """
    cv2.resize(img, (幅, 高さ), interpolation)
    (幅, 高さ)を指定して出力画像をそのサイズに変更
    interpolationでリサイズ時の補間方法を指定
    画像を縮小してから、拡大することによってモザイク処理をすることができる
    """
    #画像を縮小させる
    parrots_dst = cv2.resize(parrots_img, (lenna_width, lenna_height), cv2.INTER_NEAREST)
    #cv2.addでは2つの画像のサイズが同じでないといけない
    #cv2.add(img1, img2)
    dst = cv2.add(lenna_img, parrots_dst)#2つの画像を加算する
    #元のサイズに戻す
    cv2.imwrite("../change_image/parrots_dst.png", parrots_dst)
    cv2.imwrite("../change_image/add.png", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))