#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Returns true or false
    """
    opened = set()
    queue = [0]

    while queue:
        current = queue.pop(0)
        #print(current)
        opened.add(current)

        queue.extend(key for key in boxes[current] if key not in opened and key < len(boxes))
    
    return len(opened) == len(boxes)
