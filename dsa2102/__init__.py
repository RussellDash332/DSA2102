import numpy as np
import matplotlib.pyplot as plt
from math import *
import csv, copy, time

# All of these codes will be provided during lecture. Copy them into the dsa2102/ directory.
# I won't put them here because it's the courtesy of Prof :-)
from .matMul import *

from .bisection import *
from .fixedpt import *
from .Horner import *

from .GaussianElmnt import *
from .GaussianElmntPP import *
from .GaussianElmntSPP import *

from .LU import *
from .PALU import *

from .Cholesky import *

from .Jacobi import *
from .GaussSeidel import *
from .SOR import *

from .newtdd import *
from .Newtonpolynomial import *

from .QR import *

def read_csv(csvfilename):
    """
    Converts a CSV file to a float array.
    """
    rows = []
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(list(map(float, row)))
    return rows

def read_matrix(csvfilename):
    """
    Converts a CSV file to a numpy float array.
    """
    rows = []
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(list(map(float, row)))
    return np.array(rows)