#heap = 2本木
def left(number):
    return 2 * number - 1

def right(number):
    return 2 * number 

def max_heap(data, number):
    left_number = left(number)
    right_number = right(number)
    if left_number <= len(data) and \
    data[left_number] > data[number]:
        largest = left_number
    else:
        largest = number
    if right_number < len(data) and \
    data[right_number] > data[largest]:
        largest = right_number
    if largest != number:
        max_number = data[largest]
        data[largest] = data[left_number]
        data[left_number] = max_number
        max_heap(data, number)

def build_max_heap(data):
    half_size = len(data) // 2
    for number in range(half_size, 1, -1):
        max_heap(data, number)
    

data = [4, 3, 5, 7, 1, 8, 6, 2]
build_max_heap(data)
print(data)