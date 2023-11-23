#!/usr/bin/python3
"""ALX Interviews
Making Changes
"""


def makeChange(coins, total):
    """
    Find the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for a total of 0
    dp[0] = 0

    # Update the dp array for each total from 1 to the target total
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
