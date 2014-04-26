"""
    Developer: Chris Page
    Date: 2013-07-10
    Purpose: Given a filename and a pattern, see if the entire pattern can be
        duplicated by the filename by only removing characters from the filename
"""

import logging

def parse_string(filename, pattern):
    """ parsing a filename and returning true/false if the pattern can be 
    duplicated by the filename
    Args:
        filename (str): filename
        pattern (str): pattern
    Returns:
        True/False
    """
    try:
        filename = str(filename)
        pattern = str(pattern)
    except ValueError, error:
        logging.exception("%s: %s" % (error, error))
        return False
    if len(filename) == 0 or len(filename) < len(pattern):
        return False
    if filename == pattern:
        return True
    new_filename = str()
    tmp_filename = filename
    for pattern_char in pattern:
        test_string = tmp_filename
        for i, test_char in enumerate(test_string, 1):
            tmp_filename = test_string[i:]
            if pattern_char == test_char:
                new_filename += test_char
                break
    if new_filename != pattern:
        return False
    else:
        return True

if __name__ == '__main__':
    print parse_string('string_expression_patterner.cc', 'stxpm.c') # False
    print parse_string('string_expressiom_patterner.cc', 'stxpm.c') # True
    print parse_string('strcc', 'stxpm.c') # False
    print parse_string('mpxtng_expression.cc', 'stxpm.c') # False
    print parse_string('stxpm.c', 'stxpm.c') # True
    print parse_string('', '') # False
