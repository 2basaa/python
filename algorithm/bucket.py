#整数版のバケットソート
import math
import time
import insert

def bucket_sort(data):
    length = len(data)
    #バケツを用意(バケツの数)
    bucket_list = [[] * number for number in range(length)]
    #ソート結果
    sort_ans = []
    for num in range(0, length):
        #math.floorは小数点切り捨て
        #それぞれのバケツの中に入っている個数
        bucket_list[math.floor(data[num] / 10)].append(data[num])
    for number in range(0, length):
        bucket_insert_data = bucket_list[number]
        #print(bucket_insert_data)
        #以下では、挿入ソートを行う。
        sort = insert.insert_sort(bucket_insert_data)
        sort_data = sort.ascending()#挿入ソートで昇順となる
        if sort_data != []:#sort_dataが空リストでない時
            for num in sort_data:
                sort_ans.append(num)
    return sort_ans#ソートされた結果

#バケツの数は10個なので、要素の最大数は10
start = time.time()
data = [9, 12, 26, 39, 94, 78, 68, 17, 23, 21, 72, 83, 50, 75, 6, 83]
sort_data = bucket_sort(data)
end = time.time()
print(sort_data)
print(end - start)