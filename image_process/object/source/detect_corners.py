#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    max_corners = 50
    block_size = 3
    quality_level = 0.01
    min_distance = 20.0

    lenna_img = cv2.imread("../original_image/Lenna.png")
    #構文エラー
    if lenna_img is None:#画像がないならシステムを終了
        print("ファイルを読み込めない")
        import sys
        sys.exit()
    """
    cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)せグレイスケール化
    maxConersで出力されるコーナーの最大数
    qualityLevelは許容される画像コーナーの最低品質
    minDistanceは出力されるコーナー間の最小ユークリッド距離
    blockSizeでピクセル近傍領域における微分画像の平均化ブロックサイズ
    useHarrisDetectorは「、Harris検出器もしくは、Shi-Tomasi検出器のどちらかを検出
    cv2.goodFeaturesToTrack(gray, maxCorners, qualityLevel, 
        minDistance, blockSize, useHarrisDetector)で
        強いコーナーの検出を行う。
    """
    gray = cv2.cvtColor(lenna_img, cv2.COLOR_RGB2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, max_corners, quality_level,
            min_distance, blockSize= block_size, useHarrisDetector= False)
    
    for number in corners:
        #number.ravel()で配列の中の要素を取り出す
        x, y = number.ravel()
        #強いコーナーの座標に丸を描く
        cv2.circle(lenna_img, (int(x), int(y)), 4, (255, 255, 0), 2)

    cv2.imwrite("../change_image/corners.jpg", lenna_img)
    
except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))