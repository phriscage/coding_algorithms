#!/usr/bin/python2.7
""" 
    this can be easily accomplished by list.index(?) but included a 
    straight-forward example as well. lower-bound left to right and
    right to left need to be taken into account.
"""

def binary_search(values, target):
    """ binary search is recursive while loop to locate the target in 
        the list and we need to search both directions.
    Args:
        values (list): list of integers
        target (int): target within values
    Returns:
        middle (int)
    """
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = low + (high-low) / 2
        if values[middle] == int(target):
            return middle            
        elif values[middle] <= int(target): 
            low = middle + 1
        else:
            high = middle - 1
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = low + (high-low) / 2
        if values[middle] == int(target):
            return middle
        elif values[middle] >= int(target):
            low = middle + 1
        else:
            high = middle - 1
    raise ValueError, "%i is not in list" % target


def main():
    """ run the main logic """
    values = [1,2,4,7,9,11,1,23,34,55,66]
    print binary_search(values, 23)
    print values.index(23)
    values = sorted(range(10), reverse=True)
    for i in range(10):
        if not binary_search(values, i) == values.index(i):
            print i, False
    for i in sorted(range(10), reverse=True):
        if not binary_search(values, i) == values.index(i):
            print i, False 
    print True


if __name__ == '__main__':
    main()
