"""Move Zeroes - write your solution here.

Read README.md for the question, then run:  python test.py
"""
from typing import List


def move_zeroes(nums: List[int]) -> None:
    i, j = 0, 1

    while j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
        elif nums[i] != 0:
            i += 1

        j += 1


nums = [4, 0, 5, 0, 0, 6]
move_zeroes(nums)
print(nums)
