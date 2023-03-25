#!C:\Users\Tsubasa\anaconda3\envs\py3108\python.exe
import math
import time

def merge(data, start , mid, end):
    #最初はstart=0, mid = 0, end = 1
    print(start, end)
    left_number = mid - start + 1#左側の開始インデックス
    right_number = end - mid#右側の開始インデックス
    left = []#左側の値
    right = []#右側の値
    for l_num in range(1, left_number + 1):
        #左側の値を格納
        left.append(data[start + l_num - 1])
    for r_num in range(1 ,right_number + 1):
        #右側の値を格納
        right.append(data[mid + r_num])
    left.append(math.inf)#リストの範囲外を防ぐため
    right.append(math.inf)#infより大きい数は存在しない
    print(left)
    print(right)
    left_number = 0#leftのインデックス
    right_number = 0#rightのインデックス
    for num in range(start, end + 1):#swap
        if left[left_number] <= right[right_number]:
            data[num] = left[left_number]
            left_number += 1
        else:
            data[num] = right[right_number]
            right_number += 1
    print(data)

def merge_sort(data, start, end):
    if start < end:
        mid = (end + start) // 2
        #↓やり続けている
        #endの値やstartの値を小さくしていく
        merge_sort(data, start, mid)#左側
        merge_sort(data, mid+1, end)#右側
        merge(data, start, mid , end)

data = [9,7,6,8,5,10,3,2, 7]
end = len(data) - 1
start = time.time()
merge_sort(data, 0, end)
end = time.time()
print(end - start)