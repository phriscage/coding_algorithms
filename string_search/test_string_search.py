"""
    Developer: Chris Page
    Date: 2014-08-19
    Purpose: Test the string_search
"""
import unittest
from string_search import get_match_with_iteration, get_match_with_re, \
    get_match_with_string


class TestStringSearch(unittest.TestCase):
    """ test some use cases """
    
    def test_one_char_first_position(self):
        """ test one character in the first position of string """
        values = ('a', 'abc')
        self.assertEqual(get_match_with_iteration(*values), True)
        self.assertEqual(get_match_with_re(*values), True)
        self.assertEqual(get_match_with_string(*values), True)

    def test_one_char_first_and_last_position(self):
        """ test one character in the first and last position of string """
        values = ('a', 'abca')
        self.assertEqual(get_match_with_iteration(*values), True)
        self.assertEqual(get_match_with_re(*values), True)
        self.assertEqual(get_match_with_string(*values), True)

    def test_one_char_middle_position(self):
        """ test one character in the middle position of string """
        values = ('b', 'abc')
        self.assertEqual(get_match_with_iteration(*values), True)
        self.assertEqual(get_match_with_re(*values), True)
        self.assertEqual(get_match_with_string(*values), True)
        
    def test_one_char_last_position(self):
        """ test one character in the last position of string """
        values = ('c', 'abc')
        self.assertEqual(get_match_with_iteration(*values), True)
        self.assertEqual(get_match_with_re(*values), True)
        self.assertEqual(get_match_with_string(*values), True)
        
    def test_one_char_not_in(self):
        """ test one character not in string """
        values = ('d', 'abc')
        self.assertEqual(get_match_with_iteration(*values), False)
        self.assertEqual(get_match_with_re(*values), False)
        self.assertEqual(get_match_with_string(*values), False)
        
    def test_two_char_first_position(self):
        """ test two character in the first position of string """
        values = ('ab', 'abc')
        self.assertEqual(get_match_with_iteration(*values), True)
        self.assertEqual(get_match_with_re(*values), True)
        self.assertEqual(get_match_with_string(*values), True)

    def test_two_char_middle_position(self):
        """ test two character in the middle position of string """
        values = ('bb', 'abbc')
        self.assertEqual(get_match_with_iteration(*values), True)
        self.assertEqual(get_match_with_re(*values), True)
        self.assertEqual(get_match_with_string(*values), True)
        
    def test_two_char_last_position(self):
        """ test one character in the last position of string """
        values = ('bc', 'abbc')
        self.assertEqual(get_match_with_iteration(*values), True)
        self.assertEqual(get_match_with_re(*values), True)
        self.assertEqual(get_match_with_string(*values), True)
        
    def test_two_char_not_in(self):
        """ test two character not in string """
        values = ('aa', 'abc')
        self.assertEqual(get_match_with_iteration(*values), False)
        self.assertEqual(get_match_with_re(*values), False)
        self.assertEqual(get_match_with_string(*values), False)
            

if __name__ == '__main__':
    unittest.main()
