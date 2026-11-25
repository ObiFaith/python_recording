"""Remove Element - write your solution here.

Read README.md for the question, then run:  python test.py
"""
from typing import List


# def remove_element(nums: List[int], val: int):
#     i = 0

#     if not nums:
#         return i

#     while i < len(nums):
#         if nums[i] == val:
#             break
#         i += 1

#     j = i + 1
#     while j < len(nums):
#         if nums[j] != val:
#             nums[i] = nums[j]
#             i += 1
#         j += 1

#     return i

# def remove_element(nums: List[int], val: int):
#     left, right = 0, len(nums)
#     while left < right:
#         if nums[left] == val:
#             right -= 1
#             nums[left] = nums[right]
#         else:
#             left += 1
#     return left, nums

def remove_element(nums: list[int], val: int) -> int:
    write = 0
    for num in nums:
        if num != val:
            nums[write] = num
            write += 1
    return write

print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
