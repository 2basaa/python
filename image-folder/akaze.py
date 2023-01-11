import cv2

try:
    img1 = cv2.imread('image/Lenna.jpg')
    img2 = cv2.imread('image/apple.jpg')

    if img1 is None or img2 is None:
        print('ファイルを読み込めない。')
        import sys
        sys.exit()

    detector = cv2.AKAZE_create()
    keypoints1, descriptor1 = detector.detectAndCompute(img1, None)
    keypoints2, descriptor2 = detector.detectAndCompute(img2, None)
#cv2.BFmatcherで２つの画像に点と線を作って合体させる。
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = matcher.match(descriptor1, descriptor2)
    dst = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches, None, flags=2)
    cv2.imwrite('akaze.jpg', dst)
    cv2.imshow('dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))