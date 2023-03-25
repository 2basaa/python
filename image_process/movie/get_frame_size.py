#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2

try:
    #captureでパソコンのカメラを取得
    capture = cv2.VideoCapture(0)
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #widthで行(幅),heightで列(高さ)を取得
    print("frame size = " + str(width) + str(height) + 
    "×" + str(height))

except:#例外エラー
    import sys#例外処理を以下で実行
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))