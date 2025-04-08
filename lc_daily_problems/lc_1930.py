from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()  # (MID, OUTER)
        left = set()  # Keep track of the elements to the left
        right = Counter(s)  # Keep track of elements to the right

        for m in range(len(s)):
            right[s[m]] -= 1
            if right[s[m]] == 0:
                right.pop(s[m])

            for c in range(26):
                character = chr(ord("a") + c)

                if character in left and character in right:
                    res.add((s[m], character))

            left.add(s[m])

        return len(res)


sol = Solution()
s = "aabca"
print(sol.countPalindromicSubsequence(s=s))
