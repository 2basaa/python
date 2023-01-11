import numpy as np
import cv2
import os

# 相対パス  絶対パス
os.mkdir("image")

img = np.zeros((400, 400, 3), np.uint8)
img[:,:] = [255, 0, 0]
cv2.imwrite('C:/workspace/python/image-folder/image/blueImage.jpg', img)
cv2.imshow('img1', img)

img[:,:] = [0, 255, 0]
cv2.imwrite('C:/workspace/python/image-folder/image/greenImage.jpg', img)
cv2.imshow('img2', img)

img[:,:] = [0, 0, 255]
cv2.imwrite('C:/workspace/python/image-folder/image/redImage.jpg', img)
cv2.imshow('img3', img)

cv2.waitKey(0)
cv2.destroyAllWindows()