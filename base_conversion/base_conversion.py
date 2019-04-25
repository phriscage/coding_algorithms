#!/usr/bin/env python
"""
    Name: base_conversion.py
    Developer: Chris Page
    Last Updated Date: 2019-04-12
    Date: 2015-04-01
    Purpose: convert a base 10 <-> base 2 vs versa
"""
import sys

def get_binary(number):
    """ convert an integer to binary string """
    number = int(number)
    binary_keys = {idx:val for idx, val in enumerate("01")}
    if number == 0:
        return binary_keys[number]
    binary = str()
    while number > 0:
        binary += binary_keys[number % len(binary_keys)]
        number /= len(binary_keys))
    return binary[::-1]

def get_decimal(binary):
    """ convert a binary string to a decimal number """
    binary = str(binary)
    number_keys = {val:idx for idx, val in enumerate("01")}
    number = 0
    for val in binary:
        if not number_keys.get(val, None) and number_keys.get(val, None) != 0:
            raise ValueError("Incorrect binary string")
        number = number * len(number_keys) + number_keys[val]
    return number
