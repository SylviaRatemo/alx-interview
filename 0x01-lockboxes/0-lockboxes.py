#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    #Returns true or false
    """
    opened = set()
    queue = [0]

    while queue:
        current = queue.pop(0)
        opened.add(current)

        unopened_keys = set(boxes[current]) - opened
        valid_keys = [key for key in unopened_keys if key < len(boxes)]
        
        queue.extend(valid_keys)
    
    return len(opened) == len(boxes)
