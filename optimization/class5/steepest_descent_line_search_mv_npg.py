import numpy as np

#steepest descent with line search for alpha
#multiple variables gradient
def steepest_descent_line_search(f, df, x0, x_min, x_max, alpha, max_iter):
    i = 0
    m_epsilon = np.finfo(dtype=np.float32).eps
    tolerance = m_epsilon * 2

    xk = x0
    explored = [xk]
    evaluation = [f(xk)]
    #change:call  gradient(x,f(x)) with 2 parameters
    dk = -df(xk, f)
    #change:compute the norm of the gradient vector
    norm1_dk = np.linalg.norm(dk, ord=1)

    n_search = 20
    alpha_ls = alpha * np.arange(1.0/n_search, 1+1.0/n_search, 1.0/n_search)
    print("Alpha values considered")
    print(alpha_ls)

    within_range = True
    #chnage:the norm of the gradient vector is compared to tolerance
    while i <= max_iter and norm1_dk >= tolerance and within_range:
        #line_search alpha
        x_ls = []
        fx_ls = []
        for a in alpha_ls:
            explore_xk = xk + dk * a
            #change all elements of explore_xk must be within the range
            ge_xmin = np.greater_equal(explore_xk, x_min)#explore_xk>=x_min
            le_xmax = np.less_equal(explore_xk, x_max)#explore_xk <= x_max
            if ge_xmin.all() and le_xmax.all() :
                x_ls.append(explore_xk)
                fx_ls.append(f(explore_xk))

        if (len(x_ls) > 0):
            #convert to a numpy array
            a_fx_ls = np.array(fx_ls)
            #get the index where fx is the smallest
            j = np.argmin(a_fx_ls)
            xk = x_ls[j]
            explored.append(xk)
            f_xk = fx_ls[j]
            evaluation.append(f_xk)
            #change: call gradient(x,fx) with 2 parameters
            dk = -df(xk, f)
            #change:compute the norm of the gradient vector
            norm1_dk = np.linalg.norm(dk, ord=1)
            #change: output format
            sout = "---iter {}\n x     = {}\n  f(x)   = {:.2e}\n -df(x) = {}\n"
            sout = sout + " norm1 = {:.2e}\n alpha = {}"
            print(sout.format(i, xk, f_xk, dk, norm1_dk, alpha_ls[j]))
            i += 1
        else:
            within_range = False
            print("Out of range")
    
    print("tolerance = {:.3e}".format(tolerance))
    return explored, evaluation