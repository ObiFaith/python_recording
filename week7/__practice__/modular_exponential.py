def modular_exponentiation(base: int, exp: int, mod: int):
    if exp < 0 or mod < 1:
        raise ValueError("exp must be >= 0 and mod must be >= 1")

    result = 1
    base %= mod

    while exp > 0:
        if exp % 2 == 1:
            result = result * base % mod
        exp //= 2
        base = base * base % mod

    return result


# print(modular_exponentiation(2, 10, 1000))    # 24
# print(modular_exponentiation(3, 0, 7))        # 1
# print(modular_exponentiation(7, 128, 13))     # 3
# print(modular_exponentiation(5, 3, 1))        # 0
print(modular_exponentiation(2, 10**18, 10**9 + 7))  # instant