#!/usr/bin/python2.7
""" 
    create a graph from a matrix with incrementing values 
"""


def create_graph(rows, columns):
    """ create a rows by columns matrix with sequencial values and 
        then dict graph. 
    Args:
        rows (int): number of rows
        columns (int): number of columns
    Returns:
        graph (dict): row x column dict
     """
    matrix = [[columns*row + column for column in xrange(int(columns))] 
        for row in xrange(int(rows))]
    graph = {}
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if str(cell) not in graph:
                graph[str(cell)] = []
            if j < len(row) - 1:
                graph[str(cell)] += [str(matrix[i][j+1])]
            if i < len(matrix) - 1:
                graph[str(cell)] += [str(matrix[i+1][j])]
    return graph


def create_matrix(rows, columns):
    """ create a rows x columns matrix with incrementing integers 
    Args:
        rows (int): number of rows
        columns (int): number of columns
    Returns:
        row x column list of lists
    """
    return [[0 for column in xrange(int(columns))] 
        for row in xrange(int(rows))]


if __name__ == '__main__':
    print create_graph(2, 2)
    print create_matrix(2, 2)

