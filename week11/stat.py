def stats(nums: list[int]) -> tuple[float, ...] | None:
    if not nums:
        return None

    smallest, largest, total = float("inf"), float("-inf"), 0

    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
        total += num

    average = total / len(nums)
    return (smallest, largest, average)

# print(stats([4, 9, 2, 7]))
# print(stats([5]))
# print(stats([-3, -1, -2]))
# print(stats([]))