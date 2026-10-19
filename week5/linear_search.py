values = [14, 7, 22, 9, 7, 31]

def linear_search(numbers: list[int], target) -> str:
    for i in range(len(numbers)):
        if numbers[i] == target:
            return f"Found at index {i}"
    return "Target not found"

print(linear_search(values, 22))
print(linear_search(values, 18))
