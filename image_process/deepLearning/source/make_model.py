#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import numpy as np
from chainer import Variable, optimizers, serializers
from chainer import Chain
import chainer.functions as f
import chainer.links as l
from sklearn.datasets import fetch_openml

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

#プログラムが開始したことを示す
print("Start")

"""
sklearn.datasets.fetch_openml関数でMNISTのデータセットをダウンロード
その値をmnist_X,mnist_Yに格納
openMLFolderにデータを格納する
"""
mnist_x, mnist_y = fetch_openml('mnist_784', version=1, parser='auto', return_X_y=True)

"""
mnistのデータセットは28×28ピクセルの手書き数字のグレイスケールが増70000枚と、
画像の数字に対応するラベルのセット
mnist_xに格納された画像をx_allに格納データをfloat32型に変更
正規化するために255で割る
mnist_yに数字のラベルが格納されているので、y_allに格納
その後、データ型をint32型に変更する
"""
#データはゲットできている
x_all = mnist_x.astype(np.float32) / 255
y_all = mnist_y.astype(np.int32)

"""
optimizerはパラメータを最適化する際に利用する
optimizerでは結合に対して数値的な最適化アルゴリズが実行
確率的勾配降下法と呼ばれる簡単なアルゴリズムである
optimizers.SGDコンストラクタを使用
optimizers.setup(model)関数で引数(model)に与えられた学習モデルを最適化するように設定
"""
model = MyMLP()
optimizer = optimizers.SGD()
optimizer.setup(model)

"""
optimizerの最適を行う最適化を行う学習ループを行う
MNISTのデータセットからランダムに数字を取得
np.random.permutation関数でDATASIZEをランダムに並び替えた配列をindexesに格納
順伝播計算、逆伝播計算を行うために、Variable(chainer.variable.Variable)オブジェクトに
変換した画像データを変数x、ラベルを変数Tに格納
loss.backwordで勾配を計算
model.zerograds()で前回のループで計算された勾配を0に初期化
modelの__call__を利用して順伝播計算を行い、f.sortmax_cross_entropy関数で
与えられた正解ラベルと予測との損失値を計算
loss.backword関数で逆伝播計算を実行
optimizer.update関数で逆伝播した結果をもとに最適化
以上の処理をループしてモデルの最適化を実行する
"""
BATCHSIZE = 100
DATASIZE = 70000

"""
データフレームに対して.ilocを使用しないと提示エラーが発生
また、numpyを渡すことが期待されているので、[].valuesとする
それによって、最適化された値を取得
"""
for epoch in range(20):
    print("epoch %d" % epoch)
    indexes = np.random.permutation(DATASIZE)
    for i in range(0, DATASIZE, BATCHSIZE):
        #print(indexes[i])
        x = Variable(x_all.iloc[indexes[i : i + BATCHSIZE]].values)
        t = Variable(y_all.iloc[indexes[i : i + BATCHSIZE]].values)

        model.zerograds()
        #y = model(x)
        #loss = f.softmax_cross_entropy(y, t)
        #loss.backword()

        optimizer.update()

serializers.save_npz("mymodel.npz", model)
#プログラムの終了
print("Finish")