# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postorder(root, res):
            if root:
                postorder(root.left, res)
                res.append(root.val)
                postorder(root.right, res)
            return res
        return postorder(root, res)