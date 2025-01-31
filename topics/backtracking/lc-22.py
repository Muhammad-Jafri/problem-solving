from typing import List


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:

#         def is_correct(s: str):  #  )()

#             stack = []

#             for br in s:

#                 if br == "(":
#                     stack.append(br)
#                 elif br == ")":

#                     if stack == []:
#                         return False
#                     stack.pop()

#             return len(stack) == 0

#         candidates = []

#         def backtract(path: str):

#             if len(path) == 2 * n:
#                 candidates.append(path)
#                 return

#             for br in ["(", ")"]:
#                 backtract(path + br)

#         backtract(path="")

#         # Check each str in candidates for the criteria "is_correct"
#         return [c for c in candidates if is_correct(c)]

# n = 3
# print(Solution().generateParenthesis(n=n))


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        candidates = []

        def backtrack(path: str, open_count: int, close_count: int):
            if len(path) == 2 * n:
                candidates.append(path)
                return

            if open_count < n:
                backtrack(path + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(path + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return candidates


n = 2
