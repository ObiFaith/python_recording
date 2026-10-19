numbers_str = input("Numbers: ").replace("[", "").replace("]", "").split(",")
target = int(input("Target: "))

numbers = [0] * len(numbers_str)

for num_str in numbers_str:
    numbers.append(int(num_str))

def find_pairs(numbers: list[int], target: int):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target:
                return numbers[i], numbers[j]

print("Output: ", find_pairs(numbers, target))