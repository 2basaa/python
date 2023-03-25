#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import numpy as np
import cv2

#np.zeros(400,400,3)で400×400ピクセルの青、緑、赤の画像を生成
#それぞれのピクセルは[青、緑、赤]も3つのチャンネルを持つ
#np.uint8=符号なし8ビット整数型
#[[0,0,0]
# [0,0,0]
# :::
# [0,0,0]]とimageはなる
img = np.zeros((400, 400, 3), np.uint8)#黒色
cv2.imwrite('../original_image/original.png', img)
cv2.imshow('img1', img)#[0,0,0]で黒色
img[:,:] = [255, 0, 0]#青色
cv2.imwrite('../change_image/blueImage.png', img)
cv2.imshow('img2', img)#[255,0,0]で青色
img[:,:] = [0, 255, 0]#緑色
cv2.imwrite('../change_image/greenImage.png', img)
cv2.imshow('img3', img)#[0,255,0]で緑色
img[:,:] = [0, 0, 255]#赤色
cv2.imwrite('../change_image/redImage.png', img)
cv2.imshow('img4', img)#[0,0,255]で赤色

cv2.waitKey(0)#キーボード入力を待ち受ける関数
cv2.destroyAllWindows()#全てのウィンドウを閉じる
