"""
    Name: permutations.py
    Developer: Chris Page
    Date: 2013-03-04
    Purpose: transpose a specific string based off a given offset value
"""
import sys
import string
import re

class TransposeString(object):
    """ TransposeString will rty to return a transposed string based off a
    given offset value
    """

    def __init__(self):
        """ instatiate the class """
        self.original_string = None
        self.offset = 3

    def _transpose_string(self):
        """ transpose string creates a transposed alphabet based
        self.offset and then returns a new string using the index of the 
        transposed alphabet.
        Args:
            None
        Returns:
            transposed string
        """
        transposed_alphabet = string.lowercase[self.offset:] + \
            string.lowercase[:self.offset]
        new_string = str()
        for character in self.original_string:
            if character in string.lowercase:
                new_string += transposed_alphabet[string.lowercase.index(character)]
            else:
                new_string += character
                #raise ValueError, "%s is not in %s" % (character, string.lowercase)
        return new_string
            
    def run(self, string):
        """ run the logic of the class 
        Args:
            string (str): unformatted string
        Returns:
            True/False
        """
        self.original_string = string
        return self._transpose_string()


def main(string):
    """ run the main logic """
    transpose_string = TransposeString()
    print transpose_string.run(string)


if __name__ == '__main__':
    main("hello")
    main("hello!, I hope you know what this means!")

