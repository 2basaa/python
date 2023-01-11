import numpy as np

def newton_line_search(f, df, df2, x0, x_min, x_max, max_iter, alpha, n_ls):
    i = 0#iteration number
    m_epsilon = np.finfo(dtype=np.float32).eps
    tolerance = m_epsilon * 2

    xk = x0
    explored = [xk]
    f_xk = f(xk)
    evaluation = [f_xk]
   
    J = df(xk, f)#Gradient vector
    H = df2(xk, f)#Hessian matrix
    dk = -1*np.dot(np.linalg.pinv(H), J)#new step
    norm1_dk = np.linalg.norm(dk, ord=1)
    sout = "---iter{}\n x     = {}\n f(x)  = {:.2e}\n dk = -H^-1:J = {}\n"
    sout = sout + "J=df(x)= {}\n H=df2(x)= {}\n norm1 = {:.2e}\n"
    print(sout.format(i, xk, f_xk, dk,df(xk, f), df2(xk, f), norm1_dk))

    alpha_ls = alpha * np.arange(1.0/n_ls, 1+1.0/n_ls, 1.0/n_ls)
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
            #all elements of explore_xk must be within the range
            for j in range(len(explore_xk)):
                if explore_xk[j] < x_min[j]:
                    explore_xk[j] = x_min[j] + tolerance
                if explore_xk[j] > x_max[j]:
                    explore_xk[j] = x_max[j] - tolerance
            x_ls.append(explore_xk)
            fx_ls.append(f(explore_xk))

        #convert to a numpy array
        a_fx_ls = np.array(fx_ls)
        #get the index where fx is the smallest
        j = np.argmin(a_fx_ls)
        xk = x_ls[j]
        print("alpha = ", alpha_ls[j])
        explored.append(xk)
        f_xk = fx_ls[j]
        evaluation.append(f_xk)

        J = df(xk, f)#Gradient vector
        H = df2(xk, f)#Hessian matrix
        dk = -1*np.dot(np.linalg.pinv(H), J)#new step
        norm1_dk = np.linalg.norm(dk, ord=1)
        i += 1
        sout = "---iter{}\n x   = {}\n f(x)  = {:.2e}\n dk = -H^-1:J = {}\n"
        sout = sout + "J=df(x)= {}\n H=df2(x)= {}\n norm1 = {:.2e}\n"
        print(sout.format(i, xk, f_xk, dk,df(xk, f), df2(xk, f), norm1_dk))

    return explored, evaluation