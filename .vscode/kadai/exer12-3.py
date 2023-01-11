import math
def calculation(count):
    e = 1
    for number in range(1, count + 1): 
        e += (1 / math.factorial(number))
    return e

count = int(input())
print(calculation(count))