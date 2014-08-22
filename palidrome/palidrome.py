#!/usr/bin/env python
"""
    Developer: Chris Page
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
        left = right. Only need to go to half the len of the unknown string
        Returns:
            True/False
        """
        if not re.search(r'[%s]' % self.lowercase, self.unknown, re.I):
            return False
        reverse = self.unknown[::-1]
        if self.unknown == reverse:
            return True
        #for left in self.unknown:
        for left_index in xrange(len(self.unknown)/2):
            left = self.unknown[left_index]
            if left.lower() in self.lowercase:
                for right_index, right in enumerate(reverse, 1):
                    reverse = reverse[right_index:]
                    if right.lower() in self.lowercase:
                        if left.lower() != right.lower():
                            return False
                        #print "match: %s = %s" % (left, right)
                    break
        return True


def main(arg):
    """ run the main logic """
    palidrome = Palidrome(arg)
    print palidrome.validate()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "One argument required!"
        sys.exit(1)
    main(sys.argv[1])
