def count_paths(rows, cols):
    downward_moves = rows - 1
    rightward_moves = cols - 1

    total_steps = downward_moves + rightward_moves
    

print(count_paths(2, 2))
print(count_paths(3, 3))
print(count_paths(3, 3))
print(count_paths(1, 5))
print(count_paths(3, 7))
