def matrix_row_sum(matrix: list[list[int]]) -> str:
    if not matrix or not matrix[0]:
        return ""

    num_cols = len(matrix[0])
    col_totals = [0] * num_cols
    output = []

    for row_idx, row in enumerate(matrix, start=1):
        if len(row) != num_cols:
            raise ValueError(f"Row {row_idx} has {len(row)} columns, expected {num_cols}")

        row_total = 0
        for col_idx, value in enumerate(row):
            row_total += value
            col_totals[col_idx] += value

        output.append(
            f"Row {row_idx} total: {row_total} | "
            f"Row {row_idx} average: {row_total / num_cols:.1f}"
        )

    for col_idx, col_total in enumerate(col_totals, start=1):
        output.append(f"Column {col_idx} total: {col_total}")

    return "\n".join(output)


print(matrix_row_sum([[2, 4, 6], [1, 3, 5], [10, 20, 30]]))
