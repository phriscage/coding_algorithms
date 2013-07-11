#!/usr/bin/env python
""" 
    Name: multiplication_algorithm.py
    Developer: Chris Page
    Purpose: multiple two numbers without using the built-in mul operator
    Date: 2013-07-07
"""

from operator import mul
#import cProfile

def get_product(factor1, factor2):
    """ get the product of two factors using for loop """
    factor1 = int(factor1)
    factor2 = int(factor2)
    if factor1 == 0 or factor2 == 0:
        return 0
    if factor1 == 1:
        return factor2
    if factor2 == 1:
        return factor1
    product = 0
    for value in xrange(abs(factor2)):
        product += abs(factor2)
    if factor1 < 0 and factor2 < 0:
        return product
    if factor1 < 0 or factor2 < 0:
        return -product
    return product


def get_product_recursive(factor1, factor2): 
    """ get the product of two factors using recursion """
    factor1 = int(factor1)
    factor2 = int(factor2)
    if factor1 == 1:
        return factor2
    if factor1 == 0:
        return 0
    if factor1 < 0:
        return -get_product_recursive(-factor1, factor2)
    return factor2 + get_product_recursive(factor1 - 1, factor2)


def main():
    """ run the main logic """
    values = ((5, 5), (0, 5), (5, 0), (-5, 0), (-5, 5), (5, -5), (-5, -5))
    for pair in values:
        print get_product(*pair)
        print mul(*pair)
        #print get_product_recursive(*pair)
        
if __name__ == '__main__':
    #cProfile.run('main()')
    main()
