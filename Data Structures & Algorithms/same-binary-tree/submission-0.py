# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        def check(p, q):
            if not p and not q:
                return
            if (not p and q) or (not q and p):
                self.res = False
                return
            if p.val != q.val:
                self.res = False
                return
            check(p.left, q.left)
            check(p.right, q.right)
            return
        check(p, q)
        return self.res