from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        res = set() # (middle, outer)
        left = set() # Keep track of the things we have seen
        right_hashmap = Counter(s) # Keep track of things on the right

        for m in range(len(s)):

            right_hashmap[s[m]] -= 1 
            if right_hashmap[s[m]] == 0:
                right_hashmap.pop(s[m]) # Ensures we are not counting the middle twice

            for c in range(26):

                character = chr(ord("a") + c)

                if character in left and character in right_hashmap:

                    res.add((s[m], character))

            left.add(s[m])

        return len(res)


sol = Solution()
s = "adc"
print(sol.countPalindromicSubsequence(s=s))
