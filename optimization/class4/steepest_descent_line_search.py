import numpy as np

#steepest descent with line search for alpha

def steepest_descent_line_search(f, df, x0, x_min, x_max, alpha, max_iter):
    i = 0
    m_epsilon = np.finfo(dtype=np.float32).eps
    tolerance = m_epsilon * 2

    xk = x0
    explored = [xk]
    evaluation = [f(xk)]
    dk = -df(xk)

    n_search = 20
    alpha_ls = alpha * np.arange(1.0/n_search, 1+1.0/n_search, 1.0/n_search)
    print("Alpha values considered")
    print(alpha_ls)

    within_range = True
    while i <= max_iter and abs(dk) >= tolerance and within_range:
        #line_search alpha
        x_ls = []
        fx_ls = []
        for a in alpha_ls:
            if (xk + dk * a > x_min) and (xk + dk * a < x_max):
                x = xk + dk * a
                x_ls.append(x)
                fx_ls.append(f(x))

        if (len(x_ls) > 0):
            #convert to a numpy array
            a_fx_ls = np.array(fx_ls)
            #get the index where fx is the smallest
            j = np.argmin(a_fx_ls)
            xk = x_ls[j]
            explored.append(xk)
            f_xk = fx_ls[j]
            evaluation.append(f_xk)
            dk = -df(xk)
            sout = "iter {}, f({:.3e})= {:.3e}, -df(x)= {:.3e}, alpha = {:.3e}"
            print(sout.format(i, xk, f_xk, dk, alpha_ls[j]))
            i += 1
        else:
            within_range = False
            print("Out of range")
    
    print("tolerance = {:.3e}".format(tolerance))
    return explored, evaluation