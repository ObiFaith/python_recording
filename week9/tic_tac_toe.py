def game_status(board: list[list[str]]) -> str:
    row_len, col_len = len(board), len(board[0])

    if row_len != 3 and col_len != 3:
        return "Invalid board"

    board_count, diagonal = 0, ['', '', '']

    # row check
    for row in board:
        if row[0].strip() != "" and row[0] == row[1] == row[2]:
            return f"{row[0]} wins"

    # column check
    for id, cols in enumerate(zip(board[0], board[1], board[2])):
        i, j, k = cols

        if i.strip() != "" and i == j == k:
            return f"{i} wins"

        diagonal[id] = cols[id]

        board_count += 1 if i.strip() != "" else 0
        board_count += 1 if j.strip() != "" else 0
        board_count += 1 if k.strip() != "" else 0

    # diagonal check
    if diagonal[0].strip() != "" and diagonal[0] == diagonal[1] == diagonal[2]:
        return f"{diagonal[0]} wins"

    return "Draw" if board_count == 9 else "In progress"

print(game_status([["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]]))     # "X wins"

print(game_status([["O", "X", "X"],
             ["X", "O", " "],
             [" ", " ", "O"]]))      # "O wins"  (diagonal)

print(game_status([["X", "O", "X"],
             ["O", "X", "O"],
             ["O", "X", "O"]]))     # "Draw"

print(game_status([["X", " ", " "],
             [" ", "O", " "],
             [" ", " ", " "]]))     # "In progress"

