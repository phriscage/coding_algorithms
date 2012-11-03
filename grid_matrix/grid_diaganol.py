#!/usr/bin/python2.7
"""
    search through a (row x column) two digit grid and find the 
    maximum product for any tuple length within the grid.
"""
import sys
import operator


def get_tuples(length, grid):
    """ return the left, right, up, down and diaganol tuples 
        len(row) - len(max_tuple) = 16
        Args:
            grid (list): list of lists
    """
    four = range(int(length))
    for i in xrange(16):
        for j in xrange(16):
            yield(grid[i][j+k] for k in four)
            yield(grid[i+k][j] for k in four)
            yield(grid[i+k][j+k] for k in four)
            yield(grid[i+3-k][j+k] for k in four)
    

def main(grid):
    """ find the maximum product of each l,r,u,d tuples """
    length = 4
    numbers_grid = [[int(cell) for cell in row.split()] for row in grid if row]
    return max(reduce(operator.mul, t) for t in get_tuples(length, numbers_grid))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Argument required."
        sys.exit(1)
    grid = open(sys.argv[1])
    print main(grid)

