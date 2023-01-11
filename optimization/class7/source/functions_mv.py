import numpy as np
import math

m_epsilon = np.finfo(dtype=np.float32).eps
epsilon = m_epsilon*2

dimensions=10

x_eps = np.zeros((dimensions,1)) # ERROR
y_eps = np.zeros((dimensions))

##################################
# sum(x^2)
##################################
def squared_f(x): 
    return np.sum(np.array([x[x_i]**2 for x_i in range(x.shape[0])]))

def squared_df_analytic(x):
    return 2*x

def squared_h_analytic(x):
    N = x.shape[0]
    shape = (N, N)
    H = np.full(shape, 0.)    
    for dim in range(N):
        H[dim,dim] = 2.0
    return H    

##################################
# Rastrigin
##################################
def rastrigin(x, n=None, A=10.):
    if n is None:
        n = x.shape[0]
    return A*n + np.sum(x**2 - A*np.cos(2*np.pi*x))

def rastrigin_df_analytic(x, A=10.):
    return 2*x + A*np.sin(2*np.pi*x)*2*np.pi

def rastrigin_h_analytic(x, A=10.):
    N = len(x)
    H = np.zeros((N,N))
    for i in range(N):
        H[i,i] = 2.0 + A*4.0*np.pi**2 * np.cos(2*np.pi*x[i,0])
    return H

##################################
# numerical gradient generic functions
##################################　　
def gradient(x, f): 
    #print("mv gradient")
    gradient = np.empty(x.shape)
    for i in range(len(x)): 
        x_eps = np.zeros(x.shape)
        x_eps[i] = epsilon
        # calculate by central difference
        partial_gradient = (f(x + x_eps) - f(x - x_eps))/(2.*epsilon)
        gradient[i] = partial_gradient
    return gradient

def hessian(x, f): 
    dimensions = x.shape[0]
    H = np.empty((dimensions, dimensions))
    for i in range(dimensions):
#        x_eps = np.zeros((dimensions,1))  ERROR
        x_eps = np.zeros((dimensions))
        x_eps[i] = epsilon
        # calculate by central difference
        row_gradient = (gradient(x + x_eps, f) - gradient(x - x_eps, f))/ \
             (2.*epsilon)
        H[i,:] = row_gradient.T
    return H

##################################
# Rosenbrock
##################################
def rosenbrock(x, n=None):
    if n is None:
        n = x.shape[0]
    y = 0.0
    for i in range(n-1):
        y += 100*(x[i+1] - x[i]**2)**2 + (1 - x[i])**2
        
    return y

##################################
# Styblinski - Tang
##################################
def styblinski(x, n=None):
    if n is None:
        n = x.shape[0]
    y = 0.0
    for i in range(n):
        y += pow(x[i],4) -16*pow(x[i],2) + 5*x[i]
        
    return 0.5*y

##################################
# Ackley
##################################
def ackley(x, n=None):
    a = 20
    b = 0.2
    c = 2*np.pi
    if n is None:
        n = x.shape[0]
    sum1 = 0.0
    sum2 = 0.0
    for i in range(n):
        sum1 += x[i]**2 
        sum2 += np.cos(c * x[i])
    t1 = -a * math.exp(-b * math.sqrt(sum1 / n))    
    t2 = -math.exp( sum2 / n)
    
    return t1 + t2 + a + math.exp(1)