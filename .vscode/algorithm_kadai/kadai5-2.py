import time
import random
#%matplotlib inline
import matplotlib.pyplot as plt

def random_list(number):
    figure_list = []
    for n in range(number):
        value = random.randint(0, maxvalue)
        figure_list.append(value)
    return figure_list
   
def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        k = j - 1
        while k >= 0 and a[k] > key:
            a[k + 1] = a[k]
            k = k - 1
            a[k + 1] = key

def mergesort(a,p,r):
    if p < r:
        q = (p+r) // 2
        mergesort(a,p,q)
        mergesort(a, q+1,r)

        n1 = q-p+1
        n2 = r-q
        L=[]
        R=[]
        for i in range(0,n1):
            L.append(a[p+i])
        for j in range(0,n2):
            R.append(a[q+j+1])
        L.append(1000000)
        R.append(1000000)
        i = 0
        j = 0
        for k in range(p, r+1):
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1

maxvalue = 999999
x = [500, 1000, 2000, 5000, 10000, 15000]
y1 = []
y2 = []
for figure in x:
    a = random_list(figure)
    start_time = time.process_time()
    insertion_sort(a)
    end_time = time.process_time()
    start_time2 = time.process_time()
    mergesort(a,0,len(a)-1)
    end_time2 = time.process_time()
    y1.append(end_time-start_time)
    y2.append(end_time2-start_time2)

plt.title("Time")
plt.ylabel("Time[s]")
plt.xlabel("Number of data")
plt.plot(x, y1, marker="o", label ="insertion_sort")
plt.plot(x, y2, marker="x", label="mergesort")
plt.legend()
plt.show()