from scipy.optimize import leastsq
import scipy as sc
import numpy as np
import matplotlib.pyplot as plt

# With "optimize.curve_fit" the code is simpler, there is no need to define the "residual(error) function".

fig, ax = plt.subplots()
# data
x = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
y = np.array([6.008, 15.722, 27.130, 33.772, 5.257, 9.549, 11.098, 28.828])

# modeling functions
def funcLine(x, a, b):
    return a*x+b


def funcQuad(x, a, b, c):
    return a*x**2+b*x+c


# optimize constants for the linear function
constantsLine, _ = sc.optimize.curve_fit(funcLine, x, y)

X = np.linspace(x.min(), x.max(), 50)
Y1 = funcLine(X, *constantsLine)

# optimize constants for the quadratic function
constantsQuad, _ = sc.optimize.curve_fit(funcQuad, x, y)


Y2 = funcQuad(X, *constantsQuad)
plt.plot(X, Y1, 'r-', label='linear approximation')
plt.plot(x, y, 'bo', label='data points')
# plt.plot(X, Y2, 'g-', label='quadratic approximation')
# matplotlib.pylab.legend()
ax.set_title("Nonlinear Least Square Problems", fontsize=18)
plt.show()