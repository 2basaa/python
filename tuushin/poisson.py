import math
import numpy as np
import matplotlib.pyplot as plt

lam = 1#ラムダ
e = math.e#ネイピア数
num = 10000
sum  = 0

u_list = np.random.rand(num)
u_list.sort()
x_list =-(1/lam)*np.log(1-u_list)
#x_list.sort()

for i in range(num):
    sum += x_list[i]

average = sum / num
print(average)
plt.scatter(x_list, u_list)
plt.xlim(0, max(x_list))
plt.xlabel("random-data")
#plt.ylim(0, 1)
plt.show()
'''
height = [count_1,count_2,count_3,count_4,count_5]
left = [1, 2, 3, 4, 5]
ex = 0.1*count_1+0.3*count_2+0.5*count_3+0.7*count_4+0.9*count_5
print(ex)
plt.bar(left, height)
plt.show()
'''