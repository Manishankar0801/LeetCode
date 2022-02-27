# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        n = []
        def univalue(root):
            if root:
                n.append(root.val)
                univalue(root.left)
                univalue(root.right)
                
        univalue(root)
        return len(set(n)) ==1