# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def max_height(node):
            if not node:
                return 0

            lh = max_height(node.left)
            rh = max_height(node.right)

            self.res = max(self.res, lh+rh)
            return 1 + max(lh, rh)
        
        max_height(root)
        return self.res