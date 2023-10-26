#!/usr/bin/python3
""" UTF-8 Validation
"""


def validUTF8(data):
    masks = [128, 64, 32, 16, 8]

    def getType(num):
        for i in range(5):
            if (masks[i] & num) == 0:
                return i
        return -1

    length = len(data)

    i = 0
    while i < length:
        curr = data[i]
        type = getType(curr)

        if type == 0:
            i += 1
        elif type > 1 and i + type <= length:
            i += 1
            while type > 1:
                if getType(data[i]) != 1:
                    return False
                i += 1
                type -= 1
        else:
            return False

    return True
