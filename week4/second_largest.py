def second_largest(nums: list[int]) -> int:
    largest, second_largest = nums[0], nums[0]

    for num in nums:
        if num > largest:
            largest = num
        elif second_largest < num < largest:
            second_largest = num

    return second_largest

print(second_largest([10, 5, 8, 20, 15]))
print(second_largest([4, 9, 2, 9, 7]))
