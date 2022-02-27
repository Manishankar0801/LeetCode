# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        n = 0
        if not root:
            return n
        if root.left and not root.left.left and not root.left.right:
                n += root.left.val
        return n + self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)