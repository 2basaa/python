#!python3.7
import cv2

img = cv2.imread("../image-folder/Lenna.png")

x_step = 50
y_step = 50

#オブジェクトimgのshapeメソッドの１つめの戻り値をimg_yに、
#2つ目の戻り値をimg_xに
#img.shpe:画像の高さ、幅、チャンネル数を取得
img_y,img_x=img.shape[:2]

#横軸を引く:y_stpeからimg_yの手前までy_stepおきに白い横線を引く
img[y_step:img_y:y_step, :, :] = 255
#縦線を引く：上と同じような処理
img[:, x_step:img_x:x_step, :] = 255

cv2.imwrite("../imgae-folder/Lenna_grid.png", img)