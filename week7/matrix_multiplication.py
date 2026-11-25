def matrix_multiplication(matrix_a: list[list[int]], matrix_b: list[list[int]]):
    if not matrix_a or not matrix_b:
        return None

    n, m, p = len(matrix_a), len(matrix_b), len(matrix_b[0])

    if any(len(row) != m for row in matrix_a) or any(len(row) != p for row in matrix_b):
        return None

    result = [[0] * p for _ in range(n)]

    for i in range(n):
        a_row = matrix_a[i]
        result_row = result[i]
        for k in range(m):
            a_ik = a_row[k]
            b_row = matrix_b[k]
            for j in range(p):
                result_row[j] += a_ik * b_row[j]

    return result

print(matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]))