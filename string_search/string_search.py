"""
    Developer: Chris Page
    Date: 2014-04-28
    Purpose: Given a pattern and a string, find all occurances of that pattern
        in the string.
"""

import re

def _check_params(pattern, unknown):
    """ check the parameters are valid """
    try:
        pattern = str(pattern)
        unknown = str(unknown)
    except ValueError as error:
        print "Do something with error: %s" % error
        raise
    return pattern, unknown
    

def get_match_with_re(pattern, unknown):
    """ return all matches of the pattern in the unknown string
    Args:
        pattern (str): pattern string
        unknown (str): full unknown string
    Returns:
        True/False
    """
    pattern, unknown = _check_params(pattern, unknown)
    regex = re.compile(pattern)
    if not regex.search(unknown):
        return False
    return True


def get_match_with_string(pattern, unknown):
    """ return match index of the pattern in the unknown string
    Args:
        pattern (str): pattern string
        unknown (str): full unknown string
    Returns:
        True/False
    """
    pattern, unknown = _check_params(pattern, unknown)
    if pattern not in unknown:
        return False
    return True


def get_match_with_iteration(pattern, unknown):
    """ return first match of the pattern in the unknown string
    Args:
        pattern (str): pattern string
        unknown (str): full unknown string
        all_flag (bol): find more than one if True
    Returns:
        True/False
    """
    pattern, unknown = _check_params(pattern, unknown)
    if len(pattern) == 0 or len(pattern) > len(unknown):
        return False
    if pattern == unknown:
        return True
    matches = 0
    for val in xrange(len(unknown) + 1 - len(pattern)):
        if unknown[val:val+len(pattern)] == pattern:
            matches += 1
            return True
    return False
