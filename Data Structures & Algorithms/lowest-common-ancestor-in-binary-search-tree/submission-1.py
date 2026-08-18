# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = root
        def compare_val(root, p, q):
            if (p.val < root.val < q.val) or (p.val > root.val > q.val):
                self.res = root
            if p.val == root.val:
                self.res = p
            if q.val == root.val:
                self.res = q
            if p.val < root.val and q.val < root.val:
                compare_val(root.left, p, q)
            if p.val > root.val and q.val > root.val:
                compare_val(root.right, p, q)
        compare_val(root, p, q)
        return self.res