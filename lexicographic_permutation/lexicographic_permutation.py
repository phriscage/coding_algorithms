#!/usr/bin/python2.7
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 
5, 6, 7, 8 and 9?
"""
import itertools

def get_permutations(number, max_number=None):
    """ return either the last possible combination for a given number 
        or return the max_number using itertools.

    Args:
        number (str): number string
        max_number (int): max_number for itertools
    Returns:
        value (tup): tuple itertools permutation
    """
    number = str(number)
    permutations = itertools.permutations(number)
    try:
        if max_number:
            for i in range(int(max_number)):
                value = permutations.next()
        else:
            for i in permutations:
                value = i
    except StopIteration, e:
        return value
    return value

if __name__ == '__main__':
    number = ''.join([str(i) for i in range(10)])
    print ''.join(get_permutations(number))
        
