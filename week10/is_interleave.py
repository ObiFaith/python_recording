def is_interleave(s1, s2, s3, i=0, j=0):
    if len(s1) + len(s2) != len(s3):
        return False

    if i == len(s1) and j == len(s2):
        return True

    if i < len(s1) and s1[i] == s3[i+j]:
        return is_interleave(s1, s2, s3, i+1, j)

    if j < len(s2) and s2[j] == s3[i+j]:
        return is_interleave(s1, s2, s3, i, j+1)

print(is_interleave("abc", "def", "adbcef"))
print(is_interleave("aab", "axy", "aaxaby"))

