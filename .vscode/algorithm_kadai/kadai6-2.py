import math
def max_heapify(a, i, heap_size): 
    l = 2 * i
    r = 2 * i+ 1
    if l <= heap_size and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest, heap_size)

def build_max_heap(a):
    heap_size = len(a) - 1
    for number1 in range(math.floor(heap_size / 2), 0, -1):
        max_heapify(a, number1, heap_size)
    return heap_size

def heapsort(a):
    heap_size = build_max_heap(a)
    for number2 in range(heap_size, 1, -1):
        a[1], a[number2] = a[number2], a[1]
        heap_size = heap_size - 1
        max_heapify(a, 1, heap_size)

a = [-1, 9, 8, 1, 3, 6, 10] 
print(a) 
heapsort(a) 
print(a) 
a = [-1, 5, 13, 2, 25, 7, 17, 20, 8, 4]
print(a)
heapsort(a)
print(a)