from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:

        freq = Counter(s)
        res = 0

        for c, cnt in freq.items():

            # If the cnt is odd then we are left with 1 character
            if cnt % 2 == 1:
                res += 1
            # If the cnt is 2 we get the 2 characters
            else:
                res += 2

        return res
