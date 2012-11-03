#!/usr/bin/python2.7
""" print permutations of the alphabet """
import itertools
import string

def alpha_perms():
    a = itertools.permutations(string.ascii_lowercase[:3])
    while True:
        try:
            print a.next()
        except StopIteration, e:
            return True

if __name__ == '__main__':
    alpha_perms()

