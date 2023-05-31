#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :use extra space to do it, I am not good at nodetree@.@
@date         :2023/05/31 16:31:23
@version      :1.0
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        list_n = []
        while head:
            list_n.append(head.val)
            head = head.next
        if len(list_n) == 0:
            return head
            
        list_n.reverse()
        
        ans = ListNode(list_n[0])
        curr = ans
        # 遍歷列表，創建對應的節點
        for i in list_n[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return ans