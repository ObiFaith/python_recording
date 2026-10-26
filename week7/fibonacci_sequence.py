def add_value(value: int, fib_list: list[int], rev_fib_list: list[int]):
    fib_list.append(value)
    rev_fib_list.insert(0, value)


def fibonacci_sequence(n: int) -> tuple[list[int], list[int], int]:
    total, fib_list, rev_fib_list = 0, [], []

    if n == 0:
        return fib_list, rev_fib_list, total

    if n >= 1:
        fib_list.append(0)
        rev_fib_list.insert(0, 0)

    if n >= 2:
        add_value(1, fib_list, rev_fib_list)

    if n >= 3:
        add_value(1, fib_list, rev_fib_list)

    for i in range(3, n):
        value = fib_list[i-1] + fib_list[i-2]

        if value % 2 == 0:
            total += value

        add_value(value, fib_list, rev_fib_list)

    return fib_list, rev_fib_list, total


fib_list, rev_fib_list, total = fibonacci_sequence(8)

def join_numbers(numbers: list[int]) -> str:
    return ", ".join(map(str, numbers))

print(f"Sequence: {join_numbers(fib_list)}", f"Even Sum: {total}", f"Reversed: {join_numbers(rev_fib_list)}", sep="\n")
