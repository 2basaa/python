#heap = 2本木
def left(number):
    #左側の枝
    return 2 * number + 1

def right(number):
    #右側の枝
    return 2 * (number + 1) 

def max_heapify(data, number):
    #left_number=奇数
    left_number = left(number)
    #right_number=偶数
    right_number = right(number)
    #left_numberがのdataの数以下and
    #上の点部分が点の枝分かれした左側よりも小さい
    if left_number <= len(data) and \
    data[left_number] > data[number]:
        #最大インデックスを左側のインデックスにする
        largest = left_number
    else:
        #上の点部分が点の枝分かれした左側よりも大きい
        #最大インデックスを上のインデックスにする
        largest = number
    #right_numberがdataの数以下and
    #上の点の部分が枝分かれした右側よりも小さい
    if right_number < len(data) and \
    data[right_number] > data[largest]:
    #最大インデックスを右側のインデックスとする
        largest = right_number
    if largest != number:
        max_number = data[largest]
        data[largest] = data[number]
        data[number] = max_number
        #print(largest)
        max_heapify(data, largest)

def build_max_heap(data):
    #dataの数の半分の数
    half_size = len(data) // 2 - 1
    #4~0まで行う。
    for number in range(half_size, -1, -1):
        print("count = " + str(number))
        max_heapify(data, number)
        print(data)
        
#data = [16, 4, 10, 14, 7, 9, 3, 2, 4, 1]
data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
build_max_heap(data)