"""
    Developer: Chris Page
    Date: 2019-04-12
    Purpose: Test the palidrome
"""
import unittest
from palidrome import main


class TestPalidromeValidate(unittest.TestCase):
    """ test some use cases """

    ## Successful tests
    def test_one_char(self):
        """ test one character """
        value = 'a'
        self.assertEqual(main(value), True)

    def test_two_chars(self):
        """ test two characters """
        value = 'aa'
        self.assertEqual(main(value), True)

    def test_three_chars(self):
        """ test three chars """
        value = 'aba'
        self.assertEqual(main(value), True)

    def test_three_chars_with_special(self):
        """ test three chars with special """
        value = '*a#b$&a^'
        self.assertEqual(main(value), True)

    def test_many_chars_with_special(self):
        """ test many chars with special """
        value = 'Madam, I\'m Adam!!!'
        self.assertEqual(main(value), True)

    ## Failure tests
    def test_two_chars_false(self):
        """ test two character false """
        value = 'ab'
        self.assertEqual(main(value), False)

    def test_three_chars_false(self):
        """ test three chars false """
        value = 'abc'
        self.assertEqual(main(value), False)

    def test_three_chars_with_special_false(self):
        """ test three chars false """
        value = '*a#b$&c^'
        self.assertEqual(main(value), False)

if __name__ == '__main__':
    unittest.main()
