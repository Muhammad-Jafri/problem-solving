from typing import List
from collections import Counter, defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def is_subset(word_dict: dict, required_counts: dict) -> bool:
            # Check if required_counts (from words2) is a subset of word_dict (from words1)
            for char, count in required_counts.items():
                if word_dict.get(char, 0) < count:
                    return False
            return True

        # Create a combined frequency count for words2
        combined_count = defaultdict(int)
        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                combined_count[char] = max(combined_count[char], count)

        # Check each word in words1
        result = []
        for word in words1:
            word_count = Counter(word)
            if is_subset(word_count, combined_count):
                result.append(word)

        return result

# Test
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["l", "e"]
print(Solution().wordSubsets(words1=words1, words2=words2))