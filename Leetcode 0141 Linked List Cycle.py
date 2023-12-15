"""
12/14/2023
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: 
            return False
        
        slow_p = head
        fast_p = head.next
        while slow_p != fast_p:
            if not fast_p or not fast_p.next:
                return False
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        return True
