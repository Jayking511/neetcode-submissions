# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        curr = head
        while curr:
            lst.append(curr)
            curr = curr.next
        l = len(lst)
        i = l-n
        if l == 1 and n == 1:
            return
        if i == 0:
            return head.next
        if i == l-1:
            lst[i-1].next = None
            return head
        lst[i-1].next = lst[i+1]
        return head