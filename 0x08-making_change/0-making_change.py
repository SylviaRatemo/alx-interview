#!/usr/bin/python3
"""ALX Interviews
Making Changes
"""


def makeChange(coins, total):
    if total <= 0:
        return o
    # Initialize an array to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for a total of 0
    dp[0] = 0

    # Update the dp array for each total from 1 to the target total
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, the total cannot be met by any combination of coins
    if dp[total] == float('inf'):
        return -1

    return dp[total]