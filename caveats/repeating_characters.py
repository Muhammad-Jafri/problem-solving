def is_repeating(s: str):

    sub = ""

    for c in s:  # Getting the repeating bit

        if c in sub:
            break
        else:
            sub += c

    print(sub)
    if len(s) % len(sub) != 0:
        return False
    ptr = 0
    for c in s:

        if ptr >= len(sub):
            ptr = 0

        if sub[ptr] != c:
            return False

        ptr += 1

    return True


test_case = "abcabcabc"
print(is_repeating(s=test_case))
