def selectoon_sort(A):
    for i in range(0,len(A)-1):
        min = A[i]
        index = i
        for j in range(i+1, len(A)):
            if min > A[j]:
                min = A[j]
                index = j
        tmp = A[index]
        A[index] = A[i]
        A[i] = tmp

A = [31,41,59,26,41,58]
print(A)
selectoon_sort(A)
print(A)