"""
    Name: transpose.py
    Developer: Chris Page
    Date: 2013-03-04
    Purpose: transpose a specific string based off a given offset value
"""
from string import lowercase
import re

class TransposeString(object):
    """ TransposeString will rty to return a transposed string based off a
    given offset value
    """

    def __init__(self):
        """ instatiate the class """
        self.original = None
        self.offset = 3

    def _transpose_string(self):
        """ transpose string creates a transposed alphabet based
        self.offset and then returns a new string using the index of the 
        transposed alphabet. use regex to identify uppercase letters
        Args:
            None
        Returns:
            transposed string
        """
        transposed_alphabet = lowercase[self.offset:] + lowercase[:self.offset]
        new_string = str()
        for character in self.original:
            if re.search(character, lowercase):
                new_string += transposed_alphabet[lowercase.index(character)]
            elif re.search(character, lowercase, re.I):
                new_string += transposed_alphabet[lowercase.index(
                    character.lower())].upper()
            else:
                new_string += character
                #raise ValueError, "%s is not in %s" % (character, lowercase)
        return new_string
            
    def run(self, original):
        """ run the logic of the class 
        Args:
            original (str): original string
        Returns:
            True/False
        """
        self.original = original
        return self._transpose_string()


def main(original):
    """ run the main logic """
    transpose_string = TransposeString()
    print transpose_string.run(original)


if __name__ == '__main__':
    main("hello")
    main("hello!, I hope you know what this means, Adam!")

