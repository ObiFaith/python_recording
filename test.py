def max_sum_of_k(numbers: list[int], k: int) -> int:
    j = k
    i = total = 0

    while j <= len(numbers):
        current_sum = sum(numbers[i:j])

        if current_sum > total:
            total = current_sum

        i += 1
        j += 1

    return total

def max_sum2_of_k(numbers: list[int], k: int) -> int:
    window_sum = sum(numbers[:k])
    max_sum = window_sum

    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        max_sum = max(window_sum, max_sum)

    return max_sum

print(max_sum2_of_k([1, 2, 3, 4, 5], 2))
