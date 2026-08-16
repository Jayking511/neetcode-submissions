# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp_lst = []
        curr = head
        while curr:
            temp_lst.append(curr)
            curr = curr.next
        n = len(temp_lst)
        for i in range(n):
            if i == n//2:
                temp_lst[i].next = None
                continue
            if i < n//2:
                temp_lst[i].next = temp_lst[n-i-1]
            else:
                temp_lst[i].next = temp_lst[n-i]
        return None