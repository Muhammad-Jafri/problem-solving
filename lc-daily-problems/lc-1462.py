from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        res = []
        adj_rep = defaultdict(list)
        for u, v in prerequisites:
            adj_rep[u].append(v)

        def dfs(adj_list, start):
            visited = set()
            res = []

            def dfs_wrapper(adj_list, node):
                visited.add(node)
                res.append(node)
                for adj_node in adj_list[node]:
                    if adj_node not in visited:
                        dfs_wrapper(adj_list, adj_node)

            dfs_wrapper(adj_list, start)

            return res

        for start, end in queries:
            if end in dfs(adj_rep, start):
                res.append(True)
            else:
                res.append(False)

        return res


numCourses = 3
prerequisites = [[1, 2], [1, 0], [2, 0]]
queries = [[1, 0], [1, 2]]
print(
    Solution().checkIfPrerequisite(
        numCourses=numCourses, prerequisites=prerequisites, queries=queries
    )
)
