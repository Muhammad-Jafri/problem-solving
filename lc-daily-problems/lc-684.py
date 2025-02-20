from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Find a cycle starting from the node having the lesser in degrees, and remove the last connection

        adj_list = defaultdict(list)

        for start, end in edges:  #
            adj_list[start].append(end)
            adj_list[end].append(start)

        print(adj_list)
        # Starting node with the least amount of indegrees
        start_node = ...

        def get_cycle(node: int):
            pass


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(Solution().findRedundantConnection(edges))
