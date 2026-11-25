def transpose_in_place(matrix: list[list[int]]) -> None:
    """Transpose an n x m matrix, mutating the original list object."""
    if not matrix:
        return

    r, c = len(matrix), len(matrix[0])
    if r == c:
        for i in range(r):
            for j in range(i+1, r):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
    else:
        result = [[0] * r for _ in range(c)]

        for i in range(r):
            for j in range(c):
                result[j][i] = matrix[i][j]

        matrix[:] = result

m = [[1, 2, 3],
     [4, 5, 6]]
transpose_in_place(m)
print(m)

def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return list(map(list, zip(*matrix)))

def transpose2(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []

    # return [[matrix[i][j] for i in range(n)] for j in range(m)]

    result = []
    r, c = len(matrix), len(matrix[0])
    for j in range(c):
        row = []
        for i in range(r):
            row.append(matrix[i][j])
        result.append(row)
    return result

def rotate_clockwise2(matrix: list[list[int]]) -> list[list[int]]:
    """Return a new matrix rotated 90° clockwise. Works for any n x m matrix."""
    return list(map(list, zip(*reversed(matrix))))
    # return [list(row) for row in zip(*reversed(matrix))]

def rotate_clockwise(matrix: list[list[int]]) -> list[list[int]]:
    """Return a new matrix rotated 90° clockwise. Works for any n x m matrix."""
    if not matrix:
        return []

    r, c = len(matrix), len(matrix[0])
    result = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            result[j][r-1-i] = matrix[i][j]

    return result

# right = matrix[j][last-i]
# top = matrix[i][j]
# left = matrix[last-j][i]
# bottom = matrix[last-i][last-j]

def rotate_clockwise_in_place(matrix: list[list[int]]) -> None:
    """Rotate a square matrix 90° clockwise, modifying it in place."""
    n = len(matrix)
    last = n - 1

    for i in range(n // 2):
        for j in range(i, last - i):
            top = matrix[i][j]
            matrix[i][j] = matrix[j][last-i]
            matrix[j][last-i] = matrix[last-i][last-j]
            matrix[last-i][last-j] = matrix[last-j][i]
            matrix[last-j][i] = top


print(rotate_clockwise([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])) # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
