def roman_to_total(roman_numeral: str) -> int:
    values = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}

    roman = roman_numeral.lower()
    length = len(roman)
    total, i = 0, 0

    while i < length:
        current = values[roman[i]]
        if i + 1 < length and current < values[roman[i + 1]]:
            total -= current
        else:
            total += current

        i += 1

    return total

print(roman_to_total('III'))
print(roman_to_total('LVIII'))
print(roman_to_total('MCMXCIV'))
