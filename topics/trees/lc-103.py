from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            lvl_vals = []
            no_objs = len(queue)
            for i in range(no_objs):
                cur_node = queue.popleft()
                lvl_vals.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

            res.append(lvl_vals)

        for i in range(len(res)):
            if i % 2 == 1:
                # Reverse the sublist
                res[i] = list(reversed(res[i]))

        return res
