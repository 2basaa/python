def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)

def partition(a, p, r):
    x = a[r]
    i = p - 1
    for figure in range(p, r):
        if a[figure] <= x:
            i = i + 1
            a[i], a[figure] = a[figure], a[i]
    a[i + 1], a[r]  = a[r], a[i + 1]
    return i + 1

a = [7, 8, 3, 10, 4, 1, 9, 6]
print(a)
quicksort(a, 0, len(a) - 1)
print(a)

a = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
print(a)
quicksort(a, 0, 11)
print(a)