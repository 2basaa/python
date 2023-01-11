import numpy as np
import matplotlib.pyplot as plt
lamda=10
sample=100000
u_data=np.random.rand(sample)
u_data.sort()
result_data=-(1/lamda)*np.log(1-u_data)

#fig=plt.figure(facecolor="w")
#ax=fig.add_subplot(111)
#ax.hist(result_data, bins=100, density=True)
#ax.plot(np.arange(0,8,0.1), np.exp(-1*np.arange(0,8,0.1)))

plt.plot(result_data,u_data)
print(sum(result_data)/sample)
plt.xlabel("$random-value$", size=12)
#plt.ylabel("$$", size=12)
plt.xlim(0,max(result_data))
plt.ylim(0,1)
plt.show()