#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
#クイックソートの実行
#先頭の２つ値の内大きい値を選ぶ
import time

#quicksortでは、基準値よりも大きい領域と基準値以下の領域で分ける。
#
def partition(data, start, end):
    citeriion_value = data[end]#データの最後の要素
    small_index = start - 1#最初はインデックス外とする
    #値を変換させるための場所をずらす
    #small_indexは値を変換させるためのインデックスとなる
    for big_index in range(start, end):
        if data[big_index] <= citeriion_value:
            small_index += 1#small_indexのポインタを1つずらす
            swap_value = data[small_index]#規準値とする。
            data[small_index] = data[big_index]
            data[big_index] = swap_value
            print(data)
    #インデックスの場所がsmall_index+1とendの場所の要素を入れ替える
    swap_value = data[small_index+1]
    data[small_index+1] = data[end]
    data[end] = swap_value
    return small_index + 1#small_index+1のインデックスを戻り値とする

def quick(data, start, end):
    if start < end:
        #small_index+1をmidとする
        mid = partition(data, start, end)
        quick(data, start, mid-1)
        quick(data, mid + 1, end)#最後に使う。

data = [12, 3, 1, 13, 3, 45, 6, 7, 8]
end = len(data) - 1
start_time = time.time()
quick(data, 0, end)
end_time = time.time()
print(data)
print(end_time - start_time)