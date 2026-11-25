def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return the matrix elements in spiral order without modifying it."""
    result = []
    if not matrix or not matrix[0]:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):           # → top row
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):           # ↓ right column
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:                            # ← bottom row
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:                            # ↑ left column
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

def spiral_order2(matrix: list[list[int]]) -> list[int]:
    """Return the matrix elements in spiral order without modifying it."""
    result = []

    if not matrix or not matrix[0]:
        return result

    start, end = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while start <= end and left <= right:
        for col in range(left, right+1):
            result.append(matrix[start][col])
        start += 1

        for row in range(start, end+1):
            result.append(matrix[row][right])
        right -= 1

        if start <= end:
            

    return result


print(spiral_order2([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]))          # [1, 2, 3, 6, 9, 8, 7, 4, 5]

# print(spiral_order([[1, 2, 3, 4],
#               [5, 6, 7, 8]]))       # [1, 2, 3, 4, 8, 7, 6, 5]

# print(spiral_order([[1], [2], [3]]))      # [1, 2, 3]
# print(spiral_order([]))                   # []


