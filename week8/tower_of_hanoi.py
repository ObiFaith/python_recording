def tower_of_hanoi(n, source, target, helper):
    moves = []

    if n == 1:
        moves.append((source, target))
    else:
        moves.extend(tower_of_hanoi(n-1, source, helper, target))
        moves.append((source, target))
        moves.extend(tower_of_hanoi(n-1, helper, target, source))

    return moves

if __name__ == "__main__":
    n = 6
    print(tower_of_hanoi(n, "A", "B", "C"))