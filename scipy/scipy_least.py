import random
from scipy.optimize import least_squares


a, b = random.randint(1, 1000), random.randint(1, 1000)
print("Ground truth [a, b]: ", [a, b])


def f(args):
    x, y = args
    print(x, y)
    return (x-a)**2 + (y-b)**2


x0 = [0, 0]
result = least_squares(fun=f, x0=x0)
# print(result)
print("Estimated [a, b]: ", result.x)
