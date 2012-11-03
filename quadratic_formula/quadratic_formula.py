#!/usr/bin/python2.7
""" 
    quadratic formula example. plain and simple
"""
import math
import cmath

def quad(a,b,c):
    """ solves quadratic equations of the form aX^2+bX+c for
        real or complex.
    Args:
        a (int): a value
        b (int): b value
        c (int): c value
    """
    value = b**2 - 4*a*c
    if value < 0:
        x1 = (-b+cmath.sqrt(value)) / 2*a
        x2 = (-b-cmath.sqrt(value)) / 2*a
        return x1,x2
    else:
        x1 = (-b+math.sqrt(value)) / 2*a
        x2 = (-b-math.sqrt(value)) / 2*a
        return x1,x2

if __name__ == '__main__':
    print quad(1,1,-2)
    print quad(1,1,-6)
    print quad(1,1,-10)

