#!python3.7
import cv2
from PIL import Image

################################
'''
src = 入力画像
dsize = リサイズ後の大きさ
fx = x方向の倍率
fy = y方向の倍率
interpolation = 補間方法
'''
################mozaic#######################
image = cv2.imread("../image-folder/Lenna.png")
#rationでモザイクの新さを制御
def mozaic(src, ratio=0.1):
    #cv2.resize(src, dsize, fx, fy, interpolation)
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    #listのスライス[開始位置:終了位置:ステップ]
    #ステップが-1ならば逆順に要素を取得
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

new_image = mozaic(image)
cv2.imwrite("../image-folder/Lenna_mozaic.png", new_image)

###############mozaic_area####################
def mozaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y+height, x:x+width] = mozaic(dst[y:y+height, x:x+width], ratio)
    return dst

dst_area = mozaic_area(image, 50, 200, 200, 300)
cv2.imwrite("../image-folder/Lenna_mozaic_area.png", dst_area)

##############face_detect_mozaic###############
face_cascade_path = "../detect-folder/haarcascade_frontalface_default.xml"
#モザイク処理
hiroshi_image = cv2.imread("../image-folder/AbeHiroshi.png")
face_cascade = cv2.CascadeClassifier(face_cascade_path)
image_gray = cv2.cvtColor(hiroshi_image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(image_gray)
for x, y, w, h in faces:
    dst_face = mozaic_area(hiroshi_image, x, y, w, h)

cv2.imwrite("../image-folder/Hiroshi_mozaic.png", dst_face)

####################gif#######################
source = cv2.cvtColor(cv2.imread("../image-folder/Lenna.png"), cv2.COLOR_BGR2RGB)

imgs = [Image.fromarray(mozaic(source, 1 / i)) for i in range(1, 25)]
imgs += imgs[-2::-1] + [Image.fromarray(source)] * 5

imgs[0].save("../image-folder/Lenna_mozaic.gif", save_all=True, 
append_images=imgs[1:], optimize=False, duration=50, loop=0)