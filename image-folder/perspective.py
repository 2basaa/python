import cv2
import numpy as np

try:
    img = cv2.imread('image/Lenna.jpg')
    if img is None:
        print('ファイル読み込めない。')
        import sys
        sys.exit()

    rows, cols = img.shape[:2]
    x0 = cols / 4
    x1 = (cols * 3) / 4
    y0 = rows / 4
    y1 = (rows * 3) / 4

    list_srcs = np.float32([[x0, y0], [x0, y1], [x1, y1], [x1, y0]])

    #pattern-0
    x_margin = cols / 10
    y_margin = rows / 10
    list_dsts = np.float32([list_srcs[0], list_srcs[1], [x1 - x_margin, y1 - y_margin], [x1 - x_margin, y0 + y_margin]])
#cv2.getPerspectiveTransformは透視変換行列を行う。
#cv2.warpPerspectiveは画像の透視投影を行う。S
    perspective_mmartix = cv2.getPerspectiveTransform(list_srcs, list_dsts)
    dst = cv2.warpPerspective(img, perspective_mmartix, (cols, rows))

    cv2.imwrite('image/dst0.jpg', dst) 
    cv2.imshow('dst0', dst)

    #pattern-1
    x_margin = cols / 8
    y_margin = rows / 8
    list_dsts = np.float32([[x0 + x_margin,y0 + y_margin], list_srcs[1], list_srcs[2], [x1 - x_margin, y0 + y_margin]])

    perspective_mmartix = cv2.getPerspectiveTransform(list_srcs, list_dsts)
    dst = cv2.warpPerspective(img, perspective_mmartix, (cols, rows))

    cv2.imwrite('image/dst1.jpg', dst) 
    cv2.imshow('dst1', dst)
   
    #pattern-2
    x_margin = cols / 6
    y_margin = rows / 6
    list_dsts = np.float32([[x0 + x_margin,y0 + y_margin], list_srcs[1], [x1 - x_margin, y1 - y_margin],list_srcs[3]])

    perspective_mmartix = cv2.getPerspectiveTransform(list_srcs, list_dsts)
    dst = cv2.warpPerspective(img, perspective_mmartix, (cols, rows))

    cv2.imwrite('image/dst2.jpg', dst) 
    cv2.imshow('dst2', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Erros:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))