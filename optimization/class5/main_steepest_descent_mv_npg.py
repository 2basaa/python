import numpy as np
import matplotlib.pyplot as plt
#import steepest_descent_mv_npg as sd
import steepest_descent_line_search_mv_npg as sdls
import functions_mv as fun

np.set_printoptions(precision=2)

# number of variables, dimesion of search space
n = 10

x_min = np.array([-3]*n)
x_max = np.array([3]*n)
#np.random.seed(7)


#set starting port for search
#x0 is a numpy of dimention n
x0 = np.random.rand(n)*(x_max - x_min) + x_min
print(x0)


#f = fun.squared_f


f = fun.rastrigin

df = df = fun.gradient


alpha = 9e-3
max_iter = 200
#explored_xk, evaluated_xk = sd.steepest_descent(f, df, x0, x_min, x_max, alpha, max_iter)
explored_xk, evaluated_xk = sdls.steepest_descent_line_search(f, df, x0, x_min, x_max, alpha, max_iter)

xx = np.arange(x_min[0], x_max[0], 0.01)
xxx = []
for e in xx:
    xxx.append(np.array([e]*n))
fff = [f(e) for e in xxx]
i = 0
x_ = [x[i] for x in xxx]
plt.plot(x_, fff)

x_ = [x[i] for x in explored_xk]

plt.scatter(x_ ,evaluated_xk,  color="g")
#plt.plot(x_, evaluated_xk, color="g")
plt.scatter(x_[0], evaluated_xk[0], color="b")
i_xstar = len(x_)-1
plt.scatter(x_[i_xstar], evaluated_xk[i_xstar], color="r")
plt.show()
