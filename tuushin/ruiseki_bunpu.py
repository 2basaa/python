# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:47:10 2022

@author: swim3
"""

import numpy as np
import matplotlib.pyplot as plt

lamda=1
sample=100000
u_data=np.random.rand(sample)
u_data.sort()
result_data=-(1/lamda)*np.log(1-u_data)
x=result_data
x.sort()
print(sum(x))

#y=[(1-np.exp(-lamda*i))/(1-np.exp(-lamda)) for i in x]
y=[1-np.exp(-lamda*i) for i in x]
#y=[1-np.exp(-lamda*i) for i in x]
print(sum(x)/sample)
#print(1-(sum(y)/sample))
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(x,y)
plt.plot(result_data,u_data)
plt.xlabel("$Uniform-random$", size=12)
plt.ylabel("$probability$", size=12)
plt.show()