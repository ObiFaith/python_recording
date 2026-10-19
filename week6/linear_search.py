def linear_search(numbers: list[int], target: int) -> str:
    indices = []

    for idx, number in enumerate(numbers):
        if number == target:
            indices.append(idx)

    if not indices:
        return "Target not found"

    return (
        f"Found at indices: {indices} | Count: {len(indices)} | "
        f"First: {indices[0]} | Last: {indices[-1]}"
    )

print(linear_search([14, 7, 22, 9, 7, 31, 7, 5], 9))
print(linear_search([14, 7, 22, 9, 7, 31, 7, 5], 22))
print(linear_search([14, 7, 22, 9, 7, 31, 7, 5], 18))
