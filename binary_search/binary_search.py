#!/usr/bin/python2.7
""" 
    this can be easily accomplished by list.index(?) but included a 
    straight-forward example as well.
"""

def binary_search(values, target):
    """ binary search is recursive while loop to locate the target in the list """
    lo = 1
    hi = len(values)
    while lo <= hi:
        mid = lo + (hi-lo)/2
        if values[mid] == target:
            return mid            
        elif values[mid] < target: 
            lo = mid+1
        else:
            hi = mid-1


if __name__ == '__main__':
    values = [1,2,4,7,9,11,23,34,55,66]
    print binary_search(values, 23)
    print values.index(23)

