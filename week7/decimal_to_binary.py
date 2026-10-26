def decimal_to_binary(n: int) -> str:
    output = ""

    while n > 0:
        remainder = n % 2
        output = str(remainder) + output
        n = n // 2

    return output

print(decimal_to_binary(10))
