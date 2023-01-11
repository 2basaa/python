import math
def calculation(number):
    return math.factorial(number)
number = int(input())
print(calculation(number))
number = 0
for i in range(8):
    number += 1
    print(calculation(number))