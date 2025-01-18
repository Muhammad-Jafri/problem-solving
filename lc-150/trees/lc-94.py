from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def wrapper(root):

            if (
                root is None
            ):  # Base case itself is wrong bro, the limit would be when you encounter a None node not a leaf node.
                return

            wrapper(root.left)
            res.append(root.val)
            wrapper(root.right)

        wrapper(root=root)

        return res
