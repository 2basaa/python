#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    lenna_img = cv2.imread("../original_image/Lenna.jpg")
    parrots_img = cv2.imread("../original_image/Parrots.jpg")
    mandrill_img = cv2.imread("../original_image/Mandrill.jpg")
    #構文エラー
    if lenna_img is None or parrots_img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()

    height, width = lenna_img.shape[:2]
    """
    dstは出力画像となる
    maskは8ビットシングルチャンネルのマスク
    maskでは、対応する要素のみが変更される
    cv2.bitwise_or(img1, img2[, dst, mask])
    
    bitwise_or()では論理和ORを計算する
    論理和を求め、その結果を出力する
    """

    dst = cv2.bitwise_or(lenna_img, parrots_img)
    cv2.imwrite("../change_image/bitwiseOr1.jpg", dst)

    mandrill_gray_img = cv2.imread("../original_image/Mandrill.jpg", cv2.IMREAD_GRAYSCALE)
    mandrill_gray_dst = cv2.resize(mandrill_gray_img, (height, width))
    dst = cv2.bitwise_or(lenna_img, parrots_img, lenna_img, mandrill_gray_dst)
    cv2.imwrite("../change_image/bitwiseOr2.jpg", dst)

    

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))