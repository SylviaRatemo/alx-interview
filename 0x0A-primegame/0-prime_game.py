#!/usr/bin/python3
"""
isWinner function
    : Ben or Maria
    : Prime Game
"""


def isWinner(x, nums):
    """Prime Game
    """
    # Check for invalid inputs
    if not nums or x < 1:
        return None

    # Find the maximum number in the input list
    n = max(nums)

    # Initialize a filter list for prime numbers
    fltr = [True for _ in range(max(n + 1, 2))]

    # Use the Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not fltr[i]:
            continue
        for j in range(i * i, n + 1, i):
            fltr[j] = False

    # Mark 0 and 1 as non-prime
    fltr[0] = fltr[1] = False

    # Modify the filter list to store cumulative count of primes
    c = 0
    for i in range(len(fltr)):
        if fltr[i]:
            c += 1
        fltr[i] = c

    # Count
    plyr1 = 0
    for n in nums:
        plyr1 += fltr[n] % 2 == 1

    # Determine the winner based on the conditions
    if plyr1 * 2 == len(nums):
        return None
    if plyr1 * 2 > len(nums):
        return "Maria"
    return "Ben"
