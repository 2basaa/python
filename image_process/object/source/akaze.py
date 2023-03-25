#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
   
    lenna_img_1 = cv2.imread("../original_image/Lenna.png")
    lenna_img_2 = cv2.imread("../original_image/Lenna.png")
    
    #構文エラー
    if lenna_img_1 is None or lenna_img_2 is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()

    """
    detector = cv2.AKAZE_createで、AKAZE検出器を生成する
    detector.detectAndComputeで特徴点の検出
    BFMatcher型で総当たりのマッチングを行う。
    matcher = cv2.BFMatcher()でBFMatcherオブジェクトの生成
    mathcer.match()で特異点の適合を検出
    cv2.drawMatchesでマッチング結果の絵画
    """

    detector = cv2.AKAZE_create()
    keypoints1, descriptor1 = detector.detectAndCompute(lenna_img_1, None)
    keypoints2, descriptor2 = detector.detectAndCompute(lenna_img_2, None)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = matcher.match(descriptor1, descriptor2)
    dst = cv2.drawMatches(lenna_img_1, keypoints1, lenna_img_2,
        keypoints2, matches, None, flags=2)

    cv2.imwrite("../change_image/akaze.jpg", dst)

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))