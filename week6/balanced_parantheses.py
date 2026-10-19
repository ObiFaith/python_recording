def balanced_parantheses(text: str) -> str:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    openers = set(pairs.values())

    for char in text:
        if char in openers:
            stack.append(char)
        elif char in pairs:
            if not stack:
                return "Not balanced (mismatched type)"
            if stack.pop() != pairs[char]:
                return "Not balanced (wrong order)"

    return "Balanced" if not stack else "Not balanced (unclosed)"

print(balanced_parantheses("(a + b) * [c - d]"))
print(balanced_parantheses("(a + b)]"))
print(balanced_parantheses("((a + b)"))
print(balanced_parantheses("[(a + b) * {c - d}]"))
print(balanced_parantheses("([)]" ))
