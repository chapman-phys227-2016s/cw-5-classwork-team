#! /usr/bin/env python

"""
File: trapezoidal.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module uses three methods, iteration, vectorization, and matrix multiplication, to calculate
the integral of a function.

"""

import numpy as np

def trapezoidal(f, a, b, n):
    """Trapezoidal integration via iteration."""
    h = (b-a)/float(n)
    I = f(a) + f(b)
    for k in xrange(1, n, 1):
        x = a + k*h
        I += 2*f(x)
    I *= h/2
    return I

def trapezoidal_vectorized(f, a, b, n):
    """Trapezoidal integration via vectorization"""
    h = (b-a)/float(n)
    indexer = np.linspace(a, b, n)
    values = f(indexer)
    I = values.sum()
    I *=h
    I = I - (f(a) - f(b))(h/2.0)
    return I

def trapezoidal_matrix(f, a, b, n):
    """Trapezoidal integration via matrix multiplication."""
    h = (b-a)/float(n)
    indexer = np.linspace(a, b, n)
    values = f(indexer)
    matrixer = np.zeros(n)
    matrixer.fill(h)
    matrixer[0] = h/2.0
    matrixer[n - 1] = h/2.0
    I = np.dot(values, matrixer)
    return I

def test_trap_matrix():
    """Trapezoidal integration via matrix multiplication verified by integrating
    the sine function on the integral 0 to pi over 2."""
    apt = np.abs(trapezoidal_matrix(np.sin, 0, np.pi/2.0, 10000) - 1) < 1e-3
    msg = 'That aint how the sine do.'
    assert apt, msg