def is_valid(s: str):
    stack = []

    for p in s:
        # If p is an opening bracket
        if p == "(":
            stack.append(p)
        # If p is a closing bracket
        elif p == ")":
            if not stack:  # If the stack is empty, no matching opening parenthesis
                return False
            stack.pop()  # Pop the last opening bracket

    # Return True if all brackets were matched, False otherwise
    return len(stack) == 0


# Test case
a = "(()))"
print(is_valid(s=a))  # Output: False
