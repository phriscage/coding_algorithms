#!/usr/bin/python2.7
""" 
    this can be easily accomplished by list.index(?) but included a 
    straight-forward example as well.
"""

def binary_search(values, target):
    """ binary search is recursive while loop to locate the target in 
        the list 
    Args:
        values (list): list of integers
        target (int): target within values
    Returns:
        middle (int)
    """
    low = 0
    if type(values) is not list:
        return False
    high = len(values)
    while low <= high:
        middle = low + (high-low) / 2
        if values[middle] == int(target):
            return middle            
        elif values[middle] <= int(target): 
            low = middle + 1
        else:
            high = middle - 1


def main():
    """ run the main logic """
    values = [1,2,4,7,9,11,1,23,34,55,66]
    print binary_search(values, 23)
    print values.index(23)
    print binary_search(values, 1)
    print values.index(1)


if __name__ == '__main__':
    main()
