#!/usr/bin/python2.7
"""
    a fibonacci number can be easily calculated recursively, but this is not 
    efficient so we'll use memory instead.
    1, 1, 3, 5 
"""

_fibs = {0:0, 1:1}

def fib_optimized(number):
    """ calculate the fibonacci number utilizing memory 
    Args:
        number (int): number
    Returns:
        _fib[number] (int): fibonacci number
    """
    number = int(number)
    if not number in _fibs:
        _fibs[number] = fib_optimized(number-1) + fib_optimized(number-2)
    return _fibs[number]


def fib_slow(number):
    """ calculate the fibonacci number recursively 
    Args:
        number (int): number
    Returns:
        fib (int): fibonacci number
    """
    number = int(number)
    if number in [0, 1]:
        return number
    else:
        return fib_slow(number-1) + fib_slow(number-2)


def main():
    """ run the main logic """
    print [fib_slow(i) for i in xrange(30)]
    print [fib_optimized(i) for i in xrange(30)]

if __name__ == '__main__':
    main()

