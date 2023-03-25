#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    #grayscaleで読み込む
    img = cv2.imread("../original_image/Lenna.png", cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("ファイルを読み込めない")
        import sys
        sys.exit()

    #cv2.threshold(img, 閾値, 最大値, スレッショルド処理)
    #cv2.THRESH_BINARYでは、img(x,y)の値が閾値以上の値ならば、dst(x,y)=max_valueに変換
    #閾値未満の値ならば、dst(x,y)=0に変換
    #[0, 0, 0]で黒色
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_BINARY)
    #retは閾値,dstは変換後の画像
    cv2.imwrite("../change_image/thresh_binary.png", dst)

    #cv2.THRESH_BINARY_INVでは、img(x,y)の値が閾値以上の値ならば、dst(x,y)=0に変換
    #閾値未満の値ならば、dst(x,y)=max_valueに変換
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_BINARY_INV)
    cv2.imwrite("../change_image/thresh_binary_inv.png", dst)

    #cv2.THRESH_TRUNCでは、img(x,y)の値が閾値以上の値ならば、dst(x,y)=閾値に変換
    #閾値未満の値ならば、dst(x,y)=img(x,y)に変換
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TRUNC)
    cv2.imwrite("../change_image/thresh_trunc.png", dst)

    #cv2.THRESH_TOZEROでは、img(x,y)の値が閾値以上の値ならば、dst(x,y)=img(x,y)であり、
    #閾値未満の値ならば、dst(x,y)=0に変換
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TOZERO)
    cv2.imwrite("../change_image/thresh_tozero.png", dst)

    #cv2.THRESH_TOZERO_INVでは、img(x,y)の値が閾値以下の値ならば、dst(x,y)=img(x,y)に変換
    #閾値未満の値ならば、dst(x,y)=0に変換
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TOZERO_INV)
    cv2.imwrite("../change_image/thresh_tozero_inv.png", dst)

except:
    #例外処理を行う。
    import sys#sysとtracebackのエラーを実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))