# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1 = {}
        d2 = {}
        curr1 = l1
        curr2 = l2
        while curr1:
            d1[curr1] = curr1.val
            curr1 = curr1.next
        while curr2:
            d2[curr2] = curr2.val
            curr2 = curr2.next
        n1 = 0
        n2 = 0
        for i, n in enumerate(d1.values()):
            n1 += n*(10**i)
        for i, n in enumerate(d2.values()):
            n2 += n*(10**i)
        num = n1+n2
        hd = ListNode()
        curr = hd
        while curr:
            nd = ListNode(num%10)
            curr.next = nd
            if num//10 == 0:
                break
            curr = curr.next
            num = num//10
        return hd.next