def can_sum(nums, target, i=0):
    if target == 0:
        return True

    if i == len(nums) - 1 and max(nums) > 0 and target < 0:
        return False

    print(nums, target, i)

    return can_sum(nums, target-nums[i], i+1) or can_sum(nums, target, i+1)

print(can_sum([2, 4, 6, 10], 16))
