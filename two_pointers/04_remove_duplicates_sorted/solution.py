"""Remove Duplicates from Sorted Array - write your solution here.

Read README.md for the question, then run:  python test.py
"""
from typing import List


def remove_duplicates(nums: List[int]):
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1, nums


# while j < len(nums):
#     if nums[j] <= nums[i]:
#         j += 1
#     else:
#         k += 1
#         nums[i+1], nums[j] = nums[j], nums[i+1]
#         i += 1


print(remove_duplicates([-3, -3, -1, 0, 0, 2, 2, 5]))
print(remove_duplicates([1, 1, 1, 2, 3]))
