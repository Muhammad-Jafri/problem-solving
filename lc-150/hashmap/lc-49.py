from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_freq(word) -> list[int]:  # type: ignore
            freq_list = [0 for i in range(26)]
            for w in word:
                # Get the number mapping for the word
                idx = ord(w) - ord("a")
                print(idx)
                freq_list[idx] += 1

            return freq_list

        hashmap = defaultdict(list)

        for str in strs:
            key = tuple(get_freq(str))
            hashmap[key].append(str)

        return list(hashmap.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))
