"""Container With Most Water - write your solution here.

Read README.md for the question, then run:  python test.py
"""
from typing import List


def max_area(height: List[int]) -> int:
    area = 0
    if not height:
        return area

    i, j = 0, len(height) - 1

    while i < j:
        h = min(height[i], height[j])
        area = max((j-i) * h, area)

        if height[i] > height[j]:
            j -= 1
        else:
            i += 1

    return area

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
