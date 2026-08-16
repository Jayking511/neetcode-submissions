# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        is_present = []
        curr = head
        while curr:
            if curr in is_present:
                return True
            is_present.append(curr)
            curr = curr.next
        return False