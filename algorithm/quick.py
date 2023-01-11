#クイックソートの実行
#先頭の２つ値の内大きい値を選ぶ

def partition(data, start, end):
    citeriion_value = data[end]
    small_index = start - 1
    for big_index in range(start, end):
        if data[big_index] <= citeriion_value:
            small_index += 1
            swap_value = data[small_index]
            data[small_index] = data[big_index]
            data[big_index] = swap_value
    swap_value = data[small_index+1]
    data[small_index+1] = data[end]
    data[end] = swap_value
    print(data)
    return small_index + 1

def quick(data, start, end):
    if start < end:
        mid = partition(data, start, end)
        quick(data, start, mid-1)
        quick(data, mid + 1, end)

data = [12, 3, 1, 13, 3, 45, 6, 7, 8]
end = len(data) - 1
quick(data, 0, end)
print(data)