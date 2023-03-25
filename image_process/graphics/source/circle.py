#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import numpy as np
import cv2

img = np.zeros((400, 400, 3), np.uint8)#8bitより最大値255
#cv2.circle(img, (中心座標), 円の半径, 画像の色, 線の太さ)
cv2.circle(img, (200, 200), 50, (255, 0, 0), 1)
cv2.imwrite("../change_image/50circle.png", img)
cv2.imshow('circle1', img)#青色

img = np.zeros((400, 400, 3), np.uint8)#8bitより最大値255
cv2.circle(img, (200, 200), 100, (0, 255, 0), 3)
cv2.imwrite("../change_image/100circle.png", img)
cv2.imshow('circle2', img)#緑色

img = np.zeros((400, 400, 3), np.uint8)#8bitより最大値255
cv2.circle(img, (200, 200), 150, (0, 0, 255), -1)
cv2.imwrite("../change_image/150circle.png", img)
cv2.imshow('circle3', img)#赤色

cv2.waitKey(0)
cv2.destroyAllWindows()