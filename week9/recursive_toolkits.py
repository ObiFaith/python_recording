def digit_sum(num: int) -> int:
    if num // 10 == 0:
        return num
    return (num % 10) + digit_sum(num // 10)

# print(digit_sum(1234))
# print(digit_sum(0))

def power(base: int, exp: int) -> int:
    if exp == 0:
        return 1

    return base * power(base, exp-1)

# print(power(2, 10))
# print(power(5, 0))


def reverse_text(text: str) -> str:
    if not text or len(text) == 1:
        return text

    return text[-1] + reverse_text(text[:-1])

# print(reverse_text("abcde"))
# print(reverse_text(""))


def count_char(text: str, ch: str) -> int:
    if not text:
        return 0

    if text[0] == ch:
        return 1 + count_char(text[1:], ch)

    return 0 + count_char(text[1:], ch)

# print(count_char("banana", "a"))
