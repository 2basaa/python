#!python3.7
# -*- coding: utf-8 -*-  
import numpy as np 
import random 
import matplotlib.pyplot as plt 

np.set_printoptions(precision=4) 
m_epsilon = np.finfo(dtype=np.float32).eps 
epsilon = m_epsilon*20 
tolerance = m_epsilon*2 
################################## 
# numerical gradient generic functions 
##################################　　 
def jacobian(x, f, rho):  
    gradient = np.empty(x.shape) 
    for i in range(len(x)):  
        x_eps = np.zeros(x.shape) 
        x_eps[i] = epsilon 
        # calculate by central difference 
        f_xplus = f(x + x_eps, rho) 
        f_xminus = f(x - x_eps, rho) 
        partial_gradient = (f_xplus - f_xminus)/(2.*epsilon)
        gradient[i] = partial_gradient 
    return gradient

def hessian(x, f, rho): 
    dimensions = x.shape[0] 
    H = np.empty((dimensions, dimensions)) 
    for i in range(dimensions): 
        x_eps = np.zeros((dimensions,1)) 
        x_eps[i] = epsilon 
        # calculate by central difference 
        j_xplus = jacobian(x + x_eps, f, rho) 
        j_xminus = jacobian(x - x_eps, f, rho) 
        row_gradient = (j_xplus - j_xminus)/(2.*epsilon) 
        H[i,:] = row_gradient.T 
    return H  
################################## 
# sum(x^2) + all variables have to be positive > 1 
################################## 
def squared(x):  
    return np.sum(np.array([x[x_i]**2 for x_i in range(x.shape[0])])) 

def squared_interior_penalty(x, rho):  
    g_i = np.array([max(1, x[x_i][0]) for x_i in range(x.shape[0])]) 
    penalty = np.sum(1.0/(g_i**2))  
    return squared(x) + rho*penalty 

def squared_j(x, rho): 
    return jacobian(x, squared_interior_penalty, rho) 

def squared_h(x, rho): 
    return hessian(x, squared_interior_penalty, rho) 
# multidimensional newton 
# notes: 
# * using the approximated Moore-Penrose inverse (A+) 
# - to avoid singularities when the matrix determinant is 0
# * the inverse can also be approximated via Gaussian elimination  
def newton_m(f, df, df2, initial_value, max_iterations, rho):
    iteration = 0 
    iteration_ks = [] 
    x_k = initial_value 
    J = df(x_k, rho) # Jacobian 
    H = df2(x_k, rho) # Hessian 
    d_k = np.dot(-np.linalg.pinv(H), J) # new step 
    while True: 
        iteration_ks.append(x_k) 
        x_k = x_k + d_k 
        J = df(x_k, rho) 
        H = df2(x_k, rho) 
        d_k = np.dot(-np.linalg.pinv(H), J) 
        iteration += 1 
        step_norm = np.linalg.norm(d_k, ord=1)  
        if step_norm <= tolerance: break 
        if iteration >= max_iterations: break 
    return x_k, iteration_ks  
################################## 
# squared function configurations 
################################## 
f_penalty = squared_interior_penalty 
function = squared 
df = squared_j 
df2 = squared_h 
max_iterations = 20 
random_seed = 777 
random.seed(random_seed) 
np.random.seed(random_seed) 
dimensions = 1 
initial_value = np.random.rand(dimensions,1)+3 
################################## 
# solve with newton  
# as incrementing the penalty coefficient "rho" 
# by a gamma factor 
################################## 
print("initial_value =", initial_value) 
rho = 10 
gamma = 5.0 
tolerance = 1e-2 
x_i = initial_value 
x_star = x_i 
x_star_list = [] #save found solutions 
for i in range(max_iterations):  
    x_star, iteration_ks = newton_m(f_penalty, df, df2, x_i, 1, rho) 
    x_star_list.append(x_star) 
    step_norm = np.linalg.norm(x_i - x_star, ord=1) 
    if step_norm <= tolerance: break 
    print("iteration {}".format(i+1)) 
    print("x* = {}".format(x_i)) 
    print("f(x) = {}".format(function(x_star))) 
    print("penalty f(x) = {}".format(f_penalty(x_star, rho)))  
    print("rho = %f" % rho) 
    x_i = x_star 
    rho *= gamma 
  
print("#"*10, "solution", "#"*10) 
print("x* =\n", x_star) 
print("f(x*) = {}".format(function(x_star))) 
print("penalty f(x*) = {}".format(f_penalty(x_star, rho))) 
if dimensions == 1: 
    # plot for only 1-d 
    xx = np.linspace(-4, 4) 
    yy = np.array([function(np.array([[x_n]]).T) for x_n in xx])  
    yy2 = np.array([f_penalty(np.array([[x_n]]).T, rho) for x_n in xx])  
    fig, ax1 = plt.subplots() 
    ax1.plot(xx,yy, "b-") 
    ax1.set_ylabel("original") 
    ax1.plot(initial_value, function(initial_value), "ob")  
    ax1.plot([float(xs) for xs in x_star_list],  
    [function(np.array([[xs]], dtype=np.float).T) for xs in x_star_list],  "ok") 
    ax2 = ax1.twinx() 
    ax2.plot(xx, yy2, "r-") 
    ax2.set_ylabel("with constraints") 
    ax1.plot(x_star, function(x_star), "or") 
    
    plt.tight_layout() 
    plt.show() 