from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stones to negative values for max heap
        heap = [-s for s in stones]
        heapq.heapify(heap)  # More efficient than pushing one by one

        while len(heap) > 1:
            first_stone = -heapq.heappop(heap)
            second_stone = -heapq.heappop(heap)
            delta = first_stone - second_stone
            if delta > 0:
                heapq.heappush(heap, -delta)

        # Return the absolute value of the last stone if exists, otherwise 0
        return -heap[0] if heap else 0
