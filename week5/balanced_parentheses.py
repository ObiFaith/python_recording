def balanced_parentheses(input: str) -> str:
    brackets = {
        '(': 0,
        ')': 0
    }

    for char in input:
        if char == '(':
            brackets['('] += 1
        elif char == ')':
            brackets[')'] += 1

    return "Balanced" if brackets['('] == brackets[')'] else "Not balanced"

print(balanced_parentheses("((a+b)"))
print(balanced_parentheses("(a+b) * (c-d)"))
