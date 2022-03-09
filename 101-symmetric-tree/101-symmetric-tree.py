class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check_children(root.left, root.right)
        
    def check_children(self, root1, root2):
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (root2 and not root1):
            return False
        if root1.val != root2.val:
            return False
        else:
            return self.check_children(root1.left, root2.right) and self.check_children(root1.right, root2.left)
        