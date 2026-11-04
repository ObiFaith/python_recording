def binary_search(numbers, target):
    result, comparisonss = -1, 0
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        comparisonss += 1

        if numbers[mid] < target:
            left = mid + 1
        else:
            if numbers[mid] == target:
                result = mid
            right = mid - 1

    return result, comparisonss


# bonus
def recursive_binary_search(numbers, target):
    def search(left, right, result, comparisons):
        if left > right:
            return result, comparisons

        comparisons += 1
        mid = (left + right) // 2

        if numbers[mid] < target:
            return search(mid+1, right, result, comparisons)

        if numbers[mid] == target:
            result = mid

        return search(left, mid-1, result, comparisons)

    return search(0, len(numbers) - 1, -1, 0)

# print(binary_search([1, 3, 3, 3, 5, 8], 3))
# print(binary_search([1, 3, 5, 8], 4))
# print(binary_search([], 7))

print(recursive_binary_search([1, 3, 3, 3, 5, 8], 3))
print(recursive_binary_search([1, 3, 5, 8], 4))
print(recursive_binary_search([], 7))
