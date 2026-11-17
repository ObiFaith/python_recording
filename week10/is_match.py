def is_match(text, pattern):
    wildcards = {"*", "?"}
    if (len(pattern) <= 1 and pattern != '?') or (len(text) == 1 and pattern == '?'):
        return True

    if (pattern[0] not in wildcards and (text[0] != pattern[0])) or (pattern[-1] not in wildcards and (text[-1] != pattern[-1])):
        return False

    if (pattern[0] in wildcards or text[0] == pattern[0]) and (pattern[-1] in wildcards or text[-1] == pattern[-1]):
        return is_match(text[1:-1], pattern[1:-1])

print(is_match("hello", "h*o"))
print(is_match("cat", "c?t"))
print(is_match("dog", "d*g?"))
print(is_match("dogs", "d*g?"))
print(is_match("abc", "*"))