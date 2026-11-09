def binary_search(numbers, target):
    result, comparisons = -1, 0
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if numbers[mid] < target:
            left = mid + 1
        else:
            if numbers[mid] == target:
                result = mid
            right = mid - 1

    return result, comparisons


# bonus
def recursive_binary_search(numbers, target):
    def search(left, right, prev_mid, left_index, right_index, comparisons):
        if left > right:
            return left_index, right_index, comparisons

        comparisons += 1
        mid = (left + right) // 2

        if numbers[mid] < target:
            return search(mid+1, right, prev_mid, left_index, right_index, comparisons)

        if numbers[mid] == target:
            left_index = mid
            right_index = mid

            if prev_mid > mid:
                right_index = mid

        return search(left, mid-1, prev_mid, left_index, right_index, comparisons)

    return search(0, len(numbers) - 1, (len(numbers) - 1) // 2, -1, -1, 0)

# print(binary_search([1, 3, 3, 3, 5, 8], 3))
# print(binary_search([1, 3, 5, 8], 4))
# print(binary_search([], 7))

print(recursive_binary_search([1, 3, 3, 3, 5, 8], 3))
print(recursive_binary_search([1, 3, 5, 8], 4))
print(recursive_binary_search([], 7))
