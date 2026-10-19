numbers = [9, 7]

def get_second_largest(numbers: list[int]):
    largest = max(numbers)
    second_largest = min(numbers)

    for num in numbers:
        if second_largest < num < largest:
            second_largest = num

    return second_largest

print(get_second_largest(numbers))
