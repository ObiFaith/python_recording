def list_analyzer(numbers: list[int]) -> str:
    min_idx = max_idx = total = 0

    for idx, number in enumerate(numbers):
        if numbers[min_idx] > number:
            min_idx = idx
        elif numbers[max_idx] < number:
            max_idx = idx

        total += number

    average = total / len(numbers)

    above_average = 0
    for number in numbers:
        if number > average:
            above_average += 1

    return (
        f"Smallest: {numbers[min_idx]} (at index {min_idx})\n"
        f"Largest: {numbers[max_idx]} (at index {max_idx})\n"
        f"Total: {total}\nAverage: {average:.2f}\n"
        f"Numbers above average: {above_average}"
    )

print(list_analyzer([12, 5, 27, 8, 14, 27, 3]))