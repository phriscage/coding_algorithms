"""
    Name: max_string_subsequence.py
    Developer: Chris Page
    Date: 2013-03-16
    Purpose:    Create a function that takes an unordered string and returns the
    character that corresponds to the longest consecutvice subsequence
    I.E. ('aabaccccdaa') => ('c')
"""
#import cProfile

def get_max_subsequence_not_optimal(unorderd_string):
    """ *** this logic is not optimized and uses too much memory ***
    iterate over string to determine max subsequence of character
    and store in current_sequence, max_sequence
    Args:
        unorderd_string (str): letters
    Returns:
        character (str)
    """
    max_sequence = str()
    current_sequence = str()
    for character in unorderd_string:
        if len(current_sequence) >0 and \
            character == current_sequence[-1]:
            current_sequence += character
        else:
            current_sequence = character
        if len(current_sequence) > len(max_sequence):
            max_sequence = current_sequence
    return max_sequence[0]


def get_max_subsequence(unorderd_string):
    """ iterate over string to determine max subsequence of character
    and store (char, max).
    Args:
        unorderd_string (str): unorderd_string
    Returns:
        character (str)
    """
    max_value, cur_value = [str(), 0], [str(), 0]
    for character in unorderd_string:
        if character != cur_value[0]:
            cur_value[0] = character
        else:
            cur_value[1] += 1
        if cur_value[1] > max_value[1]:
            max_value = cur_value
            cur_value = [str(), 0]
    return max_value[0]


def main():
    """ run the main logic """
    print get_max_subsequence_not_optimal("aabaccccdaa" * 100000)
    print get_max_subsequence("aabaccccdaa" * 100000)


if __name__ == '__main__':
    main()

