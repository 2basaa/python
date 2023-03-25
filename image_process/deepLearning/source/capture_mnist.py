#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import cv2
import numpy as np
from chainer import Chain, serializers
import chainer.functions as f
import chainer.links as l

"""
__init__メソッドについて
MyMLP(Chain)で、Chainを継承する
n_inを入力層28×28
n_uintsを中間層
n_outを出力層(0から9)
l.Linear(chainear.links.Linear)はパラメータ関数を使用し、学習モデルを作成する
chainear.links.Linear関数は層の線形結合を行う
l.Linear(chainear.links.Linear)関数で学習モデルを作成
"""
class MyMLP(Chain):
    def __init__(self, n_in=784, n_uints=100, n_out=10):
        super(MyMLP, self).__init__(
            l1 = l.Linear(n_in, n_uints),
            l2 = l.Linear(n_uints, n_uints),
            l3 = l.Linear(n_uints, n_out),
        )
    """
    __call__メソッドは呼び出し関数となる
    chainer.functionsは、活性化関数(正規線形関数)
    f.relu(chainer.functions.relu)では、
    入力ｘ(MNISTの手書き数字の入力画像)に対して、
    出力y(数字の認識結果)を作成
    """
    def __call__(self, x):
        h1 = f.relu(self.l1(x))
        h2 = f.relu(self.l2(h1))
        y = self.l3(h2)
        return y
"""
processing関数では、main関数でカメラ映像の取り組みを行った画像imgを
引数として、認識を行いやすいように変数を行った画像を出力
カメラ映像の取得範囲は、中央の100×100ピクセルの部分を切り抜く
切り抜いた画像をMNISTにデータセットと同じ入力形式に変換
cvw.cvtColotでグレイスケール化
cv2.GaussianBlurで手書き数字の画像のノイズを平滑化処理を行い実行
(3,3)はカーネルサイズ
次に、imgを28×28ピクセルに縮小
cv2.threshold()で閾値処理を実行し、閾値1以上の値なら閾値2に値を変更
imgは単浮動小数32とした後に、255で割る
その後、28×28の配列から、1×784の形状に変更する
"""
def processing(img):
    img = img[190:290, 270:370]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (28, 28))
    res, img = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY_INV)
    img = img.astype(np.float32) / 255
    img = np.array(img).reshape(1, 784)
    return img
"""
main()では、以下の処理を行う
model=MyMLP()で学習モデルを作成
serializers.load_npzで学習モデルの読み込み
cv2.rectangle()で赤色の四角形を作成
"e"を押すと、赤色の四角形のなかでprocessing(image)を実行する
num.dataで0から9のそれぞれの数字に対する認識結果
np.argmin(num.data)で最も確率の高い数字をコンソールに表示
出力では、10個のデータが入った配列とそれに対応する数字が出力
これは、[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]に対する値が格納
その配列のインデックスをnp.argmin()で出力
"""
def main():
    model = MyMLP()
    serializers.load_npz("../openml/mymodel.npz", model)
    capture = cv2.VideoCapture(0)
    if capture.isOpened() is False:
        raise("IO Error")

    while True:
        ret, image = capture.read()
        if ret == False:
            continue

        cv2.rectangle(image, (269,189), (371,291), (0,0,255), 1)
        cv2.imshow("Capture", image)
        k = cv2.waitKey(10)

        if k == ord("e"):
            img = processing(image)
            num = model(img)
            print(num.data)
            print(np.argmin(num.data))

        if k == ord("q"):
            break
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()