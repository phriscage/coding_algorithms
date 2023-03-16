#!/usr/bin/env python3
""" the is the main logic """
import os.path
from collections import defaultdict

class Numeronym(object):
    """ this class captures the numeronym operations """

    def __init__(self):
        """ instantiate the class """
        self.data = dict()


def _create_numeronym(value):
    """ create numeronym from an unknown value string """
    value = str(value)
    if len(value) == 0:
        return ""
    if len(value) == 1:
        return value[0]
    if len(value) == 2:
        return value[-1]
    return value[0] + str(len(value)) + value[-1]

def create_numeronyms_reference(file_name):
    """ let's create the reference of numeronyms from the dictionary file
    Args:
    file_name (string) file name for dictionary
    Returns:
    numeronyms (dict) key -> value of numeronyms
    """
    if not os.path.isfile(file_name):
        raise TypeError("Bad file: %s" % file_name)
    #numeronyms = dict()
    numeronyms = defaultdict(int)
    with open(file_name) as file_buffer:
        for line in file_buffer:
            for word in line.split():
                numeronyms[_create_numeronym(word)] += 1
    return numeronyms

def check_if_numeronym(value, numeronyms):
    """ check if value is a numeronym in the reference' """
    if not _create_numeronym(value):
        return False
    if not numeronyms.get(_create_numeronym(value), None):
        return False
    return True

def main(**args):
    numeronyms = create_numeronyms_reference(args['file_name'])
    print(check_if_numeronym(args['value'], numeronyms))


if __name__ == '__main__':
    import sys
    # import argparse
    main(file_name=sys.argv[1], value=sys.argv[2])
