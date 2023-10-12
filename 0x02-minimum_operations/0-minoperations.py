#!/usr/bin/env python3
'''Minimum Operations
'''


def minOperations(n):
    '''return the least number of operations
    '''
    if n == 1:
        return 0
    op = [float('inf')] * (n+1)
    op[1] = 0

    for i in range(2, n+1):
        for j in range(1, i // 2 + 1):
            if i%j == 0:
                op[i] = min(op[i], op[j] + (i // j))
    return op[n] if op[n] != float('inf') else 0