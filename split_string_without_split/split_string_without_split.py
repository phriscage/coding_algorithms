#!/usr/bin/python2.7
"""
    Name: split_string_without_split.py
    Developer: Chris Page
    Date: 2013-03-03
    Purpose: split a string by a specific string without using the built-in 
    split method
"""


class SplitString(object):
    """ split string will try to use iteration and memory to determine if the
    we can split the string
    """

    def __init__(self, unsplit_string, split_regex):
        """ instantiate the class """
        self.unsplit_string = unsplit_string
        self.split_regex = split_regex

    def _split_string_without_split(self):
        """ split a string without using the built-in split function. Try
        to account for all use cases of empty self.split_regex or 
        self.unsplit_string.
        Args:
            None
        Returns:
            list of strings
        """
        results = []
        possible_string = str()
        split_regex_count = 0
        len_split_regex = len(self.split_regex)
        ## empty split_regex test case
        if len_split_regex == 0:
            return [self.unsplit_string]
        for character in self.unsplit_string:
            if character == self.split_regex[split_regex_count]:
                if (len_split_regex - 1) == split_regex_count:
                    results.append(possible_string)
                    possible_string = str()
                else:
                    split_regex_count += 1
            else:
                possible_string += character
                split_regex_count = 0
            #results.append(character)
        ## catch any trailing possible strings
        if possible_string:
            results.append(possible_string)
        return results


    def run(self, sort=None):
        """ run will try to use the private methods to split a given 
        string 
        """
        return self._split_string_without_split()
        #return self.unsplit_string.split(self.split_regex)


def main():
    """ run the main logic """
    split_string = SplitString('every;thing|;|else|;|in|;|he;re', '|;|')
    print split_string.unsplit_string
    print split_string.run()


if __name__ == '__main__':
    main()
    
