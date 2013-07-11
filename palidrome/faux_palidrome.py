#!/usr/bin/python2.7
"""
Problem Statement
        A word is a palindrome if it can be read the same forwards and backwards. For example, the strings "ANA", "AAXAA", "Z" and "XYYYYYX" are palindromes (quotes for clarity).

A word is a faux palindrome if, after replacing every group of consecutive equal letters with a single instance of the letter, the resulting word is a palindrome. For example, the string "AAAAANNAA" is a faux palindrome. A detailed explanation why this is a faux palindrome is given below in Example 1. Other examples of faux palindromes are the strings "AAAAAAAAAAAAAAAXA and "XYX". Note that every palindrome is also a faux palindrome.

Examples
0)  
        
"ANA"
Returns: "PALINDROME"
"ANA" reads the same from left to right and right to left.
1)  
        
"AAAAANNAA"
Returns: "FAUX"
This is obviously not a palindrome. Now suppose that we replace each group of consecutive equal letters by a single copy of that letter. That is, we change "AAAAA" to "A", "NN" to "N", and "AA" to "A". In this way we will obtain the new string "ANA", which is a palindrome. Hence the original string is a faux palindrome.
2)  

    Purpose: return 'PALINDROME', 'FAUX', or 'NOT EVEN FAUX' based off 
        string input
"""

class FauxPalindrome(object):
    """ A word is a palindrome if it can be read the same forwards and 
    backwards. For example, the strings "ANA", "AAXAA", "Z" and "XYYYYYX" 
    are palindromes (quotes for clarity).
    """

    def __init__(self):
        """ instantiate the class """
        self.poss_palin = None
        self.poss_faux = None
    
    def _is_palindrome(self, string):
        """ check if string is a possible palindrome 
        Args:
            string (str): possible palindrome
        Returns:
            True/False
        """
        return str(string) == str(string)[::-1]

    def _create_faux(self, string):
        """ strip the string of duplicate characters 
        Args:
            string (str): possible palindrome
        Returns:
            True/False
        """
        new = str()
        for character in string:
            if not new:
                new = character
            if character != new[-1]:
                new += character
        return new
            

    def check_string(self, string):
        """ check if string is possible faux palindrome
        Args:
            string (str): possible faux palindrome
        Returns:
            'PALINDROME', 'FAUX', or 'NOT EVEN FAUX'
        """
        if self._is_palindrome(string):
            return 'PALINDROME'
        else:
            poss_faux = self._create_faux(string)
            if self._is_palindrome(poss_faux):
                return 'FAUX'
            else:
                return 'NOT EVEN FAUX'


def main(string):
    """ run the main logic """
    faux_palindrome = FauxPalindrome()
    return faux_palindrome.check_string(string)


if __name__ == '__main__':
    for test in ['ANA', 'AAAAANNAA', 'LEGENDARY', 'XXXYTYYTTYX', 'TOPCOODEREDOOCPOT', 
        'TOPCODEREDOOCPOT', 'XXXXYYYYYZZXXYYY']:
        print test,": ", main(test)

