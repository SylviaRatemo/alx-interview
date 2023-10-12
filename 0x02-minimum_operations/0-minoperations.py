#!/usr/bin/python3
'''Minimum Operations
'''


def minOperations(n):
    '''return the least number of operations
    '''
    if not isinstance(n, int) or n <= 0:
        return 0

    ops = 0
    clipboard = 1
    done = 1

    while done < n:
        if n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops += 2
        else:
            done += clipboard
            ops += 1

    return ops
