def dot(u: list[int], v: list[int]):
    if len(u) != len(v):
        return None

    total = 0
    for i in range(len(u)):
        total += u[i] * v[i]
    return total

def transformation_matrix(points: list[list[int]], T: list[list[int]]) -> list[list[int]]:
    if not points or not T:
        raise ValueError("Matrix can't be empty")

    result = []

    for point in points:
        if len(point) != 2:
            raise ValueError("Each point must have 2 coordinates")

        new_point = []
        for T_row in T:
            total = 0
            for i in range(len(T_row)):
                total += T_row[i] * point[i]
            new_point.append(total)
        result.append(new_point)

    return result

print(transformation_matrix([[3, 2], [1, 0], [0, 1]], [[0, -1], [1, 0]]))

# def transformation_matrix(points: list[list[int]], T: list[list[int]]) -> list[list[int]]:
#     if not points or not T:
#         raise ValueError("Matrix can't be empty")

#     result = []

#     for row in points:
#         data = []
#         for i in range(2):
#                 data.append(dot(row, get_col(T, i)))
#         result.append(data)

#     return result