# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # h -> n -> t
        # n -> h -> t
        # h.next = n.next
        # n.prev = h.prev
        # n.next = h
        if not head:
            return

        curr: ListNode = head
        prev = None
        while curr:
            tmp = curr.next
            
            curr.next = prev
            prev = curr

            curr = tmp
        
        return prev
