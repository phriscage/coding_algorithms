#!/usr/bin/python2.7
""" 
    create a dictionary of a graph with each connecting key as a list
    of string values. 
"""

def recursive(graph, start, path=[]):
    """ recursive depth first search from start 
    Args:
        graph (dict): graph dict
        start (str): starting value str
        path (list): list of values in path
    Returns:
        path (list): list of values in path
    """
    path = path + [start]
    for node in graph[start]:
        if not node in path:
            path=recursive(graph, node, path)
    return path


def find_all_paths(graph, start, end, path=[]):
    """ locate each path in dict of lists 
    Args:
        graph (dict): graph dict
        start (str): starting value str
        end (str): end value str
        path (list): list of values in path
    Returns:
        paths (list): list of list of values in path
    """
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


if __name__ == '__main__':
    """ there are redundant paths from UR1, UR2 to ER1 and ER2:

        AR-->SUR->UR3
             /    | 
          UR1   UR2
          |  \ /  |
          ER1   ER2-->CR
            
    """
    graph = {'AR': ['SUR'], 'SUR': ['UR1', 'UR3'], 'UR1': ['ER1', 'ER2'], 'UR2': ['ER1', 'ER2'], 'UR3': ['UR2'], 'ER1': [], 'ER2': ['CR'], 'CR': []}
    print "recursive: ", recursive(graph, 'AR')
    print "find_all_paths: ", find_all_paths(graph, 'AR', 'CR')
    print "find_all_paths (min): ", min(find_all_paths(graph, 'AR', 'CR'), key=len)
    
