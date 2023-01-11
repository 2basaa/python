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

a = [-1, 2, 5, 7, 1, 3, 6, 4]
print(a)
max_heapify(a, 1, 7)
print(a)
a = [-1, 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
print(a)
max_heapify(a, 3, 14)
print(a)