ROMAN_PAIRS = (
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
    (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
    (1, "I"),
)


def integer_to_roman(num: int) -> str:
    if not 1 <= num <= 3999:
        raise ValueError(f"num must be between 1 and 3999, got {num}")

    output = []

    for value, symbol in ROMAN_PAIRS:
        if num == 0:
            break
        count, num = divmod(num, value)
        output.append(symbol * count)

    return "".join(output)

print(integer_to_roman(3))
print(integer_to_roman(4))
print(integer_to_roman(6))
print(integer_to_roman(9))
print(integer_to_roman(58))
print(integer_to_roman(900))
print(integer_to_roman(1994))

# i = 0
# while num > 0:
#     current, roman = ROMAN_PAIRS[i]
#     if num >= current:
#         output.append(roman)
#         num -= current
#     else:
#         i += 1
