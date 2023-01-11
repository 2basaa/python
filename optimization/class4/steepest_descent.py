import numpy as np

#steep descent with fixed step size
def steepest_descent(f, df, x0, x_min, x_max, alpha, max_iter):
    i = 0
    m_epsilon = np.finfo(dtype=np.float32).eps
    tolerance = m_epsilon * 2

    xk = x0
    explored = [xk]
    evaluation = [f(xk)]
    dk = -df(xk)
    within_range = True
    while i <= max_iter and abs(dk) >= tolerance and within_range:
        xk = xk + alpha * dk
        if xk > x_min and xk < x_max:
            explored.append(xk)
            f_xk = f(xk)
            evaluation.append(f_xk)
            dk = df(xk)
            sout = "iter {}, f({:.3e})= {:.3e}, -df(x)= {:.3e}, alpha = {:.3e}"
            print(sout.format(i, xk, f_xk, dk, alpha))
            i += 1
        else:
            within_range = False
            print("Out of range")
    
    print("tolerance = {:.3e}".format(tolerance))
    return explored, evaluation