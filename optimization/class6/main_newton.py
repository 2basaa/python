import numpy as np
import matplotlib.pyplot as plt
import newton_linear_search as nm
import functions5_mv as fun

np.set_printoptions(precision=2)
#np.random.seed(7)

#number of variables, dimension of searchh space
n = 3
x_min = np.array([-5]*n)
x_max = np.array([5]*n)

# set starting point for search
# x0 is a numpy array of dimention n
x0 = np.random.rand(n)*(x_max-x_min) + x_min

#Select a function to optimize
#f = fun.squared_f
#f = fun.rastrigin
#f = fun.rosenbrock
f = fun.styblinski #-5, 5
#f = fun.ackley #-5, 5

#set the gradient and hessian functions
df = fun.gradient
df2 = fun.hessian

#set max number of iterations, alpha and number of points for linear search
max_iter = 100
alpha = 1
n_ls = 1 #number of points to sample alpha for linear search
exp_xk, f_exp_xk = nm.newton_line_search(f, df, df2, x0, x_min, 
                                    x_max, max_iter, alpha, n_ls)

print(exp_xk)
print(f_exp_xk)
#plot f and variable x1(x[0]) of an equally distanced sample of points
x_min_max_sample = np.arange(x_min[0], x_max[0], 0.1)
x_sample_plot = []
for e in x_min_max_sample:
    x_sample_plot.append(np.array([e]*n))
f_x_sample_plot = [f(e) for e in x_sample_plot]
x_ = [x[0] for x in x_sample_plot]
plt.plot(x_, f_x_sample_plot)

#Plot f and variables x1, x2 and x3 of the explored points
i = 0
while i < 3 and i < n:
    x_i = [x[i] for x in exp_xk]
    plt.plot(x_i, f_exp_xk, color="g", linestyle='dashed', linewidth=1)
    plt.scatter(x_i[0], f_exp_xk[0], color="b")
    i_xstar = len(x_i) - 1
    plt.scatter(x_i[i_xstar], f_exp_xk[i_xstar], color="r")
    plt.text(x_i[0], f_exp_xk[0]+2, "$x_" + str(i+1) +"$",size=10)
    i += 1
plt.xlabel("$x$", size=12)
plt.ylabel("$f~(x)$", size=12)
plt.show()