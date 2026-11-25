def get_col(M: list[list[int]], j: int) -> list[int]:
    cols = []

    for i in range(len(M)):
        cols.append(M[i][j])

    return cols

def dot(u: list[int], v: list[int]) -> int | None:
    if len(u) != len(v):
        return None

    dot_sum = 0

    for i in range(len(u)):
        dot_sum += u[i] * v[i]

    return dot_sum

def cell(a: list[list[int]], b: list[list[int]], i: int, j: int) -> int | None:
    return dot(a[i], get_col(b, j))


def matrix_multiplication2(matrix_a: list[list[int]], matrix_b: list[list[int]]):
    if not matrix_a or not matrix_b or len(matrix_a[0]) != len(matrix_b):
        return

    multiplication = []
    row_len, col_len = len(matrix_a), len(matrix_b[0])

    for i in range(row_len):
        row = [0] * col_len
        for j in range(col_len):
            row[j] += cell(matrix_a, matrix_b, i, j) or 0
        multiplication.append(row)

    return multiplication

def has_uniform_width(matrix: list[list[int]], width: int) -> bool:
    return all(len(row) == width for row in matrix)


def matrix_multiplication3(matrix_a: list[list[int]], matrix_b: list[list[int]]):
    if not matrix_a or not matrix_b:
        return None

    cols = len(matrix_b[0])      # columns of B (and of the result)

    if not (has_uniform_width(matrix_a, len(matrix_b)) and has_uniform_width(matrix_b, cols)):
        return None

    result = [[0] * cols for _ in matrix_a]          # list comprehension

    for a_row, result_row in zip(matrix_a, result):  # zip: A's row with its output row
        for a_ik, b_row in zip(a_row, matrix_b):     # zip: A[i][k] with B's row k
            for j, b_kj in enumerate(b_row):         # enumerate: column index + value
                result_row[j] += a_ik * b_kj

    return result
