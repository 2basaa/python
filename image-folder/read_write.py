# -*- coding: utf-8 -*

import cv2						              #OpenCVライブラリ 
				
img = cv2.imread('c:/workspace/python/image-folder/image/Lenna.jpg')        #画像ファイルの読み込み 
cv2.imwrite('c:/workspace/python/image-folder/image/ReadWrite.jpg', img)          #出力画像の保存