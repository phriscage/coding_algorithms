"""
    Developer: Chris Page
    Date: 2014-08-19
    Purpose: Test the string_replace
"""
import unittest
from string_replace import parse_string


class TestStringParse(unittest.TestCase):
    """ test some use cases """
    
    def test_filename_length_zero(self):
        """ test_filename_length_zero """
        values = ('', 'a')
        self.assertEqual(parse_string(*values), False)

    def test_filename_length_less_than_pattern(self):
        """ test_filename_length_less_than_pattern """
        values = ('a', 'ab')
        self.assertEqual(parse_string(*values), False)

    def test_filename_and_pattern_length_zero(self):
        """ test_filename_and_pattern_length_zero """
        values = ('', '')
        self.assertEqual(parse_string(*values), True)

    def test_filename_and_pattern_none(self):
        """ test_filename_and_pattern_none """
        values = (None, None)
        self.assertEqual(parse_string(*values), True)

    def test_valid_filename_first_character(self):
        """ test_valid_filename_first_character """
        values = ('abc', 'a')
        self.assertEqual(parse_string(*values), True)

    def test_valid_filename_middle_character(self):
        """ test_valid_filename_middle_character """
        values = ('abc', 'b')
        self.assertEqual(parse_string(*values), True)

    def test_valid_filename_last_character(self):
        """ test_valid_filename_last_character """
        values = ('abc', 'c')
        self.assertEqual(parse_string(*values), True)

    def test_invalid_filename(self):
        """ test_valid_filename """
        values = ('abc', 'd')
        self.assertEqual(parse_string(*values), False)

if __name__ == '__main__':
    unittest.main()
