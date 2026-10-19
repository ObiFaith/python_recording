def two_sum(nums: list[int], target: int) -> list[int]:
    i, j = 0, len(nums) - 1

    while i < j:
        if nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            return [i, j]

    return []

print("Output:", two_sum([2, 7, 11, 15], 9))
