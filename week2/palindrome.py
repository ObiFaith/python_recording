def is_palindrome(input: str):
    input_len = len(input)
    if input_len < 2:
        return True

    for i in range(int(input_len / 2)):
        if input[i] != input[- i - 1]:
            return False

    return True

text = input("Input: ")
if is_palindrome(text.lower()):
    print("Palindrome")
else:
    print("Not a palindrome")