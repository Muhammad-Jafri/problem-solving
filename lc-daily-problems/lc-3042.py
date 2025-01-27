from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def is_prefix_suffix(str_1, str_2):

            return str_2.endswith(str_1) and str_2.startswith(str_1)

        res = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                print(f"idx {i} {j}")
                if is_prefix_suffix(words[i], words[j]):
                    res += 1

        return res


words = ["a","abb"]
sol = Solution()
print(sol.countPrefixSuffixPairs(words))