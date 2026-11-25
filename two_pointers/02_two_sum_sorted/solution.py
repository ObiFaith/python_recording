"""Two Sum (Sorted Array) - write your solution here.

Read README.md for the question, then run:  python test.py
"""
from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    if not numbers:
        return numbers

    i, j = 0, len(numbers) - 1

    while i < j:
        if numbers[i] + numbers[j] < target:
            i += 1
        elif numbers[i] + numbers[j] > target:
            j -= 1
        else:
            break

    return [i+1, j+1]
