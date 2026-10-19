matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]

def matrix_row_sum(matrix: list[list[int]]) -> str:
    output = ""

    for idx in range(len(matrix)):
        row_sum = 0
        for index in range(len(matrix[idx])):
            row_sum += matrix[idx][index]
        output += f"Row {idx + 1}, total: {row_sum}\n"

    return output

print(matrix_row_sum(matrix))
