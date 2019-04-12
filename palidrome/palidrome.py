#!/usr/bin/env python
"""
    Developer: Chris Page
    Last Updated Date: 2019-04-12
    Date: 2013-07-11
    Purpose: determine if a given string is a palidrome while ignoring
    non-alphabet characters.
    I.E ("Madam, I'm Adam!!!")
"""

import re
from string import lowercase
import sys

class Palidrome(object):
    """ encapsulate Palidrome functions in a class """

    def __init__(self, unknown):
        """ instatiate the class """
        self.unknown = str(unknown)
        self.lowercase = lowercase


    def validate(self):
        """ validate if class self.unknown is a palidrome and return
        True/False. Check if at least one character matches or if both
        left = right. Only need to go to half the len of the unknown string.
        Runtime O Notation is O(N) since complexity is determined by length
        of unkown string even though we iterate front -> back & back -> front.
        Returns:
            True/False
        """
        if not re.search(r'[%s]' % self.lowercase, self.unknown, re.I):
            return False
        reverse = self.unknown[::-1]
        if self.unknown == reverse:
            return True
        for left_index in xrange(len(self.unknown)/2):
            left = self.unknown[left_index]
            if left.lower() in self.lowercase:
                for right_index, right in enumerate(reverse, 1):
                    if right.lower() in self.lowercase:
                        if left.lower() != right.lower():
                            return False
                        # sliced to start again at a placeholder index
                        reverse = reverse[right_index:]
                        break
                    continue
            continue
        return True


def main(arg):
    """ run the main logic """
    palidrome = Palidrome(arg)
    return palidrome.validate()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "One argument required!"
        sys.exit(1)
    print sys.argv[1], " : ", main(sys.argv[1])
