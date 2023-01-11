import random
import time

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
    return

maxvalue = 999999
a = random_list(1000)
start_time = time.process_time()
insertion_sort(a)
end_time = time.process_time()
print(end_time-start_time)