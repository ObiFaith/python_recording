def multiply(A, B) -> list[list[int]]:
    if not A or not B or len(A[0]) != len(B):
        raise ValueError("Columns of A must equal rows of B")

    n, m, p = len(A), len(B), len(B[0])
    result = [[0] * p for _ in range(n)]

    for i in range(n):
        result_row = result[i]
        a_row = A[i]

        for k in range(m):
            a_ik = a_row[k]
            b_row = B[k]

            for j in range(p):
                result_row[j] += a_ik * b_row[j]

    return result

def identity(n: int) -> list[list[int]]:
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(1 if i == j else 0)
        matrix.append(row)
    return matrix


def matrix_power(A: list[list[int]], k: int) -> list[list[int]]:
    if k < 0:
        raise ValueError("k must be non-negative")

    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("A must be a square matrix")

    base = A # [[1, 1], [1, 0]]
    result = identity(n) # [[1, 0], [0, 1]]

    while k > 0:
        if k % 2 == 1:
            result = multiply(result, base) # A1 = [[1, 1], [1, 0]], A5 = [[8, 5], [5, 3]]
        k //= 2
        if k > 0:
            base = multiply(base, base) # A2 = [[2,1],[1,1]], A4 = [[5,3],[3,2]]

    return result

print(matrix_power([[1, 1], [1, 0]], 5))


# def square_matrix(A: list[list[int]], k: int=0):
#     if k == 0:
#         return identity(len(A))

#     if k == 1:
#         return A

#     result = A

#     for _ in range(1, k):
#         result = multiply(result, A)

#     return result
