from typing import List


class Solution:
    def stringMatching(
        self, words: List[str]
    ) -> List[str]:  # Brute forcing the shit out of this one
        res = set()
        n = len(words)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if words[i] in words[j]:
                    res.add(words[i])

        return list(res)


sol = Solution()
words = ["leetcoder", "leetcode", "od", "hamlet", "am"]
print(sol.stringMatching(words=words))
