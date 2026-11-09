def balanced_brackets(text: str) -> bool:
    if not text:
        return True

    i, stack = 0, []
    brackets = {"}": "{", "]": "[", ")": "("}
    open, closed = set(brackets.values()), set(brackets.keys())

    while i < len(text):
        if text[i] in open:
            stack.append(text[i])
        elif text[i] in closed:
            if not stack or stack[-1] != brackets[text[i]]:
                return False
            else:
                stack.pop()

        i += 1

    return len(stack) == 0

print(balanced_brackets("(a + b) * [c - d]"))
print(balanced_brackets("{[()]}"))
print(balanced_brackets("([)]"))
print(balanced_brackets("(("))
print(balanced_brackets("}{"))
print(balanced_brackets(""))

