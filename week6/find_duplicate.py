def find_duplicate(numbers: list[int]):
    dup_dict = {}
    for number in numbers:
        dup_dict[number] = dup_dict.get(number, 0) + 1

    duplicate = {k: v for k, v in dup_dict.items() if v > 1}
    return duplicate

print(find_duplicate([1, 2, 3, 2, 4, 5, 1]))
print(find_duplicate([4, 4, 4, 4]))
print(find_duplicate([1, 2, 3, 4]))
print(find_duplicate([10, 20, 10, 30, 20]))
