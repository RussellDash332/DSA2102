from dsa2102 import *

"""
tridiag.py

Just a function to print the square matrix as shown below. Can handle various sizes.
"""

def tridiag(n):
    """
    Returns a tridiagonal nxn matrix where nonzero elements are 1.
    """
    mat = []
    for i in range(n):
        row = [0]*n
        for j in range(max(i-1,0),min(i+2,n)):
            row[j] += 1
        mat.append(row)
    return np.array(mat)

print(tridiag(10))

"""
[[1 1 0 0 0 0 0 0 0 0]
 [1 1 1 0 0 0 0 0 0 0]
 [0 1 1 1 0 0 0 0 0 0]
 [0 0 1 1 1 0 0 0 0 0]
 [0 0 0 1 1 1 0 0 0 0]
 [0 0 0 0 1 1 1 0 0 0]
 [0 0 0 0 0 1 1 1 0 0]
 [0 0 0 0 0 0 1 1 1 0]
 [0 0 0 0 0 0 0 1 1 1]
 [0 0 0 0 0 0 0 0 1 1]]
"""