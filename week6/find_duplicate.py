def find_duplicate(numbers: list[int]):
    count = {}
    for number in numbers:
        count[number] = count.get(number, 0) + 1

    return [number for number, count in count.items() if count > 1]

print(find_duplicate([1, 2, 3, 2, 4, 5, 1]))
print(find_duplicate([4, 4, 4, 4]))
print(find_duplicate([1, 2, 3, 4]))
print(find_duplicate([10, 20, 10, 30, 20]))
