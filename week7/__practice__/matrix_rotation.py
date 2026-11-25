def get_j_col(M: list[list[int]], j: int) -> list[int]:
    col = [row[j] for row in M]
    # for row in M:
    #     col.append(row[j])
    return col

def get_cols(M: list[list[int]]):
    return list(map(list, zip(*M)))

def reverse_list(u: list[int]) -> list[int]:
    result = u.copy()

    i, j = 0, len(u) - 1

    while i < j:
        result[i], result[j] = result[j], result[i]
        i += 1
        j -= 1

    return result

def matrix_transpose(matrix: list[list[int]]) -> list[list[int]]:
    result = []

    for j in range(len(matrix[0])):
        cols = get_j_col(matrix, j)
        result.append(cols)

    return result

def matrix_rotation(matrix: list[list[int]]) -> list[list[int]]:
    result = matrix_transpose(matrix)
    for i, row in enumerate(result):
        result[i] = reverse_list(row)
    return result


# print(matrix_rotation([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]))
