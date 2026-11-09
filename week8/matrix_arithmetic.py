matrix_a = [[4, 7, 1], [9, 2, 6], [5, 8, 3]]
matrix_b = [[1, 0, 2], [3, 5, 4], [2, 1, 1]]

def same_shape(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> bool:
    return (
        len(matrix_a) == len(matrix_b)
        and len(matrix_a[0]) == len(matrix_b[0])
    )

def matrix_addition(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]] | None:
    not_same_shape = not same_shape(matrix_a, matrix_b)

    if not_same_shape:
        return None

    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(matrix_a, matrix_b)]

def matrix_subtraction(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]] | None:
    not_same_shape = not same_shape(matrix_a, matrix_b)

    if not_same_shape:
        return None

    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(matrix_a, matrix_b)]



def total(numbers: list[int]):
    sum_total = 0
    for i in range(len(numbers)):
        sum_total += numbers[i]
    return sum_total

def dot(u: list[int], v: list[int]):
    if len(u) != len(v):
        return 0

    dot_sum = 0

    for i in range(len(u)):
        dot_sum += u[i] * v[i]

    return dot_sum

def get_row(M: list[list[int]], i: int) -> list[int]:
    return M[i]

def get_col(M: list[list[int]], j: int) -> list[int]:
    output = []
    for i in range(len(M)):
        output.append(M[i][j])
    return output

def make_grid(rows, cols):
    grid = []

    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(0)
        grid.append(row)

    grid[0][0] = 9
    return grid

def multiplication_table(rows, cols):
    multiplication = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(i * j)
        multiplication.append(row)
    return multiplication

def cell(a: list[list[int]], b: list[list[int]], i: int, j: int) -> int | None:
    return dot(get_row(a, i), get_col(b, j))

def matrix_times_vector(M: list[list[int]], v: list[int]) -> list[int] | None:
    if not M or len(M[0]) != len(v):
        return

    result = []
    for row in M:
        result.append(dot(row, v))
    return result


def matrix_multiplication(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]] | None:
    if not matrix_a or not matrix_b or len(matrix_a[0]) != len(matrix_b):
        return

    multiplication = []

    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            col = [matrix_b[i][j] for i in range(len(matrix_b))] # get_col(matrix_b, j)
            row.append(dot(matrix_a[i], col))
        multiplication.append(row)

    return multiplication

print(matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
