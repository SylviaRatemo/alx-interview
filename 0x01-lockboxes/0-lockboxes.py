#!/usr/bin/python3
"""
Lockboxes
"""
from collections import deque


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, else returns False.
    """
    n = len(boxes)
    opened = set()
    queue = deque([0])

    while queue:
        current = queue.popleft()
        opened.add(current)

        unseen_boxes = set(boxes[current]) - opened
        valid_keys = [key for key in unseen_boxes if 0 <= key < n]

        queue.extend(valid_keys)

        # Check if all boxes are opened inside the loop
        if len(opened) == n:
            return True

    return False
