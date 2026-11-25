def fizzbuzz_plus(n: int) -> str | list:
    output = ""

    if n == 0:
        return []

    # items = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
    # for key in items.keys():
    #     if n % key == 0:
    #         output += items[key]
    #     elif n % key != 0:
    #         output += str(n)

    if n % 3 == 0:
        output += "Fizz"
    if n % 5 == 0:
        output += "Buzz"
    if n % 7 == 0:
        output += "Bazz"
    if not (n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
        output += str(n)

    return "".join(output)

# print(fizzbuzz_plus(3))
# print(fizzbuzz_plus(15))
# print(fizzbuzz_plus(21))
# print(fizzbuzz_plus(35))
# print(fizzbuzz_plus(105))
# print(fizzbuzz_plus(0))
