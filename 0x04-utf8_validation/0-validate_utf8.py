#!/usr/bin/python3
""" UTF-8 Validation
"""

# Constants for binary literals
TWO_BYTE_MASK = 0b110
THREE_BYTE_MASK = 0b1110
FOUR_BYTE_MASK = 0b11110
CONTINUATION_MASK = 0b10
HIGH_BIT_MASK = 0b10000000


def validUTF8(data):
    """Check if the given list of integers represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing UTF-8 encoded characters.

    Returns:
        bool: True if valid UTF-8 encoding, False otherwise.
    """
    count = 0
    for x in data:
        if count == 0:
            if (x >> 5) == TWO_BYTE_MASK:
                count = 1
            elif (x >> 4) == THREE_BYTE_MASK:
                count = 2
            elif (x >> 3) == FOUR_BYTE_MASK:
                count = 3
            elif (x >> 7) != 0:
                return False
        else:
            if (x >> 6) != CONTINUATION_MASK:
                return False
            count -= 1
    return count == 0
