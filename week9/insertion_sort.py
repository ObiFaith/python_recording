def insertion_sort(nums: list[int]):
    if not nums or len(nums) == 1:
        return nums

    sorted = [nums[0]]
    unsorted = nums[1:]

    for i in range(len(sorted), -1, -1):
        key = unsorted[0]
        if key < sorted[i]:
            sorted.insert(0, key)
            unsorted.pop(0)

    return nums

print(insertion_sort([5, 2, 4, 1]))
