from typing import List
import heapq


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Find indices range for same chars, create a min heap and take (n - 1) elements
        res = 0

        def find_repeating_ranges(s):
            if not s:
                return []

            ranges = []
            start = 0

            for i in range(1, len(s)):
                if s[i] != s[i - 1]:
                    if i - start > 1:
                        ranges.append((start, i - 1))
                    start = i

            if len(s) - start > 1:
                ranges.append((start, len(s) - 1))

            return ranges

        ranges = find_repeating_ranges(colors)

        for start, end in ranges:
            heap = neededTime[start : end + 1]
            heapq.heapify(heap)

            for i in range(len(heap) - 1):
                res += heapq.heappop(heap)

        return res


colors = "abaac"
neededTime = [1, 2, 3, 4, 5]
print(Solution().minCost(colors=colors, neededTime=neededTime))
