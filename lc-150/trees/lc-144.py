from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pass

        res = []

        def wrapper(root):

            if root is None:
                return

            res.append(root.val)
            wrapper(root.left)
            wrapper(root.right)

        wrapper(root=root)
        return res
