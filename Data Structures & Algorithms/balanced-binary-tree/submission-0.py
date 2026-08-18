# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def height_bal(node):
            if not node:
                return
            l_max = max_height(node.left)
            r_max = max_height(node.right)
            if abs(l_max-r_max) > 1:
                self.res = False
            height_bal(node.left)
            height_bal(node.right)
        def max_height(node):
            if not node:
                return 0
            lh = max_height(node.left)
            rh = max_height(node.right)
            return 1 + max(lh, rh)
        height_bal(root)
        return self.res