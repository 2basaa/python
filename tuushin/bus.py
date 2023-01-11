import random
import matplotlib.pyplot as plt
import math

bus_lam = 1#バスラムダ
passenger_lam = 20#乗客ラムダ
e = math.e#ネイピア数
bus_arrival = 0
passenger_arrival = 0
u_list = []
bus_time_list = []
passenger_time_list = []
passenger_t = 0
passenger_count = 0
passenger_count_list = []
bus_t = 0
num = 20000
bus_count = 0
people = 0
people_list = []
passenger_num = 0
wait_time = 0
time_list = []
bus_list = []

for i in range(num):
    random_number = random.random()
    u_list.append(random_number)

bus_x_list = [-(1/bus_lam)*math.log(1-u) for u in u_list]#バスの指数分布の乱数
passenger_x_list = [-(1/passenger_lam)*math.log(1-u) for u in u_list]#乗客の指数分布の乱数

'''
for bus_x in bus_x_list:
    bus_time = bus_x
    bus_time_list.append(bus_time)

for passenger_x in passenger_x_list:
    passenger_time = passenger_x 
    passenger_time_list.append(passenger_time)
'''

while bus_count < 500:
    if bus_x_list[bus_count] > passenger_num:
        wait_time = bus_x_list[bus_count] -  passenger_x_list[passenger_count]
        time_list.append(wait_time)
        passenger_num += passenger_x_list[passenger_count]
        passenger_count += 1
        people += 1
    elif bus_x_list[bus_count] <= passenger_num:
        bus_count += 1
        bus_list.append(bus_count)
        people_list.append(people)
        people = 0
        passenger_num = 0

#plt.scatter(bus_x_list[0:500], people_list)
#plt.show()

print(passenger_count)
############実験1####################
passenger_number = 0
for i in range(500):#500はバスの本数
    passenger_number += people_list[i]
average_passenger_number = passenger_number / 500
'''
plt.scatter(bus_list, people_list)
plt.xlabel("bus number")
plt.ylabel("passenger number")
plt.show()
'''
print(average_passenger_number)

#############実験2####################
relative_passenger_number = 0
relative_list =[]
for i in range(500):
    relative_passenger_number += (pow(people_list[i], 2))
    relative_list.append(pow(people_list[i], 2))
print(relative_passenger_number/passenger_number)
'''

plt.bar(bus_list, people_list)
plt.xlabel("bus number")
plt.ylabel("realtively passenger number")
plt.show()
print(relative_passenger_number/passenger_number)
'''
############実験3#####################
#print(time_list)
'''
plt.scatter(passenger_x_list[0:passenger_count], time_list)
plt.show()
'''