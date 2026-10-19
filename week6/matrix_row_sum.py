def matrix_row_sum(matrix: list[list[int]]) -> str:
    col_totals = [0] * len(matrix[0])
    output = []

    for row_idx, row in enumerate(matrix, start=1):
        row_total = 0
        for col_idx, value in enumerate(row):
            row_total += value
            col_totals[col_idx] += value

        average = row_total / len(row)
        output.append(
            f"Row {row_idx} total: {row_total} | "
            f"Row {row_idx} average: {average:.1f}"
        )

    print()

    for col_idx, col_total in enumerate(col_totals, start=1):
        output.append(f"Column {col_idx} total: {col_total}")

    return "\n".join(output)

print(matrix_row_sum([[2, 4, 6], [1, 3, 5], [10, 20, 30]]))
