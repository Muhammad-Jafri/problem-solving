from collections import Counter


class Solution:
    def canConstruct(
        self, s: str, k: int
    ) -> bool:  # Now understand this solution you fathead
        if k > len(s):
            return False

        count = Counter(s)
        odd = 0

        for cnt in count.values():
            if cnt % 2 == 1:
                odd += 1

        return odd <= k
