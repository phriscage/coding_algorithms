#!/usr/bin/env python3
## use the OS level python3 interpreter if file is chmod executable
""" the main comments explaining what the logic/class does """

from collections import defaultdict
import os.path

def parse_file(file_name):
    """ parse a file and return the data structure """
    if not os.path.isfile(file_name):
        raise TypeError("Bad file: '%s'" % file_name)
    dependencies = defaultdict(list)
    with open(file_name) as file_buffer:
        for line in file_buffer:
            values = line.split()
            dependencies[values[0].strip(':')] = values[1:]
    print(dependencies)
    return dependencies

#build_order = list()

def get_build_order(value, dependencies, build_order=None):
    """ get the dependencies """
    if not build_order:
        build_order = list()
    if dependencies.get(value, None):
        for dep in dependencies.get(value):
            build_order = get_build_order(dep, dependencies, build_order)
    if dependencies.get(value, None) != None and value not in build_order:
        build_order.append(value)
    return build_order

def main(**args):
    """ main logic """
    dependencies = parse_file(args['file_name'])
    build_order = get_build_order(args['target'], dependencies)
    print(build_order)

if __name__ == '__main__':
    import sys
    main(file_name=sys.argv[1], target=sys.argv[2])
