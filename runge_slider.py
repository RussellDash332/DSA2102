from dsa2102 import *

"""
runge_slider.py

Observe the Runge phenomenon as we query various number of nodes to interpolate a certain function.
Compare the even-spaced interpolating function with the Chebyshev interpolating function.
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
    return exp(abs(x))

even_nodes, chebyshev_nodes = even(-1, 1, 11), chebyshev(-1, 1, 11)
coefs_even = newtdd(even_nodes, list(map(f, even_nodes)))
coefs_chebyshev = newtdd(chebyshev_nodes, list(map(f, chebyshev_nodes)))

seps = 100
dots = [i/seps for i in range(-seps, seps + 1)]

# The initial plotting setup
'''
plt.figure(figsize=(16, 9))
plt.scatter(even_nodes, list(map(f, even_nodes)))
plt.plot(dots, list(map(lambda x: Newtonpolynomial(coefs_even, x, even_nodes), dots)))
plt.scatter(chebyshev_nodes, list(map(f, chebyshev_nodes)))
plt.plot(dots, list(map(lambda x: Newtonpolynomial(coefs_chebyshev, x, chebyshev_nodes), dots)))
plt.show()
'''

# Use slider instead for flexibility!
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.175)

nodes_slider = Slider(
    ax=plt.axes([0.12, 0.075, 0.78, 0.03]),
    label='Nodes',
    valmin=2,
    valmax=40,
    valinit=11,
    valstep=1
)

def update(val):
    global fig, ax
    ax.clear()
    even_nodes, chebyshev_nodes = even(-1, 1, int(nodes_slider.val)), chebyshev(-1, 1, int(nodes_slider.val))
    coefs_even = newtdd(even_nodes, list(map(f, even_nodes)))
    coefs_chebyshev = newtdd(chebyshev_nodes, list(map(f, chebyshev_nodes)))
    ax.scatter(even_nodes, list(map(f, even_nodes)))
    ax.plot(dots, list(map(lambda x: Newtonpolynomial(coefs_even, x, even_nodes), dots)))
    ax.scatter(chebyshev_nodes, list(map(f, chebyshev_nodes)))
    ax.plot(dots, list(map(lambda x: Newtonpolynomial(coefs_chebyshev, x, chebyshev_nodes), dots)))
    fig.show()

nodes_slider.on_changed(update)
ax.scatter(even_nodes, list(map(f, even_nodes)))
ax.plot(dots, list(map(lambda x: Newtonpolynomial(coefs_even, x, even_nodes), dots)))
ax.scatter(chebyshev_nodes, list(map(f, chebyshev_nodes)))
ax.plot(dots, list(map(lambda x: Newtonpolynomial(coefs_chebyshev, x, chebyshev_nodes), dots)))
fig.show()