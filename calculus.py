#!/usr/bin/python
"""
Cw5 the pinacle of groupwork and efficienceyc and comroodery

Calculus module implementing
discrete function function
differentiation function
and trapezoidal integration function

"""
import numpy as np
import math

def discrete_func(f, a, b, n):
    x = np.linspace(a, b, n+1)
    g = np.vectorize(f)
    y = g(x)
    return x, y


