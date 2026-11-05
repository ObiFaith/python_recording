def fibonacci_report(n: int):
    a, b = 0, 1
    sep, even_sum  = '', 0

    print("Sequence: ", end="")

    for _ in range(n):
        print(f"{sep}{a}", end="")
        sep = ", "

        if a % 2 == 0:
            even_sum += a

        a, b = b, a + b

    print("\nEven Sum:", even_sum)

    sep = ''
    a, b = b - a, a

    print("Reversed: ", end="")

    for _ in range(n):
        print(f"{sep}{a}", end="")
        sep = ', '
        a, b = b - a, a

    print()

fibonacci_report(8)