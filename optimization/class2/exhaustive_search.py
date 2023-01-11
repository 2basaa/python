#exhaustive_search
import matplotlib.pyplot as plt
import numpy as np

def sin(x):
    return np.sin(x)

def p3d(x):
    return np.sin(x**3 - 5*(x+0.1)**2) / (x**3 + (x+0.1)**-2)

def exhaustive_search(f, xmin, xmax, delta):
    points = []
    fvalues = []
    x = xmin
    fx = f(x)
    fbest = fx
    xbest = x

    while x < xmax:
        points.append(x)
        fvalues.append(fx)

        x = x + delta
        fx = f(x)
        if x <= xmax:
            if fx > fbest:
                fbest = fx
                xbest = x
        print("f({}): {}".format(x, fx))

    print("best f({}): {}".format(xbest, fbest))

    return points, fvalues, xbest, fbest

#f = sin
f = p3d
xmin = 0
xmax = 1*np.pi
delta = 0.01

points, fvalues, xbest, fbest = exhaustive_search(f, xmin, xmax, delta)
points = np.array(points)
fvalues = np.array(fvalues)
   
x = np.arange(xmin, xmax, 0.01)

plt.plot(x, f(x))
plt.plot(points, fvalues, 'ro')
plt.plot(points[0], fvalues[0], 'bo')
plt.plot(xbest, fbest, 'ko')
plt.title('exhaustive_search')
plt.show()