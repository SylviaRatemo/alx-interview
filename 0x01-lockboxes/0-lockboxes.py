#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, else returns False.
    """
    opened = set()
    queue = [0]

    while queue:
        current = queue.pop(0)
        opened.add(current)

        unseen_boxes = set(boxes[current]) - opened
        valid_keys = [key for key in unseen_boxes if 0 <= key < len(boxes)]

        queue.extend(valid_keys)

    return len(opened) == len(boxes)
