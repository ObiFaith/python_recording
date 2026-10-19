def is_palindrome(user_input: str) -> bool:
    input_len = len(user_input)
    for i in range(input_len // 2):
        if user_input[i] != user_input[input_len - i - 1]:
            return False
    return True

user_input = input("Input: ")
palindrome = is_palindrome(user_input)
output = f"{user_input} is a palindrome" if palindrome else f"{user_input} is not a palindrome"
print("Output:", output)
