"""
12/14/2023
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a = ""
        count = 0
        while head:
            a += str(head.val)
            head = head.next
            count+=1
        return int(a, 2)
