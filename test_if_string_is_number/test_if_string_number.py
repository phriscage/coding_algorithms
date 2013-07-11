#!usr/bin/python2.7
""" 
    Developer:  Chris Page
    Date:       2013-03-03
    Purpose:    create a method to determine if a string is a number
"""
import sys
import re

class NumberTest(object):
    """ the NumberTest class will verify if a string is an integer or float.
    The public method 'test_string' will try to validate the possible_integer
    variable that was instantiated.
    """
    
    def __init__(self, possible_number):
        """ instantiate the class 
        Args:
            possible_number (str): possible string number
        """
        self.possible_number = possible_number

    def _check_string_with_object_type(self):
        """ test string will verify if the string is an integer
        using the built-in data object type.
        Returns:
            True/False
        Raises:
            TypeError
        """
        try:
            int(self.possible_number)
            float(self.possible_number)
        except ValueError, error:
            raise error
        return True

    def _check_string_with_regex(self):
        """ test string will verify if the string is an integer or float 
        using the regex.
        Returns:
            True/False
        Raises:
            TypeError
        """
        #if not re.match(r'^-?[0-9]+\.?[0-9]+$', self.possible_number):
        if not re.match(r'^-?\d+\.?\d+$', self.possible_number):
            return False
        else:
            return True
        

    def test_string(self):
        """ test string will verify if the string is an number """
        #return self._check_string_with_object_type()
        return self._check_string_with_regex()


def main(possible_number):
    """ run the main logic """
    number_test = NumberTest(possible_number)
    print number_test.test_string()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "an argument is required!"
    else:
        main(sys.argv[1])
