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
    except ValueError as error:
        logging.exception(error)
        return False
    if filename == pattern:
        return True
    if len(filename) == 0 or len(filename) < len(pattern):
        return False
    new_filename = str()
    tmp_filename = filename
    count = 0
    for pattern_char in pattern:
        for test_char in tmp_filename:
            count += 1
            tmp_filename = filename[count:]
            if pattern_char == test_char:
                new_filename += test_char
                break
    if new_filename != pattern:
        return False
    else:
        return True
