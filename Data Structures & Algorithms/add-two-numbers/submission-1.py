# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        hd = ListNode()
        curr = hd
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            res = n1 + n2 + carry
            carry = res // 10
            res = res % 10
            
            nd = ListNode(res)
            curr.next = nd
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return hd.next