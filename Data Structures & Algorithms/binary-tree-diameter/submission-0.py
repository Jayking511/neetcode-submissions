# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def height(node: TreeNode):
            if not node:
                return 0
            return max(height(node.left), height(node.right))+1

        left_len = height(root.left)
        right_len = height(root.right)
        
        return max(left_len+right_len, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))