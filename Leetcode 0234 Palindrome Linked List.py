# 2025/01/04
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = [head.val]
        h = head
        while h.next:
            a.append(h.next.val)
            h = h.next
        if a == a[::-1]:
            return True
        else:
            return False
