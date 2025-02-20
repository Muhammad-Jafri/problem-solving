from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        n = len(words)
        prefix_sum = [0] * n

        def is_vowel_string(word: str) -> bool:
            return word[0] in vowels and word[-1] in vowels

        # Compute prefix sum based on the criteria
        prefix_sum[0] = 1 if is_vowel_string(words[0]) else 0
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + (1 if is_vowel_string(words[i]) else 0)

        # Process queries
        result = []
        for left, right in queries:
            if left == 0:
                result.append(prefix_sum[right])
            else:
                result.append(prefix_sum[right] - prefix_sum[left - 1])

        return result


# Example usage
words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]
sol = Solution()
print(sol.vowelStrings(words=words, queries=queries))
