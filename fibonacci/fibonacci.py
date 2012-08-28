#!/usr/bin/python2.7
"""
    a fibonacci number can be easily calculated recursively, but this is not 
    efficient so we'll use memory instead.
"""

memo = {0:0, 1:1}

def fib_mem(n):
    if not n in memo:
        memo[n] = fib_mem(n-1) + fib_mem(n-2)
    return memo[n]

if __name__ == '__main__':
    print [fib_mem(i) for i in range(100)]
