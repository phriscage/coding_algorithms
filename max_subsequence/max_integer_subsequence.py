#!/usr/bin/python2.7
"""
    Find the maximum sum of a sub-sequence from an positive integer array where 
    any two numbers of sub-sequence are not adjacent to each other in the original 
    sequence. E.g 1 2 3 4 5 6 --> 2 4 6
"""

def maximum_subsequence(seq):
    """ maximum subsequence is an elegant solution from here:
        http://wordaligned.org/articles/the-maximum-subsequence-problem 
    """
    maxsofar, maxendinghere = 0, 0
    for s in seq:
        # invariant: maxendinghere and maxsofar are accurate
        # are accurate up to s
        maxendinghere = max(maxendinghere + s, 0)
        maxsofar = max(maxsofar, maxendinghere)
    return maxsofar

def max_subsequence(sequence):
    """ find the maximum sub-sequence for a given list of numbers

    Args:
        sequence (list): list of numbers
    Returns:
        list of max integers
    """
    include = []
    exclude = []

    for i in sequence:
        # current max excluding i
        if sum(include) > sum(exclude):
            exclude_new = include
        else:
            exclude_new = exclude
        # current max including int(i)
        include = exclude + [int(i)]
        exclude = exclude_new
    
    if sum(include) > sum(exclude):
        return include
    else:
        return exclude

if __name__ == '__main__':
    print max_subsequence(range(10))
    #print maximum_subsequence(range(10))
