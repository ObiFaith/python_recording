def roman_to_integer(roman_numeral: str) -> int:
    symbols = {'i': 1, 'iv': 4, 'v': 5, 'ix': 9, 'x': 10, 'xl': 40, 'l': 50, 'xc': 90, 'c': 100, 'cm': 900, 'm': 1000}

    i, integer, roman = 0, 0, roman_numeral.lower()
    length = len(roman)

    while i < length:
        if roman[i] == 'i' and i+1 < length and roman[i+1] == 'v':
            integer += symbols['iv']
            i += 1
        elif roman[i] == 'i' and i+1 < length and roman[i+1] == 'x':
            integer += symbols['ix']
            i += 1
        elif roman[i] == 'x' and i+1 < length and roman[i+1] == 'l':
            integer += symbols['xl']
            i += 1
        elif roman[i] == 'x' and i+1 < length and roman[i+1] == 'c':
            integer += symbols['xc']
            i += 1
        elif roman[i] == 'c' and i+1 < length and roman[i+1] == 'm':
            integer += symbols['cm']
            i += 1
        else:
            integer += symbols[roman[i]]

        i += 1

    return integer

print(roman_to_integer('III'))
print(roman_to_integer('LVIII'))
print(roman_to_integer('MCMXCIV'))
