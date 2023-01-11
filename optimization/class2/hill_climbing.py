#hill_climbing.py
import matplotlib.pyplot as plt
import numpy as np

def sin(x):
    return np.sin(x)

def p3d(x):
    return np.sin(x**3 - 5*(x+0.1)**2) / (x**3 + (x+0.1)**-2)

def hill_climbing(f, x0, delta, xmin, xmax):
    evaluations = np.array([f(x0-delta), f(x0), f(x0+delta)])
    points = [x0]
    fvalues = [evaluations[1]]

    index_max = np.argmax(evaluations)

    sign = 1.0

    climb = True
    if  index_max == 0:
        sign = -1.0
    elif index_max == 2:
        sign = 1.0
    else:
        climb = False

    x = x0 + (sign*delta)
    fx = evaluations[index_max]
    fbest = fx

    while climb == True:
        points.append(x)
        fvalues.append(fx)

        x = x + (sign*delta)
        fx = f(x)
        if fx > fbest and (x <= xmax and x >= xmin):
            fbest = fx
            print("f({}): {}".format(x, fx))
        else:
            climb = False

    return points, fvalues

#f = sin
f = p3d
xmin = 0
xmax = 1*np.pi
x0 = 1.4
delta = 0.01

points, fvalues = hill_climbing(f, x0, delta, xmin, xmax)
points = np.array(points)
fvalues = np.array(fvalues)
   
x = np.arange(xmin, xmax, 0.01)

plt.plot(x, f(x))
plt.plot(points, fvalues, 'ro')
plt.plot(points[0], fvalues[0], 'bo')
plt.plot(points[len(points) - 1], fvalues[len(fvalues) - 1], 'ko')
plt.title('hill_climbing')
plt.show()