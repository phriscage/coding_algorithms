#!/usr/bin/python2.7
""" return a factorial from a given number """
import sys
import math


def get_factorial(number):
    """ iterate over a given number and return the factorial 
    Args:
        number (int): number integer
    Returns:
        factorial (int)
    """
    factorial = 1
    for n in range(int(number), 1, -1):
        factorial *= n
    return factorial


def math_factorial(number):
    """ user the built-in math.factorial to return factorial 
    Args:
        number (int): number integer
    Returns:
        factorial (int)
    """
    return math.factorial(int(number))

    
def main():
    """ run the main logic """
    #number = raw_input()
    if len(sys.argv) < 2:
        print "Argument required."
        sys.exit(1)
    number = sys.argv[1]
    print get_factorial(number)
    print math_factorial(number)
    
if __name__ == '__main__':
    main()

