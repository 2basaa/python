import random
import matplotlib.pyplot as plt

delta = 1
p = 0.1
count_list = []

for attempts in range(100000):#100000回試行
    number = random.randrange(10)
    while number != 0:#到着間隔deltaを求める。
        delta += 1
        number = random.randrange(10)
    count_list.append(delta)
    delta = 1

delta_list = []
delta_len_list = []

for num in range(1, 101):
    count = [count_list[i] for i in range(100000) if count_list[i] == num]
    delta_list.append(num)
    delta_len_list.append((len(count)/10000)*p)
    
print(delta_len_list)
print(delta_list)

plt.plot(delta_len_list, delta_list, label="p")
#plt.xscale("log")
plt.legend()
plt.show()