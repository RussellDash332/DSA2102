from dsa2102 import *

"""
romberg.py

Displays the Romberg integration table in a nice manner.
"""

def f(x):
    """
    The function to integrate.
    """
    # return 1/x**3
    if 0 <= x <= 1:
        return 1/(x**3 + 2)
    elif 1 <= x <= 2:
        return 1/(2*x**4 + 1)

def trapezoid(f, a, b, panels):
    """
    Composite Trapezoid Rule to calculate int_{a}^{b} f(x) dx with given number of panels.
    """
    h = (b - a)/panels
    y = list(map(f, np.linspace(a, b, panels + 1)))
    s = y[0] + y[panels]
    for i in range(1, panels):
        s += 2*y[i]
    return h/2 * s

def simpson(f, a, b, panels):
    """
    Composite Simpson Rule to calculate int_{a}^{b} f(x) dx with given number of panels.
    """
    h = (b - a)/(2*panels)
    y = list(map(f, np.linspace(a, b, 2*panels + 1)))
    s = y[0] + y[2*panels]
    for i in range(1, panels + 1):
        s += 4*y[2*i - 1]
        if i != panels:
            s += 2*y[2*i]
    return h/3 * s

def midpoint(f, a, b, panels):
    """
    Composite Midpoint Rule to calculate int_{a}^{b} f(x) dx with given number of panels.
    """
    h = (b - a)/panels
    s = 0
    y = np.linspace(a, b, panels + 1)
    for i in range(1, panels + 1):
        s += f((y[i] + y[i - 1]) / 2)
    return h * s

def romberg_table(f, a, b, n):
    """
    Construct the Romberg table given f, a, b, and the order to achieve, 2n.
    """
    assert n >= 1
    table = []
    for _ in range(n + 1):
        table.append(['']*(n + 1))
    table[0][0] = 'n'
    for i in range(1, n + 1):
        table[i][0] = i
        table[0][i] = f'R(n,{i})'
    for j in range(1, n + 1):
        for k in range(1, j + 1):
            if k == 1:
                table[j][k] = trapezoid(f, a, b, 2**(j-1))
            else:
                table[j][k] = (4**(k-1)*table[j][k-1] - table[j-1][k-1])/(4**(k-1) - 1)
    return table

def print_romberg(table):
    """
    Prints the Romberg table created by the romberg_table function
    """
    RJUST = 11
    RND_DIGIT = 5
    assert 2*RND_DIGIT <= RJUST
    m = len(table)
    for i in range(m):
        ret = ''
        for j in range(m):
            if j == 0:
                ret += str(table[i][j]).rjust(3)
            elif i == 0:
                ret += table[i][j].rjust(RJUST)
            elif table[i][j] == '':
                ret += ''.rjust(10)
            else:
                ret += str(round(table[i][j], RND_DIGIT)).rjust(RJUST)
        print(ret)
        if i == 0:
            print('-'*(len(ret) + 3))

# Romberg table for integral of 1/(x+3) dx from 0 to 4
print_romberg(romberg_table(lambda x: 1/(x+3), 0, 4, 5))
print('Actual value:', log(7/3))