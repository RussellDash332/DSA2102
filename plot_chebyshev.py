from dsa2102 import *

"""
plot_chebyshev.py

A simple plot for comparing a function with its Chebyshev interpolating polynomial.
"""

def even(a, b, num_nodes):
    """
    Returns num_nodes evenly spaced nodes in range [a, b].
    """
    # return [a + (b-a)*k/(num_nodes-1) for k in range(num_nodes)]
    return list(np.linspace(a, b, num_nodes))

def chebyshev(a, b, num_nodes):
    """
    Returns num_nodes Chebyshev nodes in range [a, b].
    """
    return [(a+b)/2 + (b-a)/2 * cos((k+0.5)*pi/num_nodes) for k in range(num_nodes)]

def f(x):
    """
    The interpolating function. Feel free to modify.
    """
    return np.exp(np.abs(x))

def plot_it(f, a, b, num_nodes):
    x = np.linspace(a, b, 20000)
    chn = chebyshev(a, b, num_nodes)
    dd = newtdd(chn, f(chn))
    # print('Divided differences coefficients:')
    # print(dd)
    plt.plot(x, f(x), c='r', label='Actual f')
    plt.plot(x, Newtonpolynomial(dd, x, chn), c='b', label='Chebyshev interpolating polynomial')
    plt.scatter(chn, f(chn), c='k', label='Chebyshev nodes')
    plt.legend()
    plt.show()

# plot_it(f, -2, 1, 4)
plot_it(lambda x: x * np.log(x + np.exp(x)), -0.5, 1, 4)