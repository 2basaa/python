#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    lenna_img = cv2.imread("../original_image/Lenna.jpg")
    parrots_img = cv2.imread("../original_image/Parrots.jpg")
    #構文エラー
    if lenna_img is None or parrots_img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    """
    alpha = img1に対する重み
    beta = img2に対する重み
    gamma = それぞれの和に加えられるスカラー
    cv2.addWeighted(img1, alpha, img2, beta, gamma)
    
    cv2.addWeighted()で以下の処理を行う
    saturate()は入力画像の彩度を変更
    dst = saturate(img1*alpha +img2*beta + gamma) 
    """

    #lenna:parrots = 3:7
    dst = cv2.addWeighted(lenna_img, 0.3, parrots_img, 0.7, 0.0)
    cv2.imwrite("../change_image/blend0307.jpg", dst)

    #lenna:parrots = 6:4
    dst = cv2.addWeighted(lenna_img, 0.6, parrots_img, 0.4, 0.0)
    cv2.imwrite("../change_image/blend0604.jpg", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))