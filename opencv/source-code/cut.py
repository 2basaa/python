import cv2

#画像読み込み
img = cv2.imread("../image-folder/Lenna.png")

#img[top:bottom:left:right]
#サンプルⅠ
img1 = img[0:50 ,0:50]
cv2.imwrite("../image-folder/Lenna_cut1.png", img1)
#サンプルⅡ
img2 = img[80:380, 100:400]
cv2.imwrite("../image-folder/Lenna_cut2.png", img2)