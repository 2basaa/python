import numpy as np
import random
import matplotlib.pyplot as plt
#import steepest_descent as sd
import steepest_descent_line_search as sdls
import functions_1v as fun

#random.seed(7)
x_min = -3
x_max = 3

#test rabdom generation
r = [random.random()*(x_max - x_min) + x_min for i in range(100)]
r.sort()
print(r)

#set starting port for search
x0 = random.random()*(x_max - x_min) + x_min

#'''
f = fun.squared_f
df = fun.squard_df_analytic
#'''


'''
f = fun.rastrigin
df = fun.rasstrigin_df_analytic
'''

alpha = 9e-3
max_iter = 100
#explored_xk, evaluated_xk = sd.steepest_descent(f, df, x0, x_min, x_max, alpha, max_iter)
explored_xk, evaluated_xk = sdls.steepest_descent_line_search(f, df, x0, x_min, x_max, alpha, max_iter)

xx = np.arange(x_min, x_max, 0.01)
plt.plot(xx, f(xx))

plt.scatter(explored_xk[:5],evaluated_xk[:5],  color="g")
plt.scatter(explored_xk[0], evaluated_xk[0], color="b")
i_xstar = len(explored_xk)-1
plt.scatter(explored_xk[i_xstar], evaluated_xk[i_xstar], color="r")
plt.show() 